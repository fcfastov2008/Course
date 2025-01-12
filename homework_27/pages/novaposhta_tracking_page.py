from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class NovaPoshtaTrackingPage(BasePage):
    TRACKING_INPUT = (By.XPATH, "//input[@placeholder='Введіть номер накладної']")
    TRACKING_BUTTON = (By.XPATH, "//button[contains(text(), 'Знайти')]")
    STATUS_TEXT = (By.XPATH, "//div[contains(@class, 'header__status-text')]")
    ERROR_MESSAGE = (By.XPATH, "//div[contains(@class, 'tracking-error-message')]")

    def enter_tracking_number(self, number):

        self.send_keys(self.TRACKING_INPUT, number)

    def click_search(self):

        self.click_element(self.TRACKING_BUTTON)

    def get_status(self):

        return self.find_element(self.STATUS_TEXT).text

    def get_error_message(self):

        return self.find_element(self.ERROR_MESSAGE).text