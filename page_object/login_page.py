from constants import ADMIN_LOGIN, ADMIN_PASSWORD
from page_object.base_page import BasePage
from page_object.login_page_locators import LoginPageLocators


class LoginPage(BasePage):

    def try_to_login(self):
        username = self.find_element(LoginPageLocators.USERNAME_INPUT_LOCATORS)
        username.send_keys(ADMIN_LOGIN)
        password = self.find_element(LoginPageLocators.PASSWORD_INPUT_LOCATORS)
        password.send_keys(ADMIN_PASSWORD)
        button = self.find_element(LoginPageLocators.LOG_IN_BUTTON)
        button.click()

