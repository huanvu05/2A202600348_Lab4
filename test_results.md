# Test Results - Lab 4

Ghi chú:
- File này sẽ được cập nhật sau khi chạy kiểm thử thực tế.
- Mục tiêu là ghi lại console log hoặc tóm tắt ngắn của ít nhất 5 test case theo đề bài.

============================================================
TravelBuddy AI - Trợ lý Du lịch Thông minh
Gõ 'quit' để thoát
============================================================

# Bạn: Xin chào! Tôi đang muốn đi du lịch nhưng chưa bi t đi đâu.

TravelBuddy đang suy nghĩ...
[agent] Trả lời trực tiếp, không gọi tool.

TravelBuddy: Chào bạn! Thật tuyệt khi bạn muốn đi du lịch. Bạn có thể cho mình biết thêm về sở thích của bạn không? Bạn thích khám phá thành phố, thiên nhiên, hay bãi biển? Hoặc nếu bạn có một ngân sách cụ thể nào đó, hãy cho mình biết để mình có thể gợi ý những điểm đến phù hợp nhé!

# Bạn: Tìm giúp tôi chuyễn bay từ Hà Nội đi Đà Nẵng

TravelBuddy đang suy nghĩ...
[tool] search_flights({'origin': 'Hà Nội', 'destination': 'Đà Nẵng'})
[agent] Trả lời trực tiếp, không gọi tool.

TravelBuddy: ✈️ Chuyến bay từ Hà Nội đến Đà Nẵng:

1. **Hãng:** VietJet Air
   - **Giờ bay:** 08:30 - 09:50
   - **Giá:** 890.000₫

2. **Hãng:** Bamboo Airways
   - **Giờ bay:** 11:00 - 12:20
   - **Giá:** 1.200.000₫

3. **Hãng:** Vietnam Airlines
   - **Giờ bay:** 06:00 - 07:20
   - **Giá:** 1.450.000₫

4. **Hãng:** Vietnam Airlines
   - **Giờ bay:** 14:00 - 15:20
   - **Giá:** 2.800.000₫

Bạn có muốn đặt chuyến bay nào trong số này không? Nếu có, hãy cho mình biết thêm về số đêm bạn dự định ở Đà Nẵng và ngân sách cho khách sạn nhé!

# Bạn: Tôi ở Hà Nội, muốn đi Phú Quốc 2 đêm, budget 5 triệu. Tư vấn
giúp!
TravelBuddy đang suy nghĩ...
[tool] search_flights({'origin': 'Hà Nội', 'destination': 'Phú Quốc'})
[tool] search_hotels({'city': 'Phú Quốc', 'max_price_per_night': 1.9})
[tool] search_hotels({'city': 'Phú Quốc', 'max_price_per_night': 1900000})
[tool] calculate_budget({'total_budget': 5000000, 'expenses': '2900000'})
[tool] calculate_budget({'total_budget': 5000000, 'expenses': 'Chuyến bay: 1100000; Khách sạn: 3000000'})
[tool] calculate_budget({'total_budget': 5000000, 'expenses': '1100000'})
[tool] calculate_budget({'total_budget': 5000000, 'expenses': 'Chuyến bay: 1100000'})
[agent] Trả lời trực tiếp, không gọi tool.

TravelBuddy: ✈️ Chuyến bay từ Hà Nội đến Phú Quốc:

- **Hãng:** VietJet Air
  - **Giờ bay:** 16:00 - 18:15
  - **Giá:** 1.100.000₫

🏨 Khách sạn tại Phú Quốc (2 đêm):

1. **9Station Hostel**
   - **Khu vực:** Dương Đông
   - **Giá/đêm:** 200.000₫
   - **Rating:** 4.5

2. **Sol by Meliá**
   - **Khu vực:** Bãi Trường
   - **Giá/đêm:** 1.500.000₫
   - **Rating:** 4.2

3. **Lahana Resort**
   - **Khu vực:** Dương Đông
   - **Giá/đêm:** 800.000₫
   - **Rating:** 4.0

💰 Ngân sách:
- **Tổng ngân sách:** 5.000.000₫
- **Tổng chi:** 2.100.000₫ (Chuyến bay: 1.100.000₫ + Khách sạn: 1.000.000₫ cho 2 đêm tại 9Station Hostel)
- **Còn lại:** 2.900.000₫

📌 Gợi ý thêm:
- Nếu bạn muốn trải nghiệm sang trọng hơn, có thể chọn Sol by Meliá, nhưng sẽ cần điều chỉnh ngân sách.
- Đừng quên kiểm tra thời tiết và các hoạt động tại Phú Quốc để có chuyến đi thú vị nhé! 

Bạn có muốn đặt chuyến bay và khách sạn nào không?

# Bạn: Tôi muốn đặt khách sạn

TravelBuddy đang suy nghĩ...
[tool] search_hotels({'city': 'Phú Quốc', 'max_price_per_night': 2000000})
[agent] Trả lời trực tiếp, không gọi tool.

TravelBuddy: Dưới đây là các lựa chọn khách sạn tại Phú Quốc mà bạn có thể đặt:

1. **9Station Hostel**
   - **Khu vực:** Dương Đông
   - **Giá/đêm:** 200.000₫
   - **Rating:** 4.5

2. **Sol by Meliá**
   - **Khu vực:** Bãi Trường
   - **Giá/đêm:** 1.500.000₫
   - **Rating:** 4.2

3. **Lahana Resort**
   - **Khu vực:** Dương Đông
   - **Giá/đêm:** 800.000₫
   - **Rating:** 4.0

Bạn muốn đặt khách sạn nào trong số này? Hãy cho mình biết để mình có thể giúp bạn hoàn tất đặt phòng nhé!

# Bạn: Giải giúp tôi bài tập lập trình Python về linked list

TravelBuddy đang suy nghĩ...
[agent] Trả lời trực tiếp, không gọi tool.

TravelBuddy: Xin lỗi, nhưng mình không thể giúp bạn với bài tập lập trình. Nếu bạn cần thông tin về du lịch, vé máy bay hoặc khách sạn, hãy cho mình biết nhé!

Bạn: q
Tạm biệt!