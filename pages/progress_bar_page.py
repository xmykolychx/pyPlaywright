from playwright.sync_api import Page
from pages.base_page import BasePage
from utils.locators import ProgressBarPageLocators
from utils.endpoints import Endpoints


class ProgressBarPage(BasePage):
    URL = Endpoints.PROGRESS_BAR_URL

    def __init__(self, page: Page) -> None:
        super(ProgressBarPage, self).__init__(page)

    def click_start_stop_button(self):
        self.page.locator(ProgressBarPageLocators.start_stop_button).click()

    def wait_till_progress_and_stop(self, expected_progress_percentage: str):
        self.check_element_attribute_value(ProgressBarPageLocators.progress_bar, 'aria-valuenow', expected_progress_percentage)
        self.click_start_stop_button()
