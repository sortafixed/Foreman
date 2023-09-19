from page_objects.login_page import LoginPage
from test.base_test import BaseTest
from utilities.test_data import TestData
from page_objects.dashboard_page import MyDashboard


class TestLogin(BaseTest):
    def test_valid_credentials(self):
        login_page = LoginPage(self.driver)
        login_page.log_into_foreman(TestData.username, TestData.password)
        dashboard_title = login_page.get_title()
        assert dashboard_title == "Foreman Dashboard"
        MyDashboard(self.driver).log_out(MyDashboard.dd_user_menu, MyDashboard.dd_user_menu_logout)
        assert self.driver.current_url == TestData.url

