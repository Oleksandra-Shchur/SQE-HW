from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from DemoWebShop.pageObjects.BasePage import BasePage


class CheckoutPage(BasePage):
    checkbox_terms_of_service_xpath = (By.XPATH, "//input[@id='termsofservice']")
    checkout_btn_xpath = (By.XPATH, "//button[@id='checkout']")
    billing_address_continue_xpath = (By.XPATH, "//input[@onclick='Billing.save()']")
    shipping_address_continue_xpath = (By.XPATH, "//input[@onclick='Shipping.save()']")
    shipping_method_continue_xpath = (By.XPATH, "//input[@class='button-1 shipping-method-next-step-button']")
    payment_method_continue_xpath = (By.XPATH, "//input[@class='button-1 payment-method-next-step-button']")
    payment_information_continue_xpath = (By.XPATH, "//input[@class='button-1 payment-info-next-step-button']")
    confirm_order_btn_xpath = (By.XPATH, "//input[@value='Confirm']")

    def accept_terms_and_checkout(self):
        self.click(self.checkbox_terms_of_service_xpath)
        self.click(self.checkout_btn_xpath)
        return self.wait.until(EC.url_to_be("https://demowebshop.tricentis.com/onepagecheckout"))

    def continue_billing_address(self):
        self.click(self.billing_address_continue_xpath)

    def continue_shipping_address(self):
        self.click(self.shipping_address_continue_xpath)

    def select_shipping_method(self):
        self.click(self.shipping_method_continue_xpath)

    def select_payment_method(self):
        self.click(self.payment_method_continue_xpath)

    def continue_payment_information(self):
        self.click(self.payment_information_continue_xpath)

    def confirm_order(self):
        self.click(self.confirm_order_btn_xpath)
        return self.wait.until(EC.url_to_be("https://demowebshop.tricentis.com/checkout/completed/"))
