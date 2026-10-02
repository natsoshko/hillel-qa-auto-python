import pytest
from playwright.sync_api import Browser, Playwright


@pytest.fixture
def browser(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    yield browser
    browser.close()


@pytest.fixture
def page(browser: Browser):
    context = browser.new_context(
        http_credentials={
            "username": "guest",
            "password": "welcome2qauto"
        }
    )

    page = context.new_page()
    page.goto("https://qauto2.forstudy.space/")

    yield page

    context.close()