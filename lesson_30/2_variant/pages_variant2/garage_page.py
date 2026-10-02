import allure
from playwright.sync_api import Page


class GaragePage:
    def __init__(self, page: Page):
        self.page = page

    @property
    def garage_heading(self):
        return self.page.get_by_role("heading", name="Garage")

    @property
    def add_car_button(self):
        return self.page.get_by_role("button", name="Add car")

    @allure.step("Verify Garage page is displayed")
    def verify_garage_page(self):
        assert self.garage_heading.is_visible()
        assert self.add_car_button.is_visible()
