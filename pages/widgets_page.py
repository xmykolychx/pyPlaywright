from playwright.sync_api import Page
from pages.base_page import BasePage
from utils.locators import WidgetsPageLocators
from utils.endpoints import Endpoints


class WidgetsPage(BasePage):
    URL = Endpoints.WIDGETS_URL

    def __init__(self, page: Page) -> None:
        super(WidgetsPage, self).__init__(page)

    def click_slider(self):
        self.page.locator(WidgetsPageLocators.slider_option).click()

    def click_tabs(self):
        self.page.locator(WidgetsPageLocators.tabs_option).click()

    def click_progress_bar(self):
        self.page.locator(WidgetsPageLocators.progress_bar_option).click()
