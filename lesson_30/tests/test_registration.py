from pages.garage_page import GaragePage
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.registration_page import RegistrationPage
from faker import Faker
import allure

fake = Faker()

@allure.feature("User registration")
def test_registration(page):
    home_page = HomePage(page)
    login_page = LoginPage(page)
    registration_page = RegistrationPage(page)
    garage_page = GaragePage(page)

    with allure.step("Open Sign In form"):
        home_page.sign_in_button.click()

    with allure.step("Open Registration form"):
        login_page.registration_button.click()

    with allure.step("Fill registration form"):
        registration_page.name_input.fill("User")
        registration_page.last_name_input.fill("Looser")
        registration_page.email_input.fill(fake.email())
        registration_page.password_input.fill("QATest123!")
        registration_page.repeat_password_input.fill("QATest123!")

    with allure.step("Submit registration form"):
        registration_page.register_button.click()
        page.wait_for_url("**/panel/garage")

    with allure.step("Verify successful registration"):
        assert page.url == "https://qauto2.forstudy.space/panel/garage"
        assert garage_page.garage_heading.is_visible()
        assert garage_page.add_car_button.is_visible()


@allure.feature("Registration")
@allure.story("Password validation")
def test_registration_passwords_do_not_match(page):
    home_page = HomePage(page)
    login_page = LoginPage(page)
    registration_page = RegistrationPage(page)

    with allure.step("Open Sign In form"):
        home_page.sign_in_button.click()

    with allure.step("Open Registration form"):
        login_page.registration_button.click()

    with allure.step("Fill registration form with different passwords"):
        registration_page.name_input.fill("User")
        registration_page.last_name_input.fill("Looser")
        registration_page.email_input.fill(fake.email())
        registration_page.password_input.fill("QATest123!")
        #registration_page.repeat_password_input.fill("QATest456!")
        #page.wait_for_timeout(500)
        registration_page.repeat_password_input.press_sequentially("QATest456!")
        registration_page.repeat_password_input.press("Tab")

    with allure.step("Check password mismatch error"):
        assert registration_page.password_mismatch_error.is_visible()

    with allure.step("Verify Register button is disabled"):
        assert registration_page.register_button.is_disabled()

        
@allure.feature("Registration")
@allure.story("Required fields validation")
def test_registration_name_required(page):
    home_page = HomePage(page)
    login_page = LoginPage(page)
    registration_page = RegistrationPage(page)

    with allure.step("Open Sign In form"):
        home_page.sign_in_button.click()

    with allure.step("Open Registration form"):
        login_page.registration_button.click()

    with allure.step("Leave Name field empty"):
        registration_page.name_input.fill("")
        registration_page.name_input.press("Tab")

    with allure.step("Fill other registration fields"):
        registration_page.last_name_input.fill("Looser")
        registration_page.email_input.fill(fake.email())
        registration_page.password_input.fill("QATest123!")
        registration_page.repeat_password_input.fill("QATest123!")

    with allure.step("Check Name required error"):
        assert registration_page.name_required_error.is_visible()

    with allure.step("Verify Register button is disabled"):
        assert registration_page.register_button.is_disabled()