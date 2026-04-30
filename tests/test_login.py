import json
from pages.login_page import LoginPage

def test_login(page):
    login = LoginPage(page)
    login.open()
    login.login("sk@user.com", "user@123")

    page.wait_for_selector("text=Log out")

    assert "logout" in page.content().lower()