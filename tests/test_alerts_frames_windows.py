from utils.locators import AlertsWindowsPageLocators, AlertsPageLocators

# def test_browser_windows(return_pages):
#     pass

def test_alerts(return_pages):
    main_page, alerts_windows_page, alerts_page = return_pages('main', 'alerts_windows', 'alerts')

    main_page.load()
    main_page.click_alerts_frames_windows()

    alerts_windows_page.click_option(AlertsWindowsPageLocators.alerts_option)

    alerts_page.register_alert_handler()
    alerts_page.click_option(AlertsPageLocators.alert_button)
    alerts_page.wait_for_load_state_load()

    alerts_page.register_alert_handler()
    alerts_page.click_option(AlertsPageLocators.timer_alert_button)
    alerts_page.wait_for_load_state_load()


# def test_frames(return_pages):
#     pass
#
# def test_nested_frames(return_pages):
#     pass
#
# def test_modal_dialogs(return_pages):
#     pass