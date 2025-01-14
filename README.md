## Kiểm Thử Tự Động với Selenium cho SauceDemo

### Tổng Quan Dự Án :
Dự án này minh họa việc kiểm thử tự động cho ứng dụng web SauceDemo bằng cách sử dụng Selenium và khung kiểm thử unittest của Python. Các bài kiểm thử xác minh các chức năng quan trọng bao gồm đăng nhập thành công, thất bại khi đăng nhập và chức năng đăng xuất.

### Công Nghệ Sử Dụng:

Ngôn Ngữ Lập Trình: Python
Khung Kiểm Thử: unittest
Công Cụ Tự Động Hóa: Selenium WebDriver
Trình Duyệt: Google Chrome

## Yêu Cầu Trước

Cài đặt Python 3.x.
Cài đặt các gói cần thiết:
pip install selenium
Tải xuống ChromeDriver tương thích với phiên bản Chrome .
Đảm bảo đường dẫn đến chromedriver.exe được chỉ định đúng trong mã.
## Cấu Trúc Dự Án

├── Selenium.py  # Tệp kiểm thử chính

└── README.md    # Tài liệu dự án

### `Selenium.py`

![image](https://github.com/user-attachments/assets/3ce84304-7041-4cce-8728-2e7731e647e1)
![image](https://github.com/user-attachments/assets/cfb82645-d71f-4b95-aeae-4c1b8841dab3)
![image](https://github.com/user-attachments/assets/6f876e16-ffdc-436f-bfff-6210efe96f52)

## Các Trường Hợp Kiểm Thử

### 1. Đăng Nhập Thành Công
Mô Tả: Xác minh rằng người dùng có thể đăng nhập với thông tin hợp lệ.
Các Bước:
Nhập tên đăng nhập: standard_user
Nhập mật khẩu: secret_sauce
Nhấn nút đăng nhập.
Xác minh rằng trang "Products" được hiển thị.

### 2. Đăng Nhập Thất Bại
Mô Tả: Xác minh rằng thông báo lỗi xuất hiện khi thông tin đăng nhập không hợp lệ.
Các Bước:
Nhập tên đăng nhập không hợp lệ.
Nhập mật khẩu không hợp lệ.
Nhấn nút đăng nhập.
Xác minh rằng thông báo lỗi xuất hiện.

### 3. Chức Năng Đăng Xuất
Mô Tả: Xác minh rằng người dùng đã đăng nhập có thể đăng xuất thành công.
Các Bước:
Đăng nhập với thông tin hợp lệ.
Mở menu bên.
Nhấn nút đăng xuất.
Xác minh rằng người dùng được chuyển hướng về trang đăng nhập.

## Chạy Mã Kiểm Thử
Mở terminal.
Di chuyển đến thư mục dự án.
Chạy các bài kiểm thử bằng lệnh:
python Selenium.py

## Kết Quả Dự Kiến
Console sẽ hiển thị kết quả kiểm thử cho từng trường hợp, cho biết liệu kiểm thử có thành công hay không.
Ví Dụ Kết Quả

![image](https://github.com/user-attachments/assets/a4c22b1b-d135-48e0-aeef-5397e2207020)

## Lưu Ý Quan Trọng

Đảm bảo phiên bản trình duyệt và ChromeDriver khớp nhau.
Các bài kiểm thử giả định rằng trang web SauceDemo có thể truy cập tại https://www.saucedemo.com.

link chatgpt: https://chatgpt.com/c/67866c9e-40d4-8012-a46e-323d0cb57528
Điều chỉnh thời gian chờ nếu cần thiết để phù hợp với tốc độ tải trang chậm hơn.



