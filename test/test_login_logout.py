from selenium import webdriver
import time
from selenium.webdriver.common.by import By


def test_mytest():

    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://dashboard.foreman.mn/login/")

    driver.find_element(By.NAME, "username").send_keys("gregoryjwacker@gmail.com")
    driver.find_element(By.NAME, "password").send_keys("B@dDoggy3")
    time.sleep(3)

    driver.find_element(By.CLASS_NAME, "sign-in-button").click()

    user_menu_dropdown = driver.find_element(By.ID, "dd-user-menu")
    user_menu_dropdown.click()

    logout_selection = driver.find_element(By.XPATH, "/html/body/header/div/div/div/div[1]/div[5]/div/a[6]")
    logout_selection.click()
    time.sleep(3)



