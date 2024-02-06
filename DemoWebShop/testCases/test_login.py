from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
import os
from selenium.webdriver.support.events import EventFiringWebDriver
from utilities.DriverListener import DriverListener


class Test_002_Login:
    base_url = ReadConfig.get_application_url()
    user_email = ReadConfig.get_user_email()
    password = ReadConfig.get_password()
    logger = LogGen.loggen()
    current_dir = os.path.dirname(os.path.abspath(__file__))
    project_dir = os.path.dirname(current_dir)
    screenshots_dir = os.path.join(project_dir, 'Screenshots')

    def test_user_login(self, setup):
        self.logger.info("*************** Test_002_Login *****************")
        self.logger.info("****Started User Login test ****")
        self.driver = setup
        e_driver = EventFiringWebDriver(self.driver, DriverListener(self.driver, self.logger, self.screenshots_dir))
        self.logger.info("****Opening URL****")
        e_driver.get(self.base_url + "login")
        login_page = LoginPage(e_driver)
        login_page.set_email(self.user_email)
        login_page.set_password(self.password)
        login_page.click_login()
        is_logged_user = login_page.check_logged_user(self.user_email)
        if is_logged_user:
            self.logger.info("**** User Login test passed ****")
            assert True
        else:
            self.logger.error("**** User Login test failed****")
            assert False
        e_driver.quit()
