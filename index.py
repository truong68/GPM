from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Mật khẩu mặc định
password ="lebahuy1990!!@@"# Thay bằng mật khẩu mong muốn

# === Đọc số điện thoại từ file ===
def read_phone_number(file_path):
    with open(file_path, "r") as file:
        phone_number = file.readline().strip()
    return phone_number

# Đọc số điện thoại từ file txt
credentials_file = "credentials.txt"  # Đặt tên file chứa số điện thoại
phone_number = read_phone_number(credentials_file)

# === THIẾT LẬP KÍCH THƯỚC MÀN HÌNH ===
custom_screen_width = 1500  # Độ rộng màn hình (px)
custom_screen_height = 870  # Độ cao màn hình (px)

# Xác định số cửa sổ cần mở
num_windows = 9  # 3 hàng, mỗi hàng 3 cửa sổ

# Chia thành 3 hàng và 3 cột
rows, cols = 3, 3

# Tính kích thước mỗi cửa sổ
window_width = custom_screen_width // cols
window_height = custom_screen_height // rows

# Danh sách các URL cần mở
urls = [
    "https://web.enetviet.com/",
    # "https://web.enetviet.com/",
    # "https://web.enetviet.com/",
    # "https://web.enetviet.com/",
    # "https://web.enetviet.com/",
    # "https://web.enetviet.com/",
    # "https://web.enetviet.com/",
    # "https://web.enetviet.com/",
    # "https://web.enetviet.com/",
    # "https://web.enetviet.com/",
    # "https://web.enetviet.com/",
]

# Tắt thông báo trình duyệt
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--disable-notifications")

# Lưu danh sách trình duyệt để không bị đóng
drivers = []

for i, url in enumerate(urls):
    row = i // cols  # Xác định hàng của cửa sổ
    col = i % cols   # Xác định cột của cửa sổ

    # Xác định vị trí cửa sổ
    pos_x = col * window_width
    pos_y = row * window_height

    driver = webdriver.Chrome(options=chrome_options)  # Mở cửa sổ Chrome mới với tùy chọn tắt thông báo
    driver.set_window_size(window_width, window_height)  # Đặt kích thước cửa sổ
    driver.set_window_position(pos_x, pos_y)  # Đặt vị trí cửa sổ
    driver.get(url)  # Truy cập trang web
    drivers.append(driver)  # Lưu driver lại để giữ cửa sổ mở
    time.sleep(1)  # Chờ 1 giây để cửa sổ ổn định

    # Tự động điền số điện thoại và mật khẩu
    try:
        time.sleep(2)  # Chờ trang tải hoàn toàn

        # Nhập số điện thoại
        input_phone = driver.find_element(By.ID, "usename")
        input_phone.send_keys(phone_number)
        print(f"Đã nhập số điện thoại vào cửa sổ {i+1}")
        
        # Nhập mật khẩu
        input_password = driver.find_element(By.ID, "password")
        input_password.send_keys(password)
        print(f"Đã nhập mật khẩu vào cửa sổ {i+1}")
        
        # Tự động bấm nút đăng nhập
        login_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Đăng nhập')]")
        login_button.click()
        print(f"Đã bấm đăng nhập trong cửa sổ {i+1}")
        
        # Chờ đăng nhập thành công
        time.sleep(5)
        
        # Tự động bấm vào thẻ mong muốn sau khi đăng nhập
        target_element = driver.find_element(By.XPATH, "//p[contains(text(), 'Lãnh đạo\nNhà trường')]")
        target_element.click()
        print(f"Đã bấm vào mục 'Lãnh đạo Nhà trường' trong cửa sổ {i+1}")
        
    except Exception as e:
        print(f"Không thể nhập thông tin hoặc đăng nhập vào cửa sổ {i+1}: {e}")

print(f"Đã mở {num_windows} cửa sổ Chrome, chia thành 3 hàng 3 cột trên màn hình!")

# Giữ chương trình chạy để cửa sổ không bị đóng
input("Nhấn Enter để kết thúc chương trình mà không đóng cửa sổ...")


