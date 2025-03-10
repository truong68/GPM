from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# === Mật khẩu mặc định ===
password = "lebahuy1990!!@@"

# === Đọc số điện thoại từ file ===
def read_phone_number(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        return file.readline().strip()

# === Đọc tiêu đề từ file ===
def read_title_content(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        return file.readline().strip()

# === Đọc nội dung từ file ===
def read_content(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read().strip()  # Đọc toàn bộ nội dung

# Đọc số điện thoại, tiêu đề và nội dung từ file txt
credentials_file = "credentials.txt"
title_file = "title.txt"
content_file = "content.txt"

phone_number = read_phone_number(credentials_file)
title_content = read_title_content(title_file)
message_content = read_content(content_file)  # Đọc nội dung từ file

# === THIẾT LẬP KÍCH THƯỚC MÀN HÌNH ===
custom_screen_width = 1500
custom_screen_height = 870

# Xác định số cửa sổ cần mở
num_windows = 1

# Danh sách các URL cần mở
urls = ["https://web.enetviet.com/"] * num_windows

# Tắt thông báo trình duyệt
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--disable-notifications")

# Lưu danh sách trình duyệt để không bị đóng
drivers = []

for i, url in enumerate(urls):
    driver = webdriver.Chrome(options=chrome_options)
    driver.set_window_size(custom_screen_width, custom_screen_height)
    driver.get(url)
    drivers.append(driver)
    time.sleep(1)

    try:
        time.sleep(2)

        # Nhập số điện thoại
        input_phone = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "usename"))
        )
        input_phone.send_keys(phone_number)

        # Nhập mật khẩu
        input_password = driver.find_element(By.ID, "password")
        input_password.send_keys(password)

        # Bấm nút đăng nhập
        login_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Đăng nhập')]")
        login_button.click()

        # Chờ đăng nhập thành công
        time.sleep(5)

        # Bấm vào thẻ 'Lãnh đạo Nhà trường'
        leadership_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//p[contains(text(), 'Lãnh đạo') and contains(text(), 'Nhà trường')]"))
        )
        leadership_button.click()
        time.sleep(2)

        # Bấm vào thẻ 'Gửi thông báo'
        send_notification_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//div[contains(text(), 'Gửi thông báo')]"))
        )
        send_notification_button.click()
        time.sleep(2)

        # Bấm vào thẻ 'Học sinh toàn trường'
        student_notification_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//div[contains(@class, 'MuiBox-root') and contains(text(), 'Học sinh toàn trường')]"))
        )
        driver.execute_script("arguments[0].click();", student_notification_button)
        time.sleep(2)

        # Bấm vào ảnh trong thẻ div
        img_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//div[contains(@class, 'p-3 bg-[#C5DCF3] rounded-[20px]')]//img"))
        )
        driver.execute_script("arguments[0].click();", img_button)
        time.sleep(2)

        # Nhập nội dung vào ô tiêu đề
        input_title = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "txtTieuDe"))
        )
        input_title.clear()
        input_title.send_keys(title_content)
        time.sleep(2)

        # === Nhập nội dung vào ô nội dung ===
        input_content = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//textarea[@name='txtNoiDung']"))  # Xpath cho ô nhập nội dung
        )
        input_content.clear()
        input_content.send_keys(message_content)
        print(f"✅ Đã nhập nội dung thông báo vào cửa sổ {i+1}")
        time.sleep(2)

        # === Chọn checkbox ===
        checkbox = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@type='checkbox' and contains(@class, 'form-control')]"))
        )
        driver.execute_script("arguments[0].click();", checkbox)
        print(f"✅ Đã chọn checkbox trong cửa sổ {i+1}")
        time.sleep(2)

        # === Click vào nút "Gửi thông báo" ===
        send_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'MuiButton-containedPrimary') and contains(text(), 'Gửi thông báo')]"))
        )
        driver.execute_script("arguments[0].click();", send_button)
        print(f"✅ Đã gửi thông báo trong cửa sổ {i+1}")
        time.sleep(5)

    except Exception as e:
        print(f"❌ Lỗi trong cửa sổ {i+1}: {e}")

print(f"🚀 Đã mở {num_windows} cửa sổ Chrome và hoàn thành các thao tác tự động!")

# Giữ chương trình chạy để cửa sổ không bị đóng
input("Nhấn Enter để kết thúc chương trình mà không đóng cửa sổ...")
