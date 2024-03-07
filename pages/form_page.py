from playwright.sync_api import Page
from pages.base_page import BasePage
from utils.endpoints import Endpoints
from utils.locators import FormLocators
from test_data.test_data import TestData
from random import choice


class FormPage(BasePage):
    URL = Endpoints.PRACTICE_FORM_URL

    def __init__(self, page: Page) -> None:
        super(FormPage, self).__init__(page)

    def fill_first_name(self):
        self.page.locator(FormLocators.first_name_input).click()
        self.page.locator(FormLocators.first_name_input).fill(TestData.first_name)

    def fill_last_name(self):
        self.page.locator(FormLocators.last_name_input).click()
        self.page.locator(FormLocators.last_name_input).fill(TestData.last_name)

    def fill_email(self):
        self.page.locator(FormLocators.email_name_input).click()
        self.page.locator(FormLocators.email_name_input).fill(TestData.email)

    def select_gender(self):
        genders = [
            FormLocators.gender_female_radio_button,
            FormLocators.gender_male_radio_button,
            FormLocators.gender_other_radio_button
        ]
        self.page.locator(choice(genders)).click()

    def fill_phone_number(self):
        self.page.locator(FormLocators.mobile_input).click()
        self.page.locator(FormLocators.mobile_input).fill(TestData.phone_number)


    def select_date_of_birth(self):
        self.page.locator(FormLocators.date_of_birth_input).fill('01 Jan 1990')


    def check_hobby(self):
        hobbies = [
            FormLocators.hobbies_music_checkbox,
            FormLocators.hobbies_sports_checkbox,
            FormLocators.hobbies_reading_checkbox
        ]
        for h in hobbies:
            self.page.locator(h).check()

    def fill_current_address(self):
        self.page.locator(FormLocators.current_address_input).click()
        self.page.locator(FormLocators.current_address_input).fill(TestData.address)

    @staticmethod
    def autosuggest_subject(subject):
        return f"//div[contains(@class, 'subjects-auto-complete__menu-list')]//div[text()='{subject}']"

    def select_subject(self, subject):
        sa = self.page.locator(self.autosuggest_subject(subject))
        sa.click()

    def fill_subject(self):
        self.page.locator(FormLocators.subject_input).click()
        self.page.locator(FormLocators.subject_input).fill('E')
        self.select_subject('English')
        self.page.locator(FormLocators.subject_input).fill('P')
        self.select_subject('Physics')

    def click_submit_button(self):
        self.click_option(FormLocators.submit_button)

    def select_state(self):
        self.page.locator(FormLocators.state_dropdown).fill('N')
        self.page.get_by_text("Haryana").click()

    def select_city(self):
        self.page.locator(FormLocators.city_dropdown).fill('a')
        self.page.get_by_text("Panipat").click()

    def fill_form(self):
        self.fill_first_name()
        self.fill_last_name()
        self.fill_email()
        self.select_gender()
        self.fill_phone_number()
        self.select_date_of_birth()
        self.fill_subject()
        self.check_hobby()
        self.fill_current_address()
        self.select_state()
        self.select_city()
        self.click_submit_button()

    def close_form(self):
        # close button is overlapped by google ad so this is the current way of closing
        self.page.evaluate('''() => {
            document.querySelector("button#closeLargeModal").click();
        }''')
