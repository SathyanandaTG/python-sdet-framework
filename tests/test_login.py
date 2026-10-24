import pytest
from playwright.sync_api import expect
from pages.login_page import LoginPage

@pytest.mark.parametrize(
    "username, password, expected_result",
    [
        ("standard_user", "secret_sauce", "success"),
        ("standard_user", "wrong_password", "failure"),
        ("wrong_user", "secret_sauce", "failure"),
        ("", "", "failure"),
    ],
)
def test_login(page, saucedemo_url, username, password, expected_result):
    login_page = LoginPage(page)
    login_page.open(saucedemo_url)
    login_page.login(username, password)

    if expected_result == "success":
        expect(page.locator(".title")).to_be_visible()
        assert page.locator(".title").inner_text() == "Products"
        assert page.url.endswith("/inventory.html")
    else:
        assert page.get_by_text(
            "Epic sadface"
        ).is_visible()