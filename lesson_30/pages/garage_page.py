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