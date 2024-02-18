from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from DemoWebShop.pageObjects.BasePage import BasePage
from selenium.common.exceptions import NoSuchElementException


class CartPage(BasePage):
    shopping_cart_btn_xpath = (By.XPATH, "//a[normalize-space()='shopping cart']")
    cart_item_locator = (By.XPATH, "//div[@class='page shopping-cart-page']")
    remove_checkbox_xpath = (By.XPATH, "//input[@name='removefromcart']")
    update_shopping_cart_btn_xpath = (By.XPATH, "//input[@name='updatecart']")
    shopping_cart_btn = (By.XPATH, "//li[@id='topcartlink']//a[@class='ico-cart']")

    def remove_item_from_cart(self):
        try:
            self.click(self.remove_checkbox_xpath)
            self.click(self.update_shopping_cart_btn_xpath)
            self.driver.find_element(*self.remove_checkbox_xpath)
            return False
        except NoSuchElementException:
            return True

    def go_to_cart(self):
        self.wait.until(EC.element_to_be_clickable(self.shopping_cart_btn_xpath))
        self.click(self.shopping_cart_btn_xpath)
