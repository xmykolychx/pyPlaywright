from playwright.sync_api import Page
from pages.base_page import BasePage
from utils.locators import DynamicPropertiesPageLocator
from utils.endpoints import Endpoints



class DynamicPropertiesPage(BasePage):
    URL = Endpoints.DYNAMIC_PROPERTIES_URL

    def __init__(self, page: Page) -> None:
        super(DynamicPropertiesPage, self).__init__(page)

    def click_will_enable_button(self):
        self.page.locator(DynamicPropertiesPageLocator.enable_after_five_sec_button).click()

