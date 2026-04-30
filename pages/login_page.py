from pages.base_page import BasePage
from utils.config import BASE_URL

class LoginPage(BasePage):

    def open(self):
        self.page.goto(f"{BASE_URL}/login")

    def login(self, email, password):
        self.fill("#Email", email)
        self.fill("#Password", password)
        self.click("input[value='Log in']")