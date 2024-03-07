from playwright.sync_api import Page
from pages.base_page import BasePage
from utils.locators import SliderPageLocators
from utils.endpoints import Endpoints



class SliderPage(BasePage):
    URL = Endpoints.SLIDER_URL

    def __init__(self, page: Page) -> None:
        super(SliderPage, self).__init__(page)

    def change_slider_value(self, value):
        # Execute JavaScript to set the value of the slider element
        self.page.eval_on_selector(SliderPageLocators.slider, f'(element, value) => element.value = value', value)