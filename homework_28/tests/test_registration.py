
import pytest
import random
import string

@pytest.mark.usefixtures("registration_page")
def test_user_registration(registration_page):
    random_email = f"test_{''.join(random.choices(string.ascii_letters, k=8))}@example.com"
    first_name = "Test"
    last_name = "User"
    password = "StrongPass123"


    registration_page.open_registration_form()


    registration_page.fill_registration_form(first_name, last_name, random_email, password)


    registration_page.submit_registration()


    assert "dashboard" in registration_page.driver.current_url