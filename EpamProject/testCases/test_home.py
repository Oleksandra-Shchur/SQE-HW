from pageObjects.HomePage import HomePage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
import os


class Test_001_Home:
    base_url = ReadConfig.get_application_url()
    logger = LogGen.loggen()
    current_dir = os.path.dirname(os.path.abspath(__file__))
    project_dir = os.path.dirname(current_dir)
    screenshots_dir = os.path.join(project_dir, 'Screenshots')

    def test_home_page_title(self, setup):
        self.logger.info("********** Test_001_Home **********")
        self.logger.info("********** Verifying Home Page Title **********")
        self.driver = setup
        self.driver.get(self.base_url)
        self.driver.maximize_window()
        self.hp = HomePage(self.driver)
        page_title = self.hp.get_title()
        if page_title == "EPAM | Software Engineering & Product Development Services":
            assert True
            self.driver.quit()
            self.logger.info("********** Home Page Title test case is passed **********")
        else:
            screenshot_file = os.path.join(self.screenshots_dir, 'test_home_page_title.png')
            self.driver.save_screenshot(screenshot_file)
            self.driver.quit()
            self.logger.error("********** Home Page Title test case is failed **********")
            assert False

    def test_theme_switch(self, setup):
        self.logger.info("********** Test_002_Theme_Switch **********")
        self.logger.info("********** Verifying Theme Switch **********")
        self.driver = setup
        self.driver.get(self.base_url)
        self.driver.maximize_window()
        self.hp = HomePage(self.driver)
        current_theme = self.hp.check_theme()
        self.hp.switch_theme()
        changed_theme = self.hp.check_theme()
        if current_theme != changed_theme:
            assert True
            self.driver.quit()
            self.logger.info("********** Theme Switch test case is passed **********")
        else:
            screenshot_file = os.path.join(self.screenshots_dir, 'test_theme_switch.png')
            self.driver.save_screenshot(screenshot_file)
            self.driver.quit()
            self.logger.error("********** Theme Switch test case is failed **********")
            assert False

    def test_language_switch(self, setup):
        self.logger.info("********** Test_003_Language_Switch **********")
        self.logger.info("********** Verifying Language Switch **********")
        self.driver = setup
        self.driver.get(self.base_url)
        self.driver.maximize_window()
        self.hp = HomePage(self.driver)
        self.hp.switch_language()
        if self.driver.current_url == "https://careers.epam.ua/":
            assert True
            self.driver.quit()
            self.logger.info("********** Language Switch test case is passed **********")
        else:
            screenshot_file = os.path.join(self.screenshots_dir, 'test_language_switch.png')
            self.driver.save_screenshot(screenshot_file)
            self.driver.quit()
            self.logger.error("********** Language Switch test case is failed **********")
            assert False

    def test_policies_list(self, setup):
        self.logger.info("********** Test_004_Policies_List **********")
        self.logger.info("********** Verifying Policies List **********")
        self.driver = setup
        self.driver.get(self.base_url)
        self.driver.maximize_window()
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        self.hp = HomePage(self.driver)
        policies_list_correct = self.hp.check_policies_list()
        if policies_list_correct:
            assert True
            self.driver.quit()
            self.logger.info("********** Policies List test case is passed **********")
        else:
            screenshot_file = os.path.join(self.screenshots_dir, 'test_policies_list.png')
            self.driver.save_screenshot(screenshot_file)
            self.driver.quit()
            self.logger.error("********** Policies List test case is failed **********")
            assert False

    def test_location_list(self, setup):
        self.logger.info("********** Test_005_1_Location_List **********")
        self.logger.info("********** Verifying Location List **********")
        self.driver = setup
        self.driver.get(self.base_url)
        self.hp = HomePage(self.driver)
        self.hp.check_location_list()
        location_list_correct = self.hp.check_location_list()
        if location_list_correct:
            assert True
            self.driver.quit()
            self.logger.info("********** Location List test case is passed **********")
        else:
            screenshot_file = os.path.join(self.screenshots_dir, 'test_location_list.png')
            self.driver.save_screenshot(screenshot_file)
            self.driver.quit()
            self.logger.error("********** Location List test case is failed **********")
            assert False

    def test_location_switch(self, setup):
        self.logger.info("********** Test_005_2_Location_Switch **********")
        self.logger.info("********** Verifying Location Switch **********")
        self.driver = setup
        self.driver.get(self.base_url)
        self.hp = HomePage(self.driver)
        location_switched_to_emea = self.hp.switch_location('EMEA')
        if location_switched_to_emea == "EMEA":
            assert True
            self.logger.info("********** Location Switch to EMEA test case is passed **********")
        else:
            screenshot_file = os.path.join(self.screenshots_dir, 'test_location_switch_to_emea.png')
            self.driver.save_screenshot(screenshot_file)
            self.driver.quit()
            self.logger.error("********** Location Switch to EMEA test case is failed **********")
            assert False
        location_switched_to_apac = self.hp.switch_location('APAC')
        if location_switched_to_apac == "APAC":
            assert True
            self.logger.info("********** Location Switch to APAC test case is passed **********")
        else:
            screenshot_file = os.path.join(self.screenshots_dir, 'test_location_switch_to_apac.png')
            self.driver.save_screenshot(screenshot_file)
            self.driver.quit()
            self.logger.error("********** Location Switch to APAC test case is failed **********")
            assert False
        location_switched_to_americas = self.hp.switch_location('AMERICAS')
        if location_switched_to_americas == "AMERICAS":
            assert True
            self.driver.quit()
            self.logger.info("********** Location Switch to AMERICAS test case is passed **********")
        else:
            screenshot_file = os.path.join(self.screenshots_dir, 'test_location_switch_to_americas.png')
            self.driver.save_screenshot(screenshot_file)
            self.driver.quit()
            self.logger.error("********** Location Switch to AMERICAS test case is failed **********")
            assert False

    def test_search_function(self, setup):
        self.logger.info("********** Test_006_Search_Function **********")
        self.logger.info("********** Verifying Search Function **********")
        self.driver = setup
        self.driver.get(self.base_url)
        self.driver.maximize_window()
        self.hp = HomePage(self.driver)
        self.hp.check_search("AI")
        if self.driver.current_url == "https://www.epam.com/search?q=AI":
            assert True
            self.driver.quit()
            self.logger.info("********** Search Function test case is passed **********")
        else:
            screenshot_file = os.path.join(self.screenshots_dir, 'test_search_function.png')
            self.driver.save_screenshot(screenshot_file)
            self.driver.quit()
            self.logger.error("********** Search Function test case is failed **********")
            assert False
