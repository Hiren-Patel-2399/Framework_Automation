import pytest
from selenium.webdriver import Chrome

@pytest.fixture
def launch():
    driver=Chrome(executable_path="../Drivers/chromedriver.exe")
    driver.get("https://demowebshop.tricentis.com/")
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    driver.close()
