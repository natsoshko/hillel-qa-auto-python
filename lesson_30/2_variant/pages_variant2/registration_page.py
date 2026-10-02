import allure
from playwright.sync_api import Page


class RegistrationPage:
    def __init__(self, page: Page):
        self.page = page

    @property
    def name_input(self):
        return self.page.locator("#signupName")

    @property
    def last_name_input(self):
        return self.page.locator("#signupLastName")

    @property
    def email_input(self):
        return self.page.get_by_role("textbox", name="Name Last name Email")

    @property
    def password_input(self):
        return self.page.get_by_role("textbox", name="Password", exact=True)

    @property
    def repeat_password_input(self):
        return self.page.get_by_role("textbox", name="Re-enter password")

    @property
    def register_button(self):
        return self.page.get_by_role("button", name="Register")

    @property
    def password_mismatch_error(self):
        return (
            self.page
            .locator("#signupRepeatPassword")
            .locator("..")
            .locator(".invalid-feedback p")
        )

    @property
    def name_required_error(self):
        return (
            self.page
            .locator("#signupName")
            .locator("..")
            .locator(".invalid-feedback p")
        )

    @allure.step("Fill registration form")
    def fill_registration_form(
        self,
        name,
        last_name,
        email,
        password,
        repeat_password
    ):
        self.name_input.fill(name)
        self.last_name_input.fill(last_name)
        self.email_input.fill(email)
        self.password_input.fill(password)
        self.repeat_password_input.fill(repeat_password)

    @allure.step("Submit registration form")
    def submit_registration(self):
        self.register_button.click()

    @allure.step("Fill registration form with different passwords")
    def fill_form_with_different_passwords(
        self,
        name,
        last_name,
        email,
        password,
        repeat_password
    ):
        self.name_input.fill(name)
        self.last_name_input.fill(last_name)
        self.email_input.fill(email)
        self.password_input.fill(password)
        self.repeat_password_input.press_sequentially(repeat_password)
        self.repeat_password_input.press("Tab")

    @allure.step("Leave Name field empty")
    def leave_name_empty(self):
        self.name_input.fill("")
        self.name_input.press("Tab")

    @allure.step("Fill registration fields except Name")
    def fill_fields_except_name(
        self,
        last_name,
        email,
        password,
        repeat_password
    ):
        self.last_name_input.fill(last_name)
        self.email_input.fill(email)
        self.password_input.fill(password)
        self.repeat_password_input.fill(repeat_password)

    @allure.step("Register user")
    def register_user(
        self,
        name,
        last_name,
        email,
        password,
        repeat_password
    ):
        self.fill_registration_form(
            name,
            last_name,
            email,
            password,
            repeat_password
        )
        self.submit_registration()