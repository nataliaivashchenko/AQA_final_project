from selenium.webdriver.common.by import By


class LoginPageLocators:
    USERNAME_INPUT_LOCATORS = (By.XPATH, "//*[@id='id_username']")
    PASSWORD_INPUT_LOCATORS = (By.XPATH, "//*[@id='id_password']")
    LOG_IN_BUTTON = (By.XPATH, "//*[@id='login-form']/div[3]/input")
