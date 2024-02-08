from pageObjects.RegistrationsPage import RegistrationsPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
import os
import string
import random
from selenium.webdriver.support.events import EventFiringWebDriver
from utilities.DriverListener import DriverListener


class Test_001_Registrations:
    base_url = ReadConfig.get_application_url()
    logger = LogGen.loggen()
    current_dir = os.path.dirname(os.path.abspath(__file__))
    project_dir = os.path.dirname(current_dir)
    screenshots_dir = os.path.join(project_dir, 'Screenshots')

    # this test looks more like test, finally :)
    # we have steps (enter, confirm)
    # and separate checking of registered user
    def test_user_registration(self, setup):
        self.logger.info("*************** Test_001_Registration *****************")
        self.logger.info("**** Registration test started ****")
        self.driver = setup
        e_driver = EventFiringWebDriver(self.driver, DriverListener(self.driver, self.logger, self.screenshots_dir))
        self.logger.info("****Opening URL****")
        e_driver.get(self.base_url + "register")
        registration_page = RegistrationsPage(e_driver)

        # what purpose in self here?
        self.email = random_generator() + "@gmail.com"
        registration_page.set_gender('mail')
        registration_page.set_first_name('Test')
        registration_page.set_last_name('User')
        registration_page.set_email(self.email)
        registration_page.set_password('testpass123')
        registration_page.set_confirm_password('testpass123')
        registration_page.click_register()
        is_registered_user = registration_page.check_registered_user(self.email)
        if is_registered_user:
            self.logger.info("********** User Registration test case is passed **********")
            assert True
        else:
            self.logger.error("********** User Registration test case is failed **********")
            assert False

        e_driver.quit()


def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))
