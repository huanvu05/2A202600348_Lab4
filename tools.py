from __future__ import annotations

from typing import Any

from langchain_core.tools import tool


FLIGHTS_DB: dict[tuple[str, str], list[dict[str, Any]]] = {
    ("Hà Nội", "Đà Nẵng"): [
        {
            "airline": "Vietnam Airlines",
            "departure": "06:00",
            "arrival": "07:20",
            "price": 1_450_000,
            "class": "economy",
        },
        {
            "airline": "Vietnam Airlines",
            "departure": "14:00",
            "arrival": "15:20",
            "price": 2_800_000,
            "class": "business",
        },
        {
            "airline": "VietJet Air",
            "departure": "08:30",
            "arrival": "09:50",
            "price": 890_000,
            "class": "economy",
        },
        {
            "airline": "Bamboo Airways",
            "departure": "11:00",
            "arrival": "12:20",
            "price": 1_200_000,
            "class": "economy",
        },
    ],
    ("Hà Nội", "Phú Quốc"): [
        {
            "airline": "Vietnam Airlines",
            "departure": "07:00",
            "arrival": "09:15",
            "price": 2_100_000,
            "class": "economy",
        },
        {
            "airline": "VietJet Air",
            "departure": "10:00",
            "arrival": "12:15",
            "price": 1_350_000,
            "class": "economy",
        },
        {
            "airline": "VietJet Air",
            "departure": "16:00",
            "arrival": "18:15",
            "price": 1_100_000,
            "class": "economy",
        },
    ],
    ("Hà Nội", "Hồ Chí Minh"): [
        {
            "airline": "Vietnam Airlines",
            "departure": "06:00",
            "arrival": "08:10",
            "price": 1_600_000,
            "class": "economy",
        },
        {
            "airline": "VietJet Air",
            "departure": "07:30",
            "arrival": "09:40",
            "price": 950_000,
            "class": "economy",
        },
        {
            "airline": "Bamboo Airways",
            "departure": "12:00",
            "arrival": "14:10",
            "price": 1_300_000,
            "class": "economy",
        },
        {
            "airline": "Vietnam Airlines",
            "departure": "18:00",
            "arrival": "20:10",
            "price": 3_200_000,
            "class": "business",
        },
    ],
    ("Hồ Chí Minh", "Đà Nẵng"): [
        {
            "airline": "Vietnam Airlines",
            "departure": "09:00",
            "arrival": "10:20",
            "price": 1_300_000,
            "class": "economy",
        },
        {
            "airline": "VietJet Air",
            "departure": "13:00",
            "arrival": "14:20",
            "price": 780_000,
            "class": "economy",
        },
    ],
    ("Hồ Chí Minh", "Phú Quốc"): [
        {
            "airline": "Vietnam Airlines",
            "departure": "08:00",
            "arrival": "09:00",
            "price": 1_100_000,
            "class": "economy",
        },
        {
            "airline": "VietJet Air",
            "departure": "15:00",
            "arrival": "16:00",
            "price": 650_000,
            "class": "economy",
        },
    ],
}

HOTELS_DB: dict[str, list[dict[str, Any]]] = {
    "Đà Nẵng": [
        {
            "name": "Sala Danang Beach",
            "stars": 5,
            "price_per_night": 1_800_000,
            "area": "Mỹ Khê",
            "rating": 4.5,
        },
        {
            "name": "Mường Thanh Luxury",
            "stars": 4,
            "price_per_night": 1_200_000,
            "area": "Mỹ Khê",
            "rating": 4.3,
        },
        {
            "name": "Fivitel Danang",
            "stars": 3,
            "price_per_night": 650_000,
            "area": "Sơn Trà",
            "rating": 4.1,
        },
        {
            "name": "Memory Hostel",
            "stars": 2,
            "price_per_night": 250_000,
            "area": "Hải Châu",
            "rating": 4.6,
        },
        {
            "name": "Christina's Homestay",
            "stars": 2,
            "price_per_night": 350_000,
            "area": "An Thượng",
            "rating": 4.7,
        },
    ],
    "Phú Quốc": [
        {
            "name": "Vinpearl Resort",
            "stars": 5,
            "price_per_night": 3_500_000,
            "area": "Bãi Dài",
            "rating": 4.4,
        },
        {
            "name": "Sol by Meliá",
            "stars": 4,
            "price_per_night": 1_500_000,
            "area": "Bãi Trường",
            "rating": 4.2,
        },
        {
            "name": "Lahana Resort",
            "stars": 3,
            "price_per_night": 800_000,
            "area": "Dương Đông",
            "rating": 4.0,
        },
        {
            "name": "9Station Hostel",
            "stars": 2,
            "price_per_night": 200_000,
            "area": "Dương Đông",
            "rating": 4.5,
        },
    ],
    "Hồ Chí Minh": [
        {
            "name": "Rex Hotel",
            "stars": 5,
            "price_per_night": 2_800_000,
            "area": "Quận 1",
            "rating": 4.3,
        },
        {
            "name": "Liberty Central",
            "stars": 4,
            "price_per_night": 1_400_000,
            "area": "Quận 1",
            "rating": 4.1,
        },
        {
            "name": "Cochin Zen Hotel",
            "stars": 3,
            "price_per_night": 550_000,
            "area": "Quận 3",
            "rating": 4.4,
        },
        {
            "name": "The Common Room",
            "stars": 2,
            "price_per_night": 180_000,
            "area": "Quận 1",
            "rating": 4.6,
        },
    ],
}


