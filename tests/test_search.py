from pages.home_page import HomePage

def test_search(page):
    page.goto("https://demowebshop.tricentis.com")
    home = HomePage(page)
    home.search("book")

    assert "search" in page.url.lower()