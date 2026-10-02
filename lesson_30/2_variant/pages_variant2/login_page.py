import allure
from playwright.sync_api import Page


class LoginPage:
    def __init__(self, page: Page):
        self.page = page

    @property
    def registration_button(self):
        return self.page.get_by_role("button", name="Registration")

    @allure.step("Open Registration form")
    def open_registration(self):
        self.registration_button.click()
