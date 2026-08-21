import pytest
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import AuthPageLocators as Auth
from locators import MainPageLocators as Main
from config import BASE_URL


class TestRegistraion:
    def test_registration_user_success(driver, email):
        driver.get(BASE_URL)
        driver.find_element(*Main.LOGIN_AND_REGISTRATION_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(Auth.DONT_HAVE_ACCOUNT_BUTTON))
        driver.find_element(*Auth.DONT_HAVE_ACCOUNT_BUTTON).click()
        driver.find_element(*Auth.EMAIL_INPUT).send_keys(email)
        driver.find_element(*Auth.PASSWORD_INPUT).send_keys("password123")
        driver.find_element(*Auth.CONFIRM_PASSWORD_INPUT).send_keys("password123")
        driver.find_element(*Auth.CREATE_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Main.USER_NAME))
        assert driver.find_element(*Main.USER_NAME).text == "User.", "отсутствует имя User на странице "
        assert driver.find_element(*Main.USER_AVATAR).is_displayed(), "Отсутствует аватар на странице"

    @pytest.mark.parametrize("wrong_email", ["testmail.ru", "test@mail", "test@.ru", "@mail.ru", "test test@mail.ru", ""])
    def test_registration_with_wrong_email_error(driver, wrong_email):
        driver.get(BASE_URL)
        driver.find_element(*Main.LOGIN_AND_REGISTRATION_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(Auth.DONT_HAVE_ACCOUNT_BUTTON))
        driver.find_element(*Auth.DONT_HAVE_ACCOUNT_BUTTON).click()
        driver.find_element(*Auth.EMAIL_INPUT).send_keys(wrong_email)
        driver.find_element(*Auth.PASSWORD_INPUT).send_keys("password123")
        driver.find_element(*Auth.CONFIRM_PASSWORD_INPUT).send_keys("password123")
        driver.find_element(*Auth.CREATE_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Auth.ERROR_MESSAGE))
        assert driver.find_element(*Auth.ERROR_MESSAGE), "отсутствует сообщение об ошибке"
        assert "rgb(255, 105, 114)" in driver.find_element(*Auth.EMAIL_CONTAINER).value_of_css_property("border"), "Поле email не имеет красной рамки"
        assert "rgb(255, 105, 114)" in driver.find_element(*Auth.PASSWORD_CONTAINER).value_of_css_property("border"), "Поле password не имеет красной рамки"
        assert "rgb(255, 105, 114)" in driver.find_element(*Auth.CONFIRM_PASSWORD_CONTAINER).value_of_css_property("border"), "Поле confrim_password не имеет красной рамки"

    def test_registarion_with_already_registrated_user_error(driver):
        driver.get(BASE_URL)
        driver.find_element(*Main.LOGIN_AND_REGISTRATION_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(Auth.DONT_HAVE_ACCOUNT_BUTTON))
        driver.find_element(*Auth.DONT_HAVE_ACCOUNT_BUTTON).click()
        driver.find_element(*Auth.EMAIL_INPUT).send_keys("testemail@mail.ru")
        driver.find_element(*Auth.PASSWORD_INPUT).send_keys("password123")
        driver.find_element(*Auth.CONFIRM_PASSWORD_INPUT).send_keys("password123")
        driver.find_element(*Auth.CREATE_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Auth.ERROR_MESSAGE))
        assert driver.find_element(*Auth.ERROR_MESSAGE), "отсутствует сообщение об ошибке"
        assert "rgb(255, 105, 114)" in driver.find_element(*Auth.EMAIL_CONTAINER).value_of_css_property("border"), "Поле email не имеет красной рамки"
        assert "rgb(255, 105, 114)" in driver.find_element(*Auth.PASSWORD_CONTAINER).value_of_css_property("border"), "Поле password не имеет красной рамки"
        assert "rgb(255, 105, 114)" in driver.find_element(*Auth.CONFIRM_PASSWORD_CONTAINER).value_of_css_property("border"), "Поле confrim_password не имеет красной рамки"


class TestAuth:
    def test_user_login_success(driver):
        driver.get(BASE_URL)
        driver.find_element(*Main.LOGIN_AND_REGISTRATION_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(Auth.DONT_HAVE_ACCOUNT_BUTTON))
        driver.find_element(*Auth.EMAIL_INPUT).send_keys("testemail@mail.ru")
        driver.find_element(*Auth.PASSWORD_INPUT).send_keys("password123")
        driver.find_element(*Auth.LOGIN_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Main.USER_NAME))
        assert driver.find_element(*Main.USER_NAME).text == "User.", "отсутствует имя User на странице "
        assert driver.find_element(*Main.USER_AVATAR).is_displayed(), "Отсутствует аватар на странице"

    def test_user_logout_success(driver):
        driver.get(BASE_URL)
        driver.find_element(*Main.LOGIN_AND_REGISTRATION_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(Auth.DONT_HAVE_ACCOUNT_BUTTON))
        driver.find_element(*Auth.EMAIL_INPUT).send_keys("testemail@mail.ru")
        driver.find_element(*Auth.PASSWORD_INPUT).send_keys("password123")
        driver.find_element(*Auth.LOGIN_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Main.USER_NAME))
        driver.find_element(*Auth.LOGOUT_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Auth.LOGIN_AND_REGISTRATION_BUTTON))
        assert driver.find_element(*Auth.LOGIN_AND_REGISTRATION_BUTTON), 'отсутствует кнопка "Вход и регистрация" '
        assert len(driver.find_elements(*Main.USER_NAME)) == 0, "На странице присутсвует имя User"
        assert len(driver.find_elements(*Main.USER_AVATAR)) == 0, "На странице присутсвует аватар"
