from playwright.sync_api import Page


class RegistrationPage:
    def __init__(self, page: Page):
        self.page = page

    @property
    def name_input(self):
        return self.page.locator("#signupName")

    @property
    def name_required_error(self):
        return self.page.locator("#signupName").locator("..").locator(".invalid-feedback p")

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
    def password_mismatch_error(self):
        return self.page.locator("#signupRepeatPassword").locator("..").locator(".invalid-feedback p")

    @property
    def register_button(self):
        return self.page.get_by_role("button", name="Register")