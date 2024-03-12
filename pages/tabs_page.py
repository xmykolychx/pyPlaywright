from playwright.sync_api import Page
from pages.base_page import BasePage
from utils.endpoints import Endpoints


class TabsPage(BasePage):
    URL = Endpoints.TABS_URL

    def __init__(self, page: Page) -> None:
        super(TabsPage, self).__init__(page)

    def click_tab(self, tab_name):
        self.page.locator(tab_name).click()
