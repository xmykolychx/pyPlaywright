from playwright.sync_api import Page
from pages.base_page import BasePage
from utils.locators import MainPageLocators


class MainPage(BasePage):

    def __init__(self, page: Page) -> None:
        super(MainPage, self).__init__(page)

    def click_elements(self):
        self.page.locator(MainPageLocators.elements_card).click()

    def click_forms(self):
        self.page.locator(MainPageLocators.forms_card).click()

    def click_alerts_frames_windows(self):
        self.page.locator(MainPageLocators.alerts_card).click()

    def click_widgets(self):
        self.page.locator(MainPageLocators.widgets_card).click()

    def click_interactions(self):
        self.page.locator(MainPageLocators.interactions_card).click()

    def click_book_store_application(self):
        self.page.locator(MainPageLocators.book_store_card).click()