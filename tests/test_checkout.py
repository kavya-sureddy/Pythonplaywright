from pages.login_page import LoginPage
from pages.checkout_page import CheckoutPage


def test_checkout(page):
    login = LoginPage(page)
    checkout = CheckoutPage(page)

    # login
    login.open()
    login.login("sk@user.com", "user@123")
    page.wait_for_load_state("networkidle")

    # add product to cart
    page.goto("https://demowebshop.tricentis.com/books")
    page.click("input[value='Add to cart']")
    page.wait_for_selector("span.cart-qty")

    # go to cart
    checkout.open_cart()

    # accept terms + checkout
    checkout.accept_terms()
    checkout.click_checkout()

    # billing
    checkout.fill_billing_details()

    # shipping address
    checkout.fill_shipping_address()

    # shipping method (auto-selects first option)
    checkout.shipping_method()

    # payment
    checkout.payment_method()
    checkout.payment_info()
    checkout.confirm_order()

    # final assertion
    assert page.locator("text=Your order has been successfully processed").is_visible()

    # logout
