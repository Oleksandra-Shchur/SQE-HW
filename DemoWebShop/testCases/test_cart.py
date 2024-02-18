from DemoWebShop.pageObjects.CartPage import CartPage
from DemoWebShop.pageObjects.CheckoutPage import CheckoutPage
from DemoWebShop.pageObjects.ProductPage import ProductPage

from DemoWebShop.pageObjects.LoginPage import LoginPage
from DemoWebShop.utilities.readProperties import ReadConfig
from DemoWebShop.utilities.customLogger import LogGen


class TestCartFunctinality:
    base_url = ReadConfig.get_application_url()
    user_email = ReadConfig.get_user_email()
    password = ReadConfig.get_password()
    logger = LogGen.loggen()

    def test_add_item_to_cart(self, setup):
        self.logger.info("*************** Test_001_AddItemToCart *****************")
        e_driver = setup
        e_driver.get(self.base_url + "login")
        login_page = LoginPage(e_driver)
        login_page.set_email(self.user_email)
        login_page.set_password(self.password)
        login_page.click_login()
        self.logger.info("************* Login successfully **********")
        self.logger.info("******* Starting Add Item to Cart Test **********")
        e_driver.get(self.base_url + "desktops")
        product = ProductPage(e_driver)
        product.click_first_product()
        is_item_added = product.add_item_to_cart()
        assert is_item_added, "**** Add item to Cart test failed ****"
        self.logger.info("**** Add item to Cart test passed ****")

    def test_remove_item_from_cart(self, setup):
        self.logger.info("*************** Test_002_RemoveItemFromCart *****************")
        e_driver = setup
        e_driver.get(self.base_url + "login")
        login_page = LoginPage(e_driver)
        login_page.set_email(self.user_email)
        login_page.set_password(self.password)
        login_page.click_login()
        self.logger.info("************* Login successfully **********")
        self.logger.info("******* Starting Remove Item Test **********")
        e_driver.get(self.base_url + "desktops")
        cart = CartPage(e_driver)
        product = ProductPage(e_driver)
        product.click_first_product()
        product.add_item_to_cart()
        cart.go_to_cart()
        is_item_removed = cart.remove_item_from_cart()
        assert is_item_removed, "**** Remove item from cart test failed ****"
        self.logger.info("**** Remove item from cart test passed ****")

    def test_checkout(self, setup):
        self.logger.info("*************** Test_003_Checkout *****************")
        e_driver = setup
        e_driver.get(self.base_url + "login")
        login_page = LoginPage(e_driver)
        login_page.set_email(self.user_email)
        login_page.set_password(self.password)
        login_page.click_login()
        self.logger.info("************* Login successfully **********")
        self.logger.info("****Starting Checkout Test ****")
        e_driver.get(self.base_url + "desktops")
        product = ProductPage(e_driver)
        product.click_first_product()
        product.add_item_to_cart()
        cart = CartPage(e_driver)
        cart.go_to_cart()
        cp = CheckoutPage(e_driver)
        cp.accept_terms_and_checkout()
        cp.continue_billing_address()
        cp.continue_shipping_address()
        cp.select_shipping_method()
        cp.select_payment_method()
        cp.continue_payment_information()
        assert cp.confirm_order(), "Order confirmation failed"
        self.logger.info("**** Checkout test passed ****")

    def test_add_item_to_wishlist(self, setup):
        self.logger.info("*************** Test_001_AddItemToWishlist *****************")
        e_driver = setup
        e_driver.get(self.base_url + "login")
        login_page = LoginPage(e_driver)
        login_page.set_email(self.user_email)
        login_page.set_password(self.password)
        login_page.click_login()
        self.logger.info("************* Login successfully **********")
        self.logger.info("******* Starting Add Item to Wishlist Test **********")
        e_driver.get(self.base_url + "apparel-shoes")
        product = ProductPage(e_driver)
        product.click_first_product()
        is_item_added = product.add_item_to_wishlist()
        assert is_item_added, "**** Add item to wishlist test failed ****"
        self.logger.info("**** Add item to wishlist test passed ****")
