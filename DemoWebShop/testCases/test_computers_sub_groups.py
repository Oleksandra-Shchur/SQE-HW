from pageObjects.ComputersGroup import ComputersGroup
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
import os
from selenium.webdriver.support.events import EventFiringWebDriver
from utilities.DriverListener import DriverListener


class Test_003_ComputersGroup:
    base_url = ReadConfig.get_application_url()
    logger = LogGen.loggen()
    current_dir = os.path.dirname(os.path.abspath(__file__))
    project_dir = os.path.dirname(current_dir)
    screenshots_dir = os.path.join(project_dir, 'Screenshots')

    def test_computers_sub_groups(self, setup):
        self.logger.info("*************** Test_001_ComputersGroup *****************")
        self.logger.info("****Started Computers Sub-Groups test ****")
        self.driver = setup
        e_driver = EventFiringWebDriver(self.driver, DriverListener(self.driver, self.logger, self.screenshots_dir))
        self.logger.info("****Opening URL****")
        e_driver.get(self.base_url)
        computers_group = ComputersGroup(e_driver)
        if computers_group.verify_computers_sub_groups():
            self.logger.info("**** Computers Sub-Groups test passed ****")
            assert True
        else:
            self.logger.error("**** Computers Sub-Groups test failed****")
            assert False
        e_driver.quit()

    def test_sorting(self, setup):
        self.logger.info("*************** Test_002_Sorting *****************")
        self.logger.info("****Started Sorting test ****")
        self.driver = setup
        e_driver = EventFiringWebDriver(self.driver, DriverListener(self.driver, self.logger, self.screenshots_dir))
        self.logger.info("****Opening URL****")
        e_driver.get(self.base_url + "desktops")
        computers_group = ComputersGroup(e_driver)
        sorting_option_text = "Created on"

        # here we check only sorting label was changed, but what about has products order changed?
        if computers_group.select_sort_option(sorting_option_text):
            self.logger.info("**** Sorting test passed ****")
            assert True
        else:
            self.logger.error("**** Sorting test failed****")
            assert False
        e_driver.quit()

    def test_items_per_page(self, setup):
        self.logger.info("*************** Test_003_ItemsPerPage *****************")
        self.logger.info("**** Started Items Per Page Test ****")
        self.driver = setup
        e_driver = EventFiringWebDriver(self.driver, DriverListener(self.driver, self.logger, self.screenshots_dir))
        self.logger.info("**** Opening URL ****")
        e_driver.get(self.base_url + "desktops")
        computers_group = ComputersGroup(e_driver)
        items_per_page_value = "12"

        # as in previous we check only labels, what about real number of items per page
        is_correct_number_displayed = computers_group.select_items_per_page(items_per_page_value)
        if is_correct_number_displayed:
            self.logger.info("**** Items Per Page Test Passed ****")
            assert True
        else:
            self.logger.error("**** Items Per Page Test Failed ****")
            assert False
        e_driver.quit()
