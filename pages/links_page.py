from playwright.sync_api import Page
from pages.base_page import BasePage
from utils.locators import LinksPageLocators
from utils.endpoints import Endpoints



class LinksPage(BasePage):
    URL = Endpoints.LINKS_URL

    def __init__(self, page: Page) -> None:
        super(LinksPage, self).__init__(page)

    def click_home_button(self):
        self.page.locator(LinksPageLocators.home_button).click()
        return self.wait_for_new_tab()

    def click_created(self):
        self.page.locator(LinksPageLocators.created_button).click()

    def click_no_content(self):
        self.page.locator(LinksPageLocators.no_content_button).click()

    def click_not_found(self):
        self.page.locator(LinksPageLocators.not_found_button).click()

    def verify_message(self, expected_text):
        self.page.wait_for_selector(LinksPageLocators.response_message)
        actual_text = self.page.locator(LinksPageLocators.response_message).inner_text()
        assert actual_text == expected_text
