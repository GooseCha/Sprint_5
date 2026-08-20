import pytest
import random as r
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture
def driver():
    chrome_options = Options()

    chrome_options.add_experimental_option("detach", True)

    prefs = {
        "credentials_enable_service": False,  # Все пункты настроек сделал через ИИ
        "profile.password_manager_enabled": False,  # Хром часто ругался на "Слитый пароль"
        "profile.password_manager_leak_detection": False,  # Который использовался для теста
    }
    chrome_options.add_experimental_option("prefs", prefs)

    driver = webdriver.Chrome(options=chrome_options)
    return driver


@pytest.fixture
def email():
    email = str(r.randint(100, 999999999)) + "@mail.ru"
    return email
