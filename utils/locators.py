class MainPageLocators:
    elements_card = '//*[@id="app"]/div/div/div[2]/div/div[1]'
    forms_card = '//*[@id="app"]/div/div/div[2]/div/div[2]'
    alerts_card = '//*[@id="app"]/div/div/div[2]/div/div[3]'
    widgets_card = '//*[@id="app"]/div/div/div[2]/div/div[4]'
    interactions_card = '//*[@id="app"]/div/div/div[2]/div/div[5]'
    book_store_card = '//*[@id="app"]/div/div/div[2]/div/div[6]'
    tools_qa_logo = '//*[@id="app"]/header/a/img'

class OptionLocators:
    elements_expand_button = ''
    text_box_option_button = ''
    check_box_option_button = ''
    radio_button_option_button = ''
    web_tables_option_button = ''
    buttons_option_button = ''
    links_option_button = ''
    broken_links_option_button = ''
    upld_dwnld_option_button = ''
    dynamic_properties_option_button = ''

    forms_expand_button = ''
    form_option_button = "//span[normalize-space()='Practice Form']"

    # to fill other options

class FormLocators:
    first_name_input = '#firstName'
    last_name_input = '#lastName'
    email_name_input = '#userEmail'
    gender_male_radio_button = "//label[@for='gender-radio-1']"
    gender_female_radio_button = "//label[@for='gender-radio-2']"
    gender_other_radio_button = "//label[@for='gender-radio-3']"
    mobile_input = '#userNumber'
    date_of_birth_input = '#dateOfBirthInput'
    month_dropdown = '.react-datepicker__month-select' # option value 0 january
    year_dropdown = 'react-datepicker__year-select'
    # day react-datepicker__day react-datepicker__day--004 react-datepicker__day--weekend role="option" text 4
    subject_input = '#subjectsInput'
    subject_option = ''
    hobbies_sports_checkbox = "//label[@for='hobbies-checkbox-1']"
    hobbies_reading_checkbox = "//label[@for='hobbies-checkbox-2']"
    hobbies_music_checkbox = "//label[@for='hobbies-checkbox-3']"
    upload_file_button = '#uploadPicture'
    current_address_input = '#currentAddress'
    state_dropdown = "#react-select-3-input"
    city_dropdown = "#react-select-4-input"
    submit_button = '#submit'
    close_form_button = '//*[@id="closeLargeModal"]'

class ElementsPageLocators:
    text_box_button = ""
    check_box_button = ""
    radio_button = ""
    web_tables_button = ""
    buttons_button = "//span[contains(text(), 'Buttons')]"
    links_button = "(//span[normalize-space()='Links'])[1]"
    broken_links_button = ""
    upld_and_dwnld_button = ""
    dynamic_properties_button = "//span[contains(text(), 'Dynamic Properties')]"

class ButtonsPageLocators:
    click_button = "(//button[normalize-space()='Click Me'])[1]"
    right_click_button = "#rightClickBtn"
    double_click_button = "#doubleClickBtn"
    dynamic_click_message = "#dynamicClickMessage"
    right_click_message = "#rightClickMessage"
    double_click_message = "#doubleClickMessage"

class LinksPageLocators:
    # new tab links
    home_button = '#simpleLink'
    another_home_button = '#dynamicLink'

    # api call links
    created_button = '#created'
    no_content_button = '#no-content'
    moved_button = '#moved'
    bad_request_button = '#bad-request'
    unauthorized_button = '#unauthorized'
    forbidden_button = '#forbidden'
    not_found_button = '#invalid-url'

    # messages
    response_message = '#linkResponse'

class DynamicPropertiesPageLocator:
    enable_after_five_sec_button = "#enableAfter"
    color_change_button = "#colorChange"
    visible_after_five_sec_button = "#visibleAfter"

class WidgetsPageLocators:
    slider_option = "//span[contains(text(), 'Slider')]"
    tabs_option = "//span[contains(text(), 'Tabs')]"
    progress_bar_option = "//span[contains(text(), 'Progress Bar')]"

class SliderPageLocators:
    slider = "//input[@type='range']"

class TabsPageLocators:
    what_tab = "#demo-tab-what"
    origin_tab = "#demo-tab-origin"
    use_tab = "#demo-tab-use"

class ProgressBarPageLocators:
    start_stop_button = "#startStopButton"
    progress_bar = "//div[@role='progressbar']"

class AlertsWindowsPageLocators:
    browser_windows_option = "//span[contains(text(), 'Browser Windows')]"
    alerts_option = "//span[contains(text(), 'Alerts')]"
    frames_option = "//span[contains(text(), 'Frames')]"
    nested_frames_option = "//span[contains(text(), 'Nested Frames')]"
    modal_dialogs_option = "//span[contains(text(), 'Modal Dialogs')]"

class AlertsPageLocators:
    alert_button = ""
    alert_five_sec_button = ""
    confirm_button = ""
    prompt_button = ""