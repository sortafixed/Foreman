from selenium.webdriver.common.by import By
from page_objects.base_page import BasePage
from page_objects.dashboard_page import MyDashboard
import time


class LoginPage(BasePage):
    email_field = (By.NAME, "username")
    password_field = (By.NAME, "password")
    sign_in_btn = (By.CLASS_NAME, "sign-in-button")

    def set_email(self, email):
        self.set(self.email_field, email)

    def set_password(self, password):
        self.set(self.password_field, password)

    def click_sign_in_btn(self):
        self.click(self.sign_in_btn)
        return MyDashboard(self.driver)

    def log_into_foreman(self, email, password):
        self.set_email(email)
        self.set_password(password)
        time.sleep(2)
        self.click_sign_in_btn()
