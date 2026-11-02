\# Use case AIMS-mini



\## Tác nhân

Người dùng ứng dụng AIMS-mini.



\## Các chức năng

\- Thêm DVD vào giỏ hàng.

\- Xóa DVD khỏi giỏ hàng.

\- Xem giỏ hàng.

\- Tính tổng tiền.

\- Tìm DVD theo tiêu đề.



\## Sơ đồ

```mermaid

flowchart LR

&#x20;   User\["Người dùng"]

&#x20;   subgraph AIMS\["AIMS-mini"]

&#x20;       Add(\["Thêm DVD vào giỏ"])

&#x20;       Remove(\["Xóa DVD khỏi giỏ"])

&#x20;       View(\["Xem giỏ hàng"])

&#x20;       Total(\["Tính tổng tiền"])

&#x20;       Search(\["Tìm DVD theo tiêu đề"])

&#x20;   end

&#x20;   User --- Add

&#x20;   User --- Remove

&#x20;   User --- View

&#x20;   User --- Total

&#x20;   User --- Search

```



\## Luồng tìm kiếm theo tiêu đề

1\. Người dùng cung cấp từ khóa.

2\. Chương trình gọi search\_by\_title(items, keyword).

3\. Hàm trả về các DVD có tiêu đề chứa từ khóa.

