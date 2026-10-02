import allure
from playwright.sync_api import Page

class HomePage:
    def __init__(self, page: Page):
        self.page = page

    @property
    def sign_in_button(self):
        return self.page.get_by_role("button", name="Sign In")

    @allure.step("Open Sign In form")
    def open_sign_in(self):
        self.sign_in_button.click()
