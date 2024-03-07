from playwright.sync_api import Page
from pages.base_page import BasePage
from utils.locators import OptionLocators
from utils.endpoints import Endpoints


class OptionsPage(BasePage):
    URL = Endpoints.OPTIONS_FORMS_URL

    def __init__(self, page: Page) -> None:
        super(OptionsPage, self).__init__(page)

    def click_practice_form(self):
        self.page.locator(OptionLocators.form_option_button).click()