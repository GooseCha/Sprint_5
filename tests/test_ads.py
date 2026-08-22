import pytest
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import AuthPageLocators as Auth
from locators import MainPageLocators as Main
from locators import AdPageLocators as Ad
from config import BASE_URL


class TestAds:
    def test_ad_creation_by_unauthorized_user_error(self, driver):
        driver.get(BASE_URL)
        driver.find_element(*Main.MAKE_AD_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Ad.AD_FORM_REGISTRATION))
        assert driver.find_element(*Ad.AD_FORM_REGISTRATION_TEXT), "Окно регистрации отсутсвует"
        assert driver.find_element(*Ad.AD_FORM_REGISTRATION_TEXT).text == "Чтобы разместить объявление, авторизуйтесь", "отсутствует заголовок окна регистрации"

    def test_ad_creation_by_authorized_user_success(self, driver):
        driver.get(BASE_URL)
        driver.find_element(*Main.LOGIN_AND_REGISTRATION_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(Auth.DONT_HAVE_ACCOUNT_BUTTON))
        driver.find_element(*Auth.EMAIL_INPUT).send_keys("testemail@mail.ru")
        driver.find_element(*Auth.PASSWORD_INPUT).send_keys("password123")
        driver.find_element(*Auth.LOGIN_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Main.USER_NAME))
        driver.find_element(*Main.MAKE_AD_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Ad.AD_FORM))
        driver.find_element(*Ad.AD_NAME).send_keys("Тестовое объявление")
        driver.find_element(*Ad.AD_DESCRIPTION).send_keys("Тестовое описание объявления")
        driver.find_element(*Ad.AD_COST).send_keys("116")
        driver.find_element(*Ad.AD_TYPE_ARROW).click()
        driver.find_element(*Ad.AD_TYPE).click()
        driver.find_element(*Ad.AD_CITY_ARROW).click()
        driver.find_element(*Ad.AD_CITY).click()
        driver.find_element(*Ad.AD_STATE).click()
        driver.find_element(*Ad.AD_SUBMIT_BUTTON).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Main.SEARCH))
        driver.find_element(*Main.USER_CLICK).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Ad.MY_ADS))
        ad_titles = driver.find_elements(*Ad.AD_CARDS_TITLES)
        ad_titles_text = [title.text for title in ad_titles]
        assert "Тестовое объявление" in ad_titles_text, "Объявление не найдено в профиле"
