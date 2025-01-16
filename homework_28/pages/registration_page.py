from selenium.webdriver.common.by import By
from pages.base_pages import BasePage

class RegistrationPage(BasePage):
    SIGN_UP_BUTTON = (By.XPATH, "//button[contains(@class, 'sign-up')]")
    FIRST_NAME_INPUT = (By.NAME, "first_name")
    LAST_NAME_INPUT = (By.NAME, "last_name")
    EMAIL_INPUT = (By.NAME, "email")
    PASSWORD_INPUT = (By.NAME, "password")
    CONFIRM_PASSWORD_INPUT = (By.NAME, "password_repeat")
    SUBMIT_BUTTON = (By.XPATH, "//button[@type='submit']")

    def open_registration_form(self):
        self.click_element(self.SIGN_UP_BUTTON)

    def fill_registration_form(self, first_name, last_name, email, password):
        self.send_keys(self.FIRST_NAME_INPUT, first_name)
        self.send_keys(self.LAST_NAME_INPUT, last_name)
        self.send_keys(self.EMAIL_INPUT, email)
        self.send_keys(self.PASSWORD_INPUT, password)
        self.send_keys(self.CONFIRM_PASSWORD_INPUT, password)

    def submit_registration(self):
        self.click_element(self.SUBMIT_BUTTON)