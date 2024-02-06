from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CartFunctionality:
    add_to_cart_btn_details_xpath = (By.XPATH, "//input[@id='add-to-cart-button-72']")
    shopping_cart_btn_xpath = (By.XPATH, "//span[normalize-space()='Shopping cart']")
    cart_item_locator = (By.XPATH, "//div[@class='page shopping-cart-page']")
    remove_checkbox_xpath = (By.XPATH, "//input[@name='removefromcart']")
    update_shopping_cart_btn_xpath = (By.XPATH, "//input[@name='updatecart']")
    checkbox_terms_of_service_xpath = (By.XPATH, "//input[@id='termsofservice']")
    checkout_btn_xpath = (By.XPATH, "//button[@id='checkout']")
    billing_address_continue_xpath = (By.XPATH, "//input[@onclick='Billing.save()']")
    shipping_address_continue_xpath = (By.XPATH, "//input[@onclick='Shipping.save()']")
    shipping_method_continue_xpath = (By.XPATH, "//input[@class='button-1 shipping-method-next-step-button']")
    payment_method_continue_xpath = (By.XPATH, "//input[@class='button-1 payment-method-next-step-button']")
    payment_information_continue_xpath = (By.XPATH, "//input[@class='button-1 payment-info-next-step-button']")
    confirm_order_btn_xpath = (By.XPATH, "//input[@value='Confirm']")
    add_to_wishlist_btn_details_css = (By.ID, "add-to-wishlist-button-5")

    def __init__(self, driver):
        self.driver = driver

    def add_item_to_cart(self, item_locator):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(item_locator)).click()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.add_to_cart_btn_details_xpath)).click()
        return True

    def remove_item_from_cart(self, item_locator):
        WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located(item_locator))
        self.driver.find_element(*self.remove_checkbox_xpath).click()
        self.driver.find_element(*self.update_shopping_cart_btn_xpath).click()
        return True

    def checkout(self):
        wait = WebDriverWait(self.driver, 50)
        wait.until(EC.element_to_be_clickable(self.checkbox_terms_of_service_xpath)).click()
        wait.until(EC.element_to_be_clickable(self.checkout_btn_xpath)).click()
        wait.until(EC.url_to_be("https://demowebshop.tricentis.com/onepagecheckout"))
        wait.until(EC.element_to_be_clickable(self.billing_address_continue_xpath)).click()
        wait.until(EC.element_to_be_clickable(self.shipping_address_continue_xpath)).click()
        wait.until(EC.element_to_be_clickable(self.shipping_method_continue_xpath)).click()
        wait.until(EC.element_to_be_clickable(self.payment_method_continue_xpath)).click()
        wait.until(EC.element_to_be_clickable(self.payment_information_continue_xpath)).click()
        wait.until(EC.element_to_be_clickable(self.confirm_order_btn_xpath)).click()
        wait.until(EC.url_to_be("https://demowebshop.tricentis.com/checkout/completed/"))
        return True

    def add_item_to_wishlist(self, item_locator, url_substring):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located(item_locator)).click()
        wait.until(EC.url_contains(url_substring))
        wait.until(EC.element_to_be_clickable(self.add_to_wishlist_btn_details_css)).click()
        return True
