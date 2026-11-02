\# Câu trả lời Lab 05



\## 1. Ưu, nhược điểm của upstream first so với release first?



\### Upstream first

Sửa lỗi trên nhánh phát triển chính trước, sau đó chuyển bản sửa

sang các nhánh release bị ảnh hưởng.



Ưu điểm:

\- Nhánh chính nhận bản sửa sớm, giảm nguy cơ lỗi xuất hiện lại.

\- Có thể kiểm tra bản sửa cùng các thay đổi phát triển mới.



Nhược điểm:

\- Bản sửa có thể phụ thuộc mã mới chưa có trên release.

\- Khi đưa về phiên bản cũ có thể phải điều chỉnh hoặc xử lý xung đột.



\### Release first

Sửa trên nhánh release bị ảnh hưởng trước, sau đó chuyển bản sửa

về master và các release khác.



Ưu điểm:

\- Tập trung sửa và kiểm tra đúng phiên bản đang gặp lỗi.

\- Có thể phát hành bản vá mà không đưa thêm tính năng mới vào.



Nhược điểm:

\- Có thể quên chuyển bản sửa sang các dòng phiên bản khác.

\- Cần theo dõi và kiểm toán việc lan truyền bản sửa.



\## 2. Nếu quên chuyển bản sửa sang release/lab05, phát hiện thế nào?



Kiểm tra các commit có thông tin nguồn gốc:

git log --all --oneline --grep="cherry picked from commit 8af1d45"



Sau đó kiểm tra commit tương ứng có nằm trong release/lab05:

git branch -r --contains cc1be7c



Kiểm tra hành vi tìm "lion" trên release/lab05:

nếu trả về danh sách rỗng thì phiên bản này vẫn còn lỗi.



Chỉ đếm số commit cherry-pick chưa đủ để xác nhận chúng đã được

merge vào đúng nhánh đích.

