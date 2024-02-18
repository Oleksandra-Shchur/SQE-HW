from DemoWebShop.pageObjects.LoginPage import LoginPage
from DemoWebShop.utilities.readProperties import ReadConfig
from DemoWebShop.utilities.customLogger import LogGen


class Test_002_Login:
    base_url = ReadConfig.get_application_url()
    user_email = ReadConfig.get_user_email()
    password = ReadConfig.get_password()
    logger = LogGen.loggen()

    def test_user_login(self, setup):
        self.logger.info("*************** Test_002_Login *****************")
        self.logger.info("****Started User Login test ****")
        e_driver = setup
        self.logger.info("****Opening URL****")
        e_driver.get(self.base_url + "login")
        login_page = LoginPage(e_driver)
        login_page.set_email(self.user_email)
        login_page.set_password(self.password)
        login_page.click_login()
        is_logged_user = login_page.check_logged_user(self.user_email)
        assert is_logged_user, "**** User Login test failed ****"
        self.logger.info("**** User Login test passed ****")
