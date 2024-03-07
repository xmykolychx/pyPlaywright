from playwright.sync_api import Page, expect
from utils.endpoints import Endpoints


class BasePage(object):
    URL = Endpoints.BASE_URL

    def __init__(self, page: Page):
        self.page = page

    def load(self) -> None:
        self.page.goto(self.URL)

    def get_current_url(self):
        return self.page.url

    def click_option(self, option):
        self.page.locator(option).click()

    def verify_page_content(self, expected_text):
        self.page.wait_for_text(expected_text)

    def wait_for_new_tab(self):
        # Wait for the new tab to open
        new_page = self.page.context.pages[-1]

        # Switch to the new tab
        self.page = new_page

        # Return the reference to the new page
        return self.page

    def check_element_presence(self, expected_locator):
        self.page.locator(expected_locator).is_visible()

    def check_element_class(self, expected_locator, expected_class):
        expect(self.page.locator(expected_locator)).to_have_class(expected_class)

    def check_element_attribute_value(self, selector: str, attribute: str, expected_value: str) -> bool:
        element = self.page.locator(selector)
        actual_value = element.get_attribute(attribute)
        return actual_value == expected_value

    def handle_alert(self, dialog_info):
        dialog_info.accept()

    def register_alert_handler(self):
        # Register the callback to handle the alert
        self.page.context.on("dialog", self.handle_alert)

    def wait_for_load_state_load(self):
        self.page.wait_for_load_state("load")
