import string
import random
from DemoWebShop.pageObjects.RegistrationsPage import RegistrationsPage
from DemoWebShop.utilities.readProperties import ReadConfig
from DemoWebShop.utilities.customLogger import LogGen


class Test_001_Registrations:
    base_url = ReadConfig.get_application_url()
    logger = LogGen.loggen()

    def test_user_registration(self, setup):
        self.logger.info("*************** Test_001_Registration *****************")
        self.logger.info("**** Registration test started ****")
        e_driver = setup
        self.logger.info("****Opening URL****")
        e_driver.get(self.base_url + "register")
        registration_page = RegistrationsPage(e_driver)
        email = random_generator() + "@gmail.com"
        registration_page.set_gender('mail')
        registration_page.set_first_name('Test')
        registration_page.set_last_name('User')
        registration_page.set_email(email)
        registration_page.set_password('testpass123')
        registration_page.set_confirm_password('testpass123')
        registration_page.click_register()
        is_registered_user = registration_page.check_registered_user(email)
        assert is_registered_user, "********** User Registration test case is failed **********"
        self.logger.info("********** User Registration test case is passed **********")


def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))
