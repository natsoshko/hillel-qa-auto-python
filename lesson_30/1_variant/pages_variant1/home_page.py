from playwright.sync_api import Page

class HomePage:
    def __init__(self, page: Page):
        self.page = page

    @property
    def sign_in_button(self):
        return self.page.get_by_role("button", name="Sign In")