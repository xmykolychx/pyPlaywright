from playwright.sync_api import Page
from pages.base_page import BasePage
from utils.locators import AlertsWindowsPageLocators
from utils.endpoints import Endpoints


class AlertsWindowsPage(BasePage):
    URL = Endpoints.ALERTS_WINDOWS_URL

    def __init__(self, page: Page) -> None:
        super(AlertsWindowsPage, self).__init__(page)

