from selenium.webdriver.common.by import By


class AuthPageLocators:
    DONT_HAVE_ACCOUNT_BUTTON = (By.XPATH, "//button[text()='Нет аккаунта']")
    EMAIL_INPUT = (By.NAME, "email")
    PASSWORD_INPUT = (By.NAME, "password")
    CONFIRM_PASSWORD_INPUT = (By.NAME, "submitPassword")
    CREATE_ACCOUNT_BUTTON = (By.XPATH, "//button[text()='Создать аккаунт']")
    ERROR_MESSAGE = (By.CLASS_NAME, "input_span__yWPqB")
    EMAIL_CONTAINER = (By.XPATH, "//input[@name='email']/parent::div")
    PASSWORD_CONTAINER = (By.XPATH, "//input[@name='password']/parent::div")
    CONFIRM_PASSWORD_CONTAINER = (By.XPATH, "//input[@name='submitPassword']/parent::div")
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']")
    LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выйти']")


class MainPageLocators:
    USER_NAME = (By.CSS_SELECTOR, ".profileText.name")
    USER_AVATAR = (By.CLASS_NAME, "svgSmall")
    LOGIN_AND_REGISTRATION_BUTTON = (By.XPATH, "//button[text()='Вход и регистрация']")
    MAKE_AD_BUTTON = (By.XPATH, "//button[text()='Разместить объявление']")
    USER_CLICK = (By.CLASS_NAME, "circleSmall")
    SEARCH = (By.CLASS_NAME, "input_inputDefaultSearch__EKhe3")


class AdPageLocators:
    AD_FORM_REGISTRATION = (By.CLASS_NAME, "popUp_shell__LuyqR")
    AD_FORM_REGISTRATION_TEXT = (By.XPATH, "//form/div/h1")
    AD_FORM = (By.CLASS_NAME, "createListingPage_createListingPageStyle__U-MJJ")
    AD_NAME = (By.NAME, "name")
    AD_DESCRIPTION = (By.CSS_SELECTOR, "textarea[name='description']")
    AD_COST = (By.NAME, "price")
    AD_TYPE_ARROW = (By.XPATH, "//input[@name='category']/parent::div/button")
    AD_CITY_ARROW = (By.XPATH, "//input[@name='city']/parent::div/button")
    AD_TYPE = (By.XPATH, "//button[.='Книги']")
    AD_CITY = (By.XPATH, "//button[.='Нижний Новгород']")
    AD_STATE = (By.CLASS_NAME, "radioUnput_inputRegular__FbVbr")
    AD_SUBMIT_BUTTON = (By.XPATH, "//button[text()='Опубликовать']")
    MY_ADS = (By.XPATH, "//div[@class='card']")
    MY_PROFILE = (By.CLASS_NAME, "circleLarge")
    AD_CARDS_TITLES = (By.XPATH, "//div[@class='card']//h2[@class='h2']")
