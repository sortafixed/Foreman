
from selenium.webdriver.common.by import By
from page_objects.base_page import BasePage


class MyDashboard(BasePage):
    dd_user_menu = (By.ID, "dd-user-menu")
    dd_user_menu_logout = (By.CLASS_NAME, ".float-right")







