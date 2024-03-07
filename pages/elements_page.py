from playwright.sync_api import Page
from pages.base_page import BasePage
from utils.locators import ElementsPageLocators
from utils.endpoints import Endpoints
class ElementsPage(BasePage):
    URL = Endpoints.ELEMENTS_PAGE_URL

    def __init__(self, page: Page) -> None:
        super(ElementsPage, self).__init__(page)

    def click_buttons(self):
        self.page.locator(ElementsPageLocators.buttons_button).click()

    def click_links(self):
        self.page.locator(ElementsPageLocators.links_button).click()

    def click_dynamic_properties(self):
        self.page.locator(ElementsPageLocators.dynamic_properties_button).click()

