from selenium import webdriver


class BasePage:
    """
    The Purpose of BasePage is to contain methods common to all Page Objects
    """

    def __init__(self, driver):
        self.driver = driver

    def find(self, *locator):
        return self.driver.find_element(*locator)

    def click(self, locator):
        self.find(*locator).click()

    def log_out(self, menu_locator, sub_menu_locator):
        menu = self.find(*menu_locator)
        menu.click()
        sub_menu = self.find(*sub_menu_locator)
        sub_menu.click()

    def set(self, locator, value):
        self.find(*locator).clear()
        self.find(*locator).send_keys(value)

    def get_text(self, locator):
        return self.find(*locator).text

    def get_title(self):
        return self.driver.title

    def get_url(self):
        return self.driver.is_element_present


