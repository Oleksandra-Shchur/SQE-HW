from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import text_to_be_present_in_element
from selenium.webdriver.support import expected_conditions as EC
from DemoWebShop.pageObjects.BasePage import BasePage
from selenium.common.exceptions import NoSuchElementException


class ProductPage(BasePage):
    add_to_cart_btn_details_xpath = (By.XPATH, "//input[@id='add-to-cart-button-72']")
    add_to_wishlist_btn_details_css = (By.ID, "add-to-wishlist-button-5")
    products = (By.XPATH, '//div[@class="item-box"]')
    success_message_locator = (By.CLASS_NAME, 'content')

    def click_first_product(self):
        product_elements = self.wait.until(EC.presence_of_all_elements_located(self.products))
        if not product_elements:
            raise NoSuchElementException("No products found on page")
        first_product = product_elements[0]
        first_product.click()
        return first_product

    def add_item_to_cart(self):
        self.click(self.add_to_cart_btn_details_xpath)
        is_success_message_showing = self.wait.until(
            text_to_be_present_in_element(
                self.success_message_locator,
                'The product has been added to your'))
        return is_success_message_showing

    def add_item_to_wishlist(self):
        self.click(self.add_to_wishlist_btn_details_css)
        is_success_message_showing = self.wait.until(
            text_to_be_present_in_element(
                self.success_message_locator,
                'The product has been added to your'))
        return is_success_message_showing
