from pages.base_page import BasePage

class CartPage(BasePage):

    def open_cart(self):
        self.click("text=Shopping cart")

    def get_title(self):
        return self.page.title()
    