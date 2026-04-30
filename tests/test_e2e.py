from pages.login_page import LoginPage

def test_e2e(page):
    login = LoginPage(page)
    login.open()
    login.login("valid@gmail.com", "Valid@123")

    page.goto("https://demowebshop.tricentis.com/books")
    page.click("input[value='Add to cart']")
    page.click("text=Shopping cart")

    assert "cart" in page.url.lower()