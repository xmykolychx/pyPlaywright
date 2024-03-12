def test_form(return_pages):
    main_page, options_page, form_page = return_pages('main', 'options', 'form')

    main_page.load()
    main_page.click_forms()

    options_page.click_practice_form()

    form_page.fill_first_name()
    form_page.fill_last_name()
    form_page.fill_email()
    form_page.select_gender()
    form_page.fill_phone_number()
    form_page.select_date_of_birth()
    form_page.fill_subject()
    form_page.check_hobby()
    form_page.fill_current_address()
    form_page.select_state()
    form_page.select_city()
    form_page.click_submit_button()
    form_page.close_form()
