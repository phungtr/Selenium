from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
import unittest

class LoginTestSauceDemo(unittest.TestCase):
    BASE_URL = "https://www.saucedemo.com"

    def setUp(self):
        """Thiết lập WebDriver"""
        chrome_service = Service("C:/Users/hienpg/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe")
        self.driver = webdriver.Chrome(service=chrome_service)
        self.driver.get(self.BASE_URL)
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 10)

    def test_login_success(self):
        """Kiểm thử đăng nhập thành công"""
        driver = self.driver
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()

        # Xác nhận trang Products hiển thị sau khi đăng nhập
        inventory_page_title = self.wait.until(
            EC.visibility_of_element_located((By.CLASS_NAME, "title"))
        ).text

        # Kiểm tra tiêu đề không phân biệt chữ hoa/chữ thường
        self.assertEqual(inventory_page_title.upper(), "PRODUCTS")

    def test_login_failure(self):
        """Kiểm thử đăng nhập thất bại"""
        driver = self.driver
        driver.find_element(By.ID, "user-name").send_keys("invalid_user")
        driver.find_element(By.ID, "password").send_keys("invalid_password")
        driver.find_element(By.ID, "login-button").click()

        # Xác nhận thông báo lỗi xuất hiện
        error_message = self.wait.until(
            EC.visibility_of_element_located((By.CLASS_NAME, "error-message-container"))
        ).text
        self.assertIn("Username and password do not match any user", error_message)

    def test_logout(self):
        """Kiểm thử chức năng đăng xuất"""
        driver = self.driver
        # Đăng nhập thành công
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()

        # Mở menu và nhấn nút Logout
        driver.find_element(By.ID, "react-burger-menu-btn").click()
        logout_button = self.wait.until(
            EC.visibility_of_element_located((By.ID, "logout_sidebar_link"))
        )
        logout_button.click()

        # Xác nhận quay về trang đăng nhập
        login_button_visible = self.wait.until(
            EC.visibility_of_element_located((By.ID, "login-button"))
        )
        self.assertTrue(login_button_visible.is_displayed())

    def tearDown(self):
        """Đóng trình duyệt sau mỗi test case"""
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
