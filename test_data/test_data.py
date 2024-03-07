from faker import Faker


class TestData:
    FAKE = Faker()

    first_name = FAKE.first_name()
    last_name = FAKE.last_name()
    email = FAKE.email()
    phone_number = FAKE.pystr_format(string_format='##########')
    subjects = FAKE.pystr(min_chars=5, max_chars=10)
    address = FAKE.street_address() + FAKE.city()

    dynamic_click_message_text = "You have done a dynamic click"
    right_click_message_text = "You have done a right click"
    double_click_message_text = "You have done a double click"

    created_message = "Link has responded with staus 201 and status text Created"
    no_content_message = "Link has responded with staus 204 and status text No Content"
    moved_message = "Link has responded with staus 301 and status text Moved Permanently"
    bad_request_message = "Link has responded with staus 400 and status text Bad Request"
    unauthorized_message = "Link has responded with staus 401 and status text Unauthorized"
    forbidden_message = "Link has responded with staus 403 and status text Forbidden"
    not_found_message = "Link has responded with staus 404 and status text Not Found"
