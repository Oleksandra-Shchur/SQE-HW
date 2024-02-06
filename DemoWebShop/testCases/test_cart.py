import os
from pageObjects.CartFunctionality import CartFunctionality
from pageObjects.Item import Item
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from selenium.webdriver.common.by import By
from selenium.webdriver.support.events import EventFiringWebDriver
from utilities.DriverListener import DriverListener


class TestCartFunctionality:
    base_url = ReadConfig.get_application_url()
    user_email = ReadConfig.get_user_email()
    password = ReadConfig.get_password()
    logger = LogGen.loggen()
    current_dir = os.path.dirname(os.path.abspath(__file__))
    project_dir = os.path.dirname(current_dir)
    screenshots_dir = os.path.join(project_dir, 'Screenshots')
    item_desktops = Item(
        name='Build your own cheap computer',
        shop_locator=(By.CSS_SELECTOR, ".item-box:nth-child(1) img"),
        cart_locator=(By.XPATH,
                      "//a[@class='product-name'][normalize-space()='Build your own cheap computer']"))
    item_apparel_shoes = Item(
        name="50's Rockabilly Polka Dot Top JR Plus Size",
        shop_locator=(By.CSS_SELECTOR, ".item-box:nth-child(1) .button-2"),
        cart_locator=(By.CSS_SELECTOR, ".cart-item-row:nth-child(2) > .product"))

    def test_add_item_to_cart(self, setup):
        self.logger.info("*************** Test_001_AddItemToCart *****************")
        self.driver = setup
        e_driver = EventFiringWebDriver(self.driver, DriverListener(self.driver, self.logger, self.screenshots_dir))
        e_driver.get(self.base_url + "login")
        e_driver.maximize_window()
        login_page = LoginPage(e_driver)
        login_page.set_email(self.user_email)
        login_page.set_password(self.password)
        login_page.click_login()
        self.logger.info("************* Login succesfully **********")
        self.logger.info("******* Starting Add Item Test **********")
        e_driver.get(self.base_url + "desktops")
        cart = CartFunctionality(e_driver)
        is_item_added = cart.add_item_to_cart(self.item_desktops.shop_locator)
        if is_item_added:
            self.logger.info("**** Add item to cart test passed ****")
            assert True
        else:
            self.logger.error("**** Add item to cart test failed ****")
            assert False
        e_driver.quit()

    def test_remove_item_from_cart(self, setup):
        self.logger.info("*************** Test_002_RemoveItemFromCart *****************")
        self.driver = setup
        e_driver = EventFiringWebDriver(self.driver, DriverListener(self.driver, self.logger, self.screenshots_dir))
        e_driver.get(self.base_url + "login")
        e_driver.maximize_window()
        login_page = LoginPage(e_driver)
        login_page.set_email(self.user_email)
        login_page.set_password(self.password)
        login_page.click_login()
        self.logger.info("************* Login successfully **********")
        self.logger.info("******* Starting Remove Item Test **********")
        e_driver.get(self.base_url + "desktops")
        cart = CartFunctionality(e_driver)
        cart.add_item_to_cart(self.item_desktops.shop_locator)
        e_driver.get(self.base_url + "cart")
        if cart.remove_item_from_cart(self.item_desktops.cart_locator):
            self.logger.info("**** Remove item from cart test passed ****")
            assert True
        else:
            self.logger.error("**** Remove item from cart test failed ****")
            assert False
        e_driver.quit()

    def test_checkout(self, setup):
        self.logger.info("*************** Test_003_Checkout *****************")
        self.driver = setup
        e_driver = EventFiringWebDriver(self.driver, DriverListener(self.driver, self.logger, self.screenshots_dir))
        e_driver.get(self.base_url + "login")
        e_driver.maximize_window()
        login_page = LoginPage(e_driver)
        login_page.set_email(self.user_email)
        login_page.set_password(self.password)
        login_page.click_login()
        self.logger.info("************* Login successfully **********")
        self.logger.info("****Starting Checkout Test ****")
        e_driver.get(self.base_url + "desktops")
        cart = CartFunctionality(e_driver)
        cart.add_item_to_cart(self.item_desktops.shop_locator)
        e_driver.get(self.base_url + "cart")
        if cart.checkout:
            self.logger.info("**** Checkout test passed ****")
            assert True
        else:
            self.logger.error("**** Checkout test failed ****")
            assert False
        e_driver.quit()

    def test_add_item_to_wishlist(self, setup):
        self.logger.info("*************** Test_001_AddItemToWishlist *****************")
        self.driver = setup
        e_driver = EventFiringWebDriver(self.driver, DriverListener(self.driver, self.logger, self.screenshots_dir))

        e_driver.get(self.base_url + "login")
        e_driver.maximize_window()

        login_page = LoginPage(e_driver)
        login_page.set_email(self.user_email)
        login_page.set_password(self.password)
        login_page.click_login()

        self.logger.info("************* Login successfully **********")
        self.logger.info("******* Starting Add Item to Wishlist Test **********")

        e_driver.get(self.base_url + "apparel-shoes")
        cart = CartFunctionality(e_driver)
        is_item_added = cart.add_item_to_wishlist(self.item_apparel_shoes.shop_locator,
                                                  "50s-rockabilly-polka-dot-top-jr-plus-size")

        if is_item_added:
            self.logger.info("**** Add item to wishlist test passed ****")
            assert True
        else:
            self.logger.error("**** Add item to wishlist test failed ****")
            assert False

        e_driver.quit()
