from pages.base_page import BasePage

class HomePage(BasePage):

    def search(self, product):
        self.fill("#small-searchterms", product)
        self.click("input[value='Search']")