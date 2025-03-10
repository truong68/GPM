from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# === Mật khẩu mặc định ===
password = "lebahuy1990!!@@"  # Thay bằng mật khẩu mong muốn

# === Đọc số điện thoại từ file ===
def read_phone_number(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        return file.readline().strip()

# === Đọc tiêu đề từ file ===
def read_title_content(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        return file.readline().strip()

# Đọc số điện thoại và tiêu đề từ file txt
credentials_file = "credentials.txt"  # File chứa số điện thoại
title_file = "title.txt"  # File chứa tiêu đề
phone_number = read_phone_number(credentials_file)
title_content = read_title_content(title_file)

# === THIẾT LẬP KÍCH THƯỚC MÀN HÌNH ===
custom_screen_width = 1500  # Độ rộng màn hình (px)
custom_screen_height = 870  # Độ cao màn hình (px)

# Xác định số cửa sổ cần mở
num_windows = 1  # Thay đổi nếu muốn mở nhiều cửa sổ

# Danh sách các URL cần mở
urls = ["https://web.enetviet.com/"] * num_windows

# Tắt thông báo trình duyệt
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--disable-notifications")

# Lưu danh sách trình duyệt để không bị đóng
drivers = []

for i, url in enumerate(urls):
    driver = webdriver.Chrome(options=chrome_options)  # Mở trình duyệt mới
    driver.set_window_size(custom_screen_width, custom_screen_height)  # Đặt kích thước cửa sổ
    driver.get(url)  # Truy cập trang web
    drivers.append(driver)  # Lưu driver lại để giữ cửa sổ mở
    time.sleep(1)  # Chờ 1 giây để cửa sổ ổn định

    # Tự động điền số điện thoại và mật khẩu
    try:
        time.sleep(2)  # Chờ trang tải hoàn toàn

        # Nhập số điện thoại
        input_phone = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "usename"))
        )
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

        # Tự động bấm vào thẻ 'Lãnh đạo Nhà trường'
        try:
            leadership_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//p[contains(text(), 'Lãnh đạo') and contains(text(), 'Nhà trường')]"))
            )
            driver.execute_script("arguments[0].scrollIntoView();", leadership_button)
            leadership_button.click()
            print(f"Đã bấm vào thẻ 'Lãnh đạo Nhà trường' trong cửa sổ {i+1}")
            time.sleep(2)
        except Exception as e:
            print(f"Không thể bấm vào thẻ 'Lãnh đạo Nhà trường' trong cửa sổ {i+1}: {e}")

        # Tự động bấm vào thẻ 'Gửi thông báo'
        try:
            send_notification_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//div[contains(text(), 'Gửi thông báo')]"))
            )
            driver.execute_script("arguments[0].scrollIntoView();", send_notification_button)
            send_notification_button.click()
            print(f"Đã bấm vào thẻ 'Gửi thông báo' trong cửa sổ {i+1}")
            time.sleep(2)
        except Exception as e:
            print(f"Không thể bấm vào thẻ 'Gửi thông báo' trong cửa sổ {i+1}: {e}")

        # Tự động bấm vào thẻ 'Học sinh toàn trường'
        try:
            student_notification_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//div[contains(@class, 'MuiBox-root') and contains(text(), 'Học sinh toàn trường')]"))
            )
            driver.execute_script("arguments[0].scrollIntoView();", student_notification_button)
            driver.execute_script("arguments[0].click();", student_notification_button)
            print(f"Đã bấm vào thẻ 'Học sinh toàn trường' trong cửa sổ {i+1}")
            time.sleep(2)
        except Exception as e:
            print(f"Không thể bấm vào thẻ 'Học sinh toàn trường' trong cửa sổ {i+1}: {e}")

        # Tự động bấm vào icon img trong thẻ div
        try:
            img_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//div[contains(@class, 'p-3 bg-[#C5DCF3] rounded-[20px]')]//img"))
            )
            driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", img_button)
            driver.execute_script("arguments[0].click();", img_button)
            print(f"Đã bấm vào ảnh trong cửa sổ {i+1}")
            time.sleep(2)
        except Exception as e:
            print(f"Không thể bấm vào ảnh trong cửa sổ {i+1}: {e}")

        # Tự động nhập nội dung vào ô input tiêu đề
        try:
            input_title = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.NAME, "txtTieuDe"))
            )
            input_title.clear()
            time.sleep(1)
            input_title.send_keys(title_content)
            print(f"Đã nhập tiêu đề: '{title_content}' vào ô trong cửa sổ {i+1}")
            time.sleep(2)
        except Exception as e:
            print(f"Không thể nhập nội dung vào ô tiêu đề trong cửa sổ {i+1}: {e}")

    except Exception as e:
        print(f"Không thể nhập thông tin hoặc đăng nhập vào cửa sổ {i+1}: {e}")

print(f"Đã mở {num_windows} cửa sổ Chrome và hoàn thành các thao tác tự động!")

# Giữ chương trình chạy để cửa sổ không bị đóng
input("Nhấn Enter để kết thúc chương trình mà không đóng cửa sổ...")
