import allure
from faker import Faker

from pages_variant2.home_page import HomePage
from pages_variant2.login_page import LoginPage
from pages_variant2.registration_page import RegistrationPage
from pages_variant2.garage_page import GaragePage


fake = Faker()


@allure.feature("Registration")
@allure.story("Successful registration")
def test_registration(page):
    home_page = HomePage(page)
    login_page = LoginPage(page)
    registration_page = RegistrationPage(page)
    garage_page = GaragePage(page)

    home_page.open_sign_in()
    login_page.open_registration()

    registration_page.register_user(
        name="User",
        last_name="Looser",
        email=fake.email(),
        password="QATest123!",
        repeat_password="QATest123!"
    )

    page.wait_for_url("**/panel/garage")

    garage_page.verify_garage_page()


@allure.feature("Registration")
@allure.story("Password validation")
def test_registration_passwords_do_not_match(page):
    home_page = HomePage(page)
    login_page = LoginPage(page)
    registration_page = RegistrationPage(page)

    home_page.open_sign_in()
    login_page.open_registration()

    registration_page.fill_form_with_different_passwords(
        name="User",
        last_name="Looser",
        email=fake.email(),
        password="QATest123!",
        repeat_password="QATest456!"
    )

    assert registration_page.password_mismatch_error.is_visible()
    assert registration_page.register_button.is_disabled()


@allure.feature("Registration")
@allure.story("Required fields validation")
def test_registration_name_required(page):
    home_page = HomePage(page)
    login_page = LoginPage(page)
    registration_page = RegistrationPage(page)

    home_page.open_sign_in()
    login_page.open_registration()

    registration_page.leave_name_empty()

    registration_page.fill_fields_except_name(
        last_name="Looser",
        email=fake.email(),
        password="QATest123!",
        repeat_password="QATest123!"
    )

    assert registration_page.name_required_error.is_visible()
    assert registration_page.register_button.is_disabled()