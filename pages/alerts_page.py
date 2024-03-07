from playwright.sync_api import Page
from pages.base_page import BasePage
from utils.locators import AlertsPageLocators
from utils.endpoints import Endpoints


class AlertsPage(BasePage):
    URL = Endpoints.ALERTS_WINDOWS_URL

    def __init__(self, page: Page) -> None:
        super(AlertsPage, self).__init__(page)