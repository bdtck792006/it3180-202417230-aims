\# Câu trả lời Lab 02



\## 1. Vì sao phải đồng bộ master trước khi gửi PR?

Để nhánh làm việc tích hợp các thay đổi mới nhất, phát hiện xung đột

và kiểm tra khả năng hoạt động chung trước khi merge.



\## 2. Khi nào không được rebase?

Không rebase các commit đã chia sẻ mà người khác đang dựa vào,

đặc biệt trên master và release/\*. Rebase thay đổi lịch sử và mã SHA,

có thể gây khó khăn khi đồng bộ.



\## 3. feature/\* khác topic/\* như thế nào?

Theo quy ước của bài lab, feature/\* dùng để phát triển tính năng.

topic/\* dùng cho công việc theo chủ đề như tài liệu, PR template

hoặc chuẩn bị phát hành.

