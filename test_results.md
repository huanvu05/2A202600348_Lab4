# Test Results - Lab 4

Ghi chú:
- File này sẽ được cập nhật sau khi chạy kiểm thử thực tế.
- Mục tiêu là ghi lại console log hoặc tóm tắt ngắn của ít nhất 5 test case theo đề bài.

(venv) admin@SINCE205---MacPro Lab_4 % python /Users/admin/Documents/AI_ThucChien/assignments/Lab_4/agent.py
============================================================
TravelBuddy AI - Trợ lý Du lịch Thông minh
Gõ 'quit' để thoát
============================================================

Bạn: Xin chào! Tôi đang muốn đi du lịch nhưng chưa bi t đi đâu.

TravelBuddy đang suy nghĩ...
[agent] Trả lời trực tiếp, không gọi tool.

TravelBuddy: Chào bạn! Thật tuyệt khi bạn muốn đi du lịch. Bạn có thể cho mình biết thêm về sở thích của bạn không? Bạn thích biển, núi, hay thành phố? Hoặc nếu bạn có một khoảng thời gian cụ thể và ngân sách nào đó, mình có thể giúp bạn lên kế hoạch tốt hơn!

Bạn: Tìm giúp tôi chuyễn bay từ Hà Nội đi Đà Nẵng

TravelBuddy đang suy nghĩ...
[agent] Trả lời trực tiếp, không gọi tool.

TravelBuddy: Bạn có thể cho mình biết thêm thông tin về chuyến đi không? Bạn dự định đi trong bao nhiêu ngày và có ngân sách cụ thể nào không? Điều này sẽ giúp mình tìm chuyến bay phù hợp hơn cho bạn!

Bạn: Tôi ở Hà Nội, muốn đi Phú Quốc 2 đêm, budget 5 triệu. Tư vấn
giúp!
TravelBuddy đang suy nghĩ...
[tool] search_flights({'origin': 'Hà Nội', 'destination': 'Phú Quốc'})
[tool] search_hotels({'city': 'Phú Quốc', 'max_price_per_night': 1850000})
[tool] calculate_budget({'total_budget': 5000000, 'expenses': '1100000 + 1500000 * 2'})
[tool] calculate_budget({'total_budget': 5000000, 'expenses': '1100000 + 3000000'})
[tool] calculate_budget({'total_budget': 5000000, 'expenses': 'vé máy bay:1100000, khách sạn:3000000'})
[agent] Trả lời trực tiếp, không gọi tool.

TravelBuddy: ✈️ Chuyến bay:
- Hãng: VietJet Air
- Giờ bay: 16:00 - 18:15
- Giá: 1.100.000₫

🏨 Khách sạn:
- Tên: Sol by Meliá
- Khu vực: Bãi Trường
- Giá/đêm: 1.500.000₫
- Rating: 4.2

💰 Ngân sách:
- Tổng ngân sách: 5.000.000₫
- Tổng chi: 4.100.000₫
- Còn lại: 900.000₫

📌 Gợi ý thêm:
- Bạn có thể sử dụng số tiền còn lại để thưởng thức các món ăn ngon hoặc tham gia các hoạt động giải trí tại Phú Quốc. 
- Đừng quên mang theo đồ bơi để tận hưởng biển cả nhé!

Bạn: Tôi muốn đặt khách sạn

TravelBuddy đang suy nghĩ...
[agent] Trả lời trực tiếp, không gọi tool.

TravelBuddy: Mình không thể đặt khách sạn trực tiếp, nhưng mình có thể cung cấp thông tin để bạn có thể đặt. Bạn có muốn mình gửi thông tin chi tiết về khách sạn Sol by Meliá để bạn có thể liên hệ đặt phòng không?

Bạn: Giải giúp tôi bài tập lập trình Python về linked list

TravelBuddy đang suy nghĩ...
[agent] Trả lời trực tiếp, không gọi tool.

TravelBuddy: Xin lỗi, nhưng mình chỉ hỗ trợ các yêu cầu liên quan đến du lịch. Nếu bạn cần giúp đỡ về chuyến đi hoặc đặt vé máy bay, khách sạn, hãy cho mình biết nhé!
