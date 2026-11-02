\# Câu trả lời Lab 04



\## 1. Vì sao release/\* không merge ngược vào master?

Nhánh release lưu một dòng phiên bản đã phát hành.

Các bản sửa cần đưa về master được chuyển qua nhánh và PR riêng,

tránh đưa cấu hình hoặc số phiên bản riêng của release vào master.



\## 2. So sánh với GitFlow

Release Flow trong học phần phát triển tính năng trên master

và duy trì các nhánh release cho từng bản nộp.

GitFlow sử dụng thêm develop làm nhánh tích hợp,

còn main lưu các bản phát hành.



\## 3. Vì sao dùng 1.0.0 thay vì 0.4.0?

Bản 1.0.0 đánh dấu một baseline được xác định là ổn định

và sẵn sàng phát hành theo phạm vi đã thống nhất.

Việc tăng lên 1.0.0 không chỉ phụ thuộc vào số thứ tự bài lab.



\## Ghi nhận kiểm tra bản phát hành

Tag v1.0.0 ban đầu chưa chứa thông tin phiên bản đầy đủ.

Nhánh release/lab04 đã được sửa qua PR để khớp trạng thái

chuẩn bị phát hành. Tag đã xuất bản được giữ nguyên;

vì vậy kiểm tra trực tiếp tag cũ vẫn phản ánh thiếu sót ban đầu.

