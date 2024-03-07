from playwright.sync_api import Page, expect
from pages.base_page import BasePage
from utils.locators import ButtonsPageLocators
from utils.endpoints import Endpoints
from test_data.test_data import TestData


class ButtonsPage(BasePage):
    URL = Endpoints.BUTTONS_URL

    def __init__(self, page: Page) -> None:
        super(ButtonsPage, self).__init__(page)

    def click_left(self):
        self.page.locator(ButtonsPageLocators.click_button).click()
        expect(self.page.locator(ButtonsPageLocators.dynamic_click_message)).to_have_text(TestData.dynamic_click_message_text)

    def click_right(self):
        self.page.locator(ButtonsPageLocators.right_click_button).click(button="right")
        expect(self.page.locator(ButtonsPageLocators.right_click_message)).to_have_text(TestData.right_click_message_text)

    def click_double(self):
        self.page.locator(ButtonsPageLocators.double_click_button).dblclick()
        expect(self.page.locator(ButtonsPageLocators.double_click_message)).to_have_text(TestData.double_click_message_text)
