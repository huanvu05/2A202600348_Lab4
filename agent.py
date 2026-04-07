from __future__ import annotations

import os
from pathlib import Path
from typing import Annotated

from dotenv import load_dotenv
from langchain_core.messages import AIMessage, BaseMessage, HumanMessage, SystemMessage
from langgraph.graph import END, START, StateGraph
from langgraph.graph.message import add_messages
from langgraph.prebuilt import ToolNode, tools_condition
from langchain_openai import ChatOpenAI
from typing_extensions import TypedDict

from tools import calculate_budget, search_flights, search_hotels


BASE_DIR = Path(__file__).resolve().parent
SYSTEM_PROMPT_PATH = BASE_DIR / "system_prompt.txt"


def load_environment() -> None:
    load_dotenv(BASE_DIR / ".env")
    load_dotenv(BASE_DIR.parent / ".env")


def load_system_prompt() -> str:
    return SYSTEM_PROMPT_PATH.read_text(encoding="utf-8").strip()


def build_llm() -> ChatOpenAI:
    github_token = os.getenv("GITHUB_TOKEN")
    if github_token:
        return ChatOpenAI(
            model=os.getenv("GITHUB_MODEL", "openai/gpt-4o-mini"),
            api_key=github_token,
            base_url=os.getenv(
                "GITHUB_MODELS_BASE_URL",
                "https://models.github.ai/inference",
            ),
            default_headers={
                "Accept": "application/vnd.github+json",
                "X-GitHub-Api-Version": "2022-11-28",
            },
            temperature=0,
            timeout=60,
        )

    openai_api_key = os.getenv("OPENAI_API_KEY")
    if openai_api_key:
        return ChatOpenAI(
            model=os.getenv("OPENAI_MODEL", "gpt-4o-mini"),
            temperature=0,
            timeout=60,
        )

    raise RuntimeError(
        "Không tìm thấy OPENAI_API_KEY hoặc GITHUB_TOKEN. "
        "Hãy cấu hình biến môi trường trước khi chạy agent. "
        "Nếu dùng GitHub Models, token cần có quyền models:read."
    )


load_environment()
SYSTEM_PROMPT = load_system_prompt()


class AgentState(TypedDict):
    messages: Annotated[list[BaseMessage], add_messages]


TOOLS = [search_flights, search_hotels, calculate_budget]
LLM = build_llm()
LLM_WITH_TOOLS = LLM.bind_tools(TOOLS)


def agent_node(state: AgentState) -> AgentState:
    messages = list(state["messages"])
    if not messages or not isinstance(messages[0], SystemMessage):
        messages = [SystemMessage(content=SYSTEM_PROMPT), *messages]

    response = LLM_WITH_TOOLS.invoke(messages)

    if response.tool_calls:
        for tool_call in response.tool_calls:
            print(f"[tool] {tool_call['name']}({tool_call['args']})")
    else:
        print("[agent] Trả lời trực tiếp, không gọi tool.")

    return {"messages": [response]}


def build_graph():
    builder = StateGraph(AgentState)
    builder.add_node("agent", agent_node)
    builder.add_node("tools", ToolNode(TOOLS))

    builder.add_edge(START, "agent")
    builder.add_conditional_edges(
        "agent",
        tools_condition,
        {
            "tools": "tools",
            "__end__": END,
        },
    )
    builder.add_edge("tools", "agent")

    return builder.compile()


GRAPH = build_graph()


def run_chat_loop() -> None:
    print("=" * 60)
    print("TravelBuddy AI - Trợ lý Du lịch Thông minh")
    print("Gõ 'quit' để thoát")
    print("=" * 60)

    conversation: list[BaseMessage] = []

    while True:
        user_input = input("\nBạn: ").strip()
        if user_input.lower() in {"quit", "exit", "q"}:
            print("Tạm biệt!")
            break
        if not user_input:
            continue

        conversation.append(HumanMessage(content=user_input))
        print("\nTravelBuddy đang suy nghĩ...")

        result = GRAPH.invoke({"messages": conversation})
        conversation = result["messages"]

        final_message = conversation[-1]
        if isinstance(final_message, AIMessage):
            print(f"\nTravelBuddy: {final_message.content}")
        else:
            print("\nTravelBuddy: Không nhận được phản hồi hợp lệ từ agent.")


if __name__ == "__main__":
    run_chat_loop()
