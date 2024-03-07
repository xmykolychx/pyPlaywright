def test_form(return_pages):
    main_page, options_page, form_page = return_pages('main', 'options', 'form')

    main_page.load()
    main_page.click_forms()

    options_page.click_practice_form()

    form_page.fill_form()
    form_page.close_form()
