from test_data.test_data import TestData
from utils.locators import MainPageLocators, DynamicPropertiesPageLocator


def test_buttons(return_pages):
    main_page, elements_page, buttons_page = return_pages('main', 'elements', 'buttons')

    main_page.load()
    main_page.click_elements()

    elements_page.click_buttons()

    buttons_page.click_left()
    buttons_page.click_right()
    buttons_page.click_double()


def test_created(return_pages):
    main_page, elements_page, links_page = return_pages('main', 'elements', 'links')

    main_page.load()
    main_page.click_elements()

    elements_page.click_links()

    links_page.click_created()
    links_page.verify_message(TestData.created_message)


def test_not_found(return_pages):
    main_page, elements_page, links_page = return_pages('main', 'elements', 'links')

    main_page.load()
    main_page.click_elements()

    elements_page.click_links()

    links_page.click_not_found()
    links_page.verify_message(TestData.not_found_message)


def test_click_home(return_pages):
    main_page, elements_page, links_page = return_pages('main', 'elements', 'links')

    main_page.load()
    main_page.click_elements()

    elements_page.click_links()

    new_tab = links_page.click_home_button()
    print("HTML content of the new tab:", new_tab.content())  # Print the HTML content of the new tab for debugging
    new_tab.wait_for_selector(MainPageLocators.tools_qa_logo)


def test_dynamic_properties(return_pages):
    main_page, elements_page, dynamic_properties_page = return_pages('main', 'elements', 'dynamic')

    main_page.load()
    main_page.click_elements()

    elements_page.click_dynamic_properties()

    dynamic_properties_page.check_element_presence(DynamicPropertiesPageLocator.visible_after_five_sec_button)
    dynamic_properties_page.check_element_presence(DynamicPropertiesPageLocator.enable_after_five_sec_button)
    dynamic_properties_page.click_will_enable_button()
    dynamic_properties_page.check_element_class(DynamicPropertiesPageLocator.color_change_button,
                                                "mt-4 text-danger btn btn-primary")
