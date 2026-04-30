class CheckoutPage:

    def __init__(self, page):
        self.page = page

    def open_cart(self):
        self.page.locator("a.ico-cart").first.click()

    def accept_terms(self):
        self.page.check("#termsofservice")

    def click_checkout(self):
        self.page.click("#checkout")
        self.page.wait_for_url("**/onepagecheckout")

    def fill_billing_details(self):
        self.page.wait_for_selector("#billing-buttons-container")

        # Fill only if fields visible (new user case)
        if self.page.locator("#BillingNewAddress_CountryId").is_visible():
            self.page.select_option("#BillingNewAddress_CountryId", "41")
            self.page.fill("#BillingNewAddress_City", "Hyderabad")
            self.page.fill("#BillingNewAddress_Address1", "Test Address")
            self.page.fill("#BillingNewAddress_ZipPostalCode", "500001")
            self.page.fill("#BillingNewAddress_PhoneNumber", "9999999999")

        # Click correct Continue
        self.page.locator("#billing-buttons-container input[value='Continue']").click()

        # wait till next section opens
        self.page.wait_for_selector("#shipping-method-buttons-container")

    def shipping_method(self):
        self.page.locator("#shipping-method-buttons-container input[value='Continue']").click()
        self.page.wait_for_selector("#payment-method-buttons-container")

    def payment_method(self):
        self.page.locator("#payment-method-buttons-container input[value='Continue']").click()
        self.page.wait_for_selector("#payment-info-buttons-container")

    def payment_info(self):
        self.page.locator("#payment-info-buttons-container input[value='Continue']").click()
        self.page.wait_for_selector("#confirm-order-buttons-container")

    def confirm_order(self):
        self.page.locator("#confirm-order-buttons-container input[value='Confirm']").click()
        self.page.wait_for_selector("text=Your order has been successfully processed")