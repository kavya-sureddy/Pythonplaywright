def test_cart(page):
    page.goto("https://demowebshop.tricentis.com/books")
    page.click("input[value='Add to cart']")
    page.wait_for_selector("text=Shopping cart")

    page.click("text=Shopping cart")

    assert "cart" in page.url.lower()