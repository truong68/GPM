import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QMessageBox, QVBoxLayout

class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Đăng Nhập")
        self.setGeometry(100, 100, 300, 200)

        # Layout chính
        layout = QVBoxLayout()

        # Tạo label và ô nhập tên đăng nhập
        self.label_username = QLabel("Tên đăng nhập:")
        self.input_username = QLineEdit(self)

        # Tạo label và ô nhập mật khẩu
        self.label_password = QLabel("Mật khẩu:")
        self.input_password = QLineEdit(self)
        self.input_password.setEchoMode(QLineEdit.EchoMode.Password)  # Ẩn mật khẩu

        # Nút đăng nhập
        self.btn_login = QPushButton("Đăng nhập")
        self.btn_login.clicked.connect(self.check_login)

        # Thêm vào layout
        layout.addWidget(self.label_username)
        layout.addWidget(self.input_username)
        layout.addWidget(self.label_password)
        layout.addWidget(self.input_password)
        layout.addWidget(self.btn_login)

        self.setLayout(layout)

    def check_login(self):
        username = self.input_username.text()
        password = self.input_password.text()

        # Kiểm tra thông tin đăng nhập
        if username == "admin" and password == "123456":
            QMessageBox.information(self, "Thành công", "Đăng nhập thành công!")
        else:
            QMessageBox.warning(self, "Thất bại", "Tên đăng nhập hoặc mật khẩu sai!")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LoginWindow()
    window.show()
    sys.exit(app.exec())
