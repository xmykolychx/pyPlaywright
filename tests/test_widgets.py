from utils.locators import TabsPageLocators


def test_slider(return_pages):
    main_page, widgets_page, slider_page = return_pages('main', 'widgets', 'slider')

    main_page.load()
    main_page.click_widgets()

    widgets_page.click_slider()

    slider_page.change_slider_value('75')


def test_tabs(return_pages):
    main_page, widgets_page, tabs_page = return_pages('main', 'widgets', 'tabs')

    main_page.load()
    main_page.click_widgets()

    widgets_page.click_tabs()

    tabs_page.click_tab(TabsPageLocators.origin_tab)
    origin_aria_selected_true = tabs_page.check_element_attribute_value(TabsPageLocators.origin_tab, 'aria-selected',
                                                                        'true')
    assert origin_aria_selected_true, "Origin tab should have aria-selected attribute with value 'true'"


def test_progress_bar(return_pages):
    main_page, widgets_page, progress_bar_page = return_pages('main', 'widgets', 'progress')

    main_page.load()
    main_page.click_widgets()

    widgets_page.click_progress_bar()

    progress_bar_page.click_start_stop_button()
    progress_bar_page.wait_till_progress_and_stop('75')
