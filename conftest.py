import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="function")
def driver():
    # это перед началом теста
    # driver = webdriver.Chrome(ChromeDriverManager().install())
    # options.add_argument('--headless')
    #
    options = Options()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])  # от лишних сообщений в терминале
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), chrome_options=options)
    driver.maximize_window()

    yield driver
    # driver.quit()