def _format_currency(amount: int) -> str:
    return f"{amount:,}".replace(",", ".") + "₫"


def _normalize_amount(raw_value: str) -> int:
    cleaned = (
        raw_value.strip()
        .replace("_", "")
        .replace(".", "")
        .replace("₫", "")
        .replace("đ", "")
        .replace(" ", "")
    )
    return int(cleaned)


def _parse_expenses(expenses: str) -> list[tuple[str, int]]:
    if not expenses.strip():
        raise ValueError("Danh sách chi phí đang trống.")

    parsed_items: list[tuple[str, int]] = []
    for item in expenses.split(","):
        piece = item.strip()
        if not piece:
            continue
        if ":" not in piece:
            raise ValueError(
                f"Mục '{piece}' không đúng định dạng 'tên_khoản:số_tiền'."
            )
        name, raw_amount = piece.split(":", 1)
        name = name.strip()
        if not name:
            raise ValueError("Tên khoản chi không được để trống.")
        try:
            amount = _normalize_amount(raw_amount)
        except ValueError as exc:
            raise ValueError(
                f"Số tiền của khoản '{name}' không hợp lệ: '{raw_amount.strip()}'."
            ) from exc
        parsed_items.append((name, amount))

    if not parsed_items:
        raise ValueError("Không đọc được khoản chi nào từ chuỗi expenses.")

    return parsed_items


@tool
def search_flights(origin: str, destination: str) -> str:
    """Tìm kiếm các chuyến bay giữa hai thành phố."""

    key = (origin.strip(), destination.strip())
    flights = FLIGHTS_DB.get(key)

    if flights is None:
        reverse_key = (destination.strip(), origin.strip())
        reverse_flights = FLIGHTS_DB.get(reverse_key)
        if reverse_flights is None:
            return f"Không tìm thấy chuyến bay từ {origin} đến {destination}."

        lines = [
            f"Không tìm thấy dữ liệu chiều {origin} -> {destination}.",
            f"Dưới đây là các chuyến tham khảo chiều ngược lại {destination} -> {origin}:",
        ]
        for index, flight in enumerate(sorted(reverse_flights, key=lambda item: item["price"]), start=1):
            lines.append(
                f"{index}. {flight['airline']} | {flight['departure']} - {flight['arrival']} | "
                f"{flight['class']} | {_format_currency(flight['price'])}"
            )
        return "\n".join(lines)

    sorted_flights = sorted(flights, key=lambda item: item["price"])
    lines = [f"Các chuyến bay từ {origin} đến {destination}:"]
    for index, flight in enumerate(sorted_flights, start=1):
        lines.append(
            f"{index}. {flight['airline']} | {flight['departure']} - {flight['arrival']} | "
            f"{flight['class']} | {_format_currency(flight['price'])}"
        )
    return "\n".join(lines)


@tool
def search_hotels(city: str, max_price_per_night: int = 99_999_999) -> str:
    """Tìm kiếm khách sạn theo thành phố và mức giá tối đa mỗi đêm."""

    hotels = HOTELS_DB.get(city.strip())
    if hotels is None:
        return f"Hiện chưa có dữ liệu khách sạn cho thành phố {city}."

    filtered_hotels = [
        hotel for hotel in hotels if hotel["price_per_night"] <= max_price_per_night
    ]
    filtered_hotels.sort(key=lambda item: (-item["rating"], item["price_per_night"]))

    if not filtered_hotels:
        return (
            f"Không tìm thấy khách sạn tại {city} với giá dưới "
            f"{_format_currency(max_price_per_night)}/đêm. Hãy thử tăng ngân sách."
        )

    lines = [
        f"Khách sạn phù hợp tại {city} (tối đa {_format_currency(max_price_per_night)}/đêm):"
    ]
    for index, hotel in enumerate(filtered_hotels, start=1):
        lines.append(
            f"{index}. {hotel['name']} | {hotel['stars']} sao | {hotel['area']} | "
            f"{_format_currency(hotel['price_per_night'])}/đêm | rating {hotel['rating']}"
        )
    return "\n".join(lines)


@tool
def calculate_budget(total_budget: int, expenses: str) -> str:
    """Tính toán ngân sách còn lại dựa trên tổng ngân sách và các khoản chi."""

    try:
        parsed_expenses = _parse_expenses(expenses)
    except ValueError as exc:
        return f"Lỗi dữ liệu chi phí: {exc}"

    total_cost = sum(amount for _, amount in parsed_expenses)
    remaining = total_budget - total_cost

    lines = ["Bảng chi phí:"]
    for name, amount in parsed_expenses:
        pretty_name = name.replace("_", " ").strip().capitalize()
        lines.append(f"- {pretty_name}: {_format_currency(amount)}")

    lines.append("")
    lines.append(f"Tổng chi: {_format_currency(total_cost)}")
    lines.append(f"Ngân sách: {_format_currency(total_budget)}")

    if remaining >= 0:
        lines.append(f"Còn lại: {_format_currency(remaining)}")
    else:
        lines.append(f"Còn lại: -{_format_currency(abs(remaining))}")
        lines.append(
            f"Vượt ngân sách {_format_currency(abs(remaining))}! Cần điều chỉnh."
        )

    return "\n".join(lines)
