import os
# which should be settings of the project for this kind of import? Have you switched root dir for each task?
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

    # could we move Screenshots directory init to driver extension where this screenshots will be done?
    current_dir = os.path.dirname(os.path.abspath(__file__))
    project_dir = os.path.dirname(current_dir)
    screenshots_dir = os.path.join(project_dir, 'Screenshots')

    # locator in test it's really bad practice, try to move it to page
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

        # there is no need in the following line. Driver should be accessible immediatelly by self.driver
        self.driver = setup
        # also it will be better to return in test final version of driver with all extensions
        e_driver = EventFiringWebDriver(self.driver, DriverListener(self.driver, self.logger, self.screenshots_dir))
        e_driver.get(self.base_url + "login")
        e_driver.maximize_window()
        login_page = LoginPage(e_driver)
        login_page.set_email(self.user_email)
        login_page.set_password(self.password)
        login_page.click_login()
        # All opening, browser, maximize it, and login should be moved from test to preconditions.
        self.logger.info("************* Login succesfully **********")
        self.logger.info("******* Starting Add Item Test **********")
        e_driver.get(self.base_url + "desktops")
        cart = CartFunctionality(e_driver)

        # basically this one line is our test
        # where we do just two clicks without any asserting that something was added or changed
        # not looks like real test
        is_item_added = cart.add_item_to_cart(self.item_desktops.shop_locator)

        # Excessive verification just for logging purpose, can be removed at all
        if is_item_added:
            self.logger.info("**** Add item to cart test passed ****")
            assert True
        else:
            self.logger.error("**** Add item to cart test failed ****")
            assert False

        # Closing driver already exist in postcondition
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

        # why directly changing url instead of clicking appropriate button?
        # I have doubts then people will go to cart by url
        e_driver.get(self.base_url + "cart")
        # also test without any verification that removing from cart is really working
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

        # magic method which looks like "verify everything is fine" and in test we don't see what we really should check
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

        # what will be if exactly this product will be deleted?
        # I suppose we need more ajustable test like click at first product, or randomly choosen product
        is_item_added = cart.add_item_to_wishlist(self.item_apparel_shoes.shop_locator,
                                                  "50s-rockabilly-polka-dot-top-jr-plus-size")

        if is_item_added:
            self.logger.info("**** Add item to wishlist test passed ****")
            assert True
        else:
            self.logger.error("**** Add item to wishlist test failed ****")
            assert False

        e_driver.quit()
