import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from utilities.test_data import TestData


@pytest.fixture(params=["chrome"])
def initialize_driver(request):
    driver = webdriver.Chrome()
    request.cls.driver = driver
    print(f"Browser: {request.param}")
    driver.get(TestData.url)
    yield
    print("Close Driver")
    #driver.close()


