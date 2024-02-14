from pageObjects.HomePage import HomePage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_001_Home:
    base_url = ReadConfig.get_application_url()
    logger = LogGen.loggen()

    def test_home_page_title(self, setup):
        self.logger.info("********** Test_001_Home **********")
        self.logger.info("********** Verifying Home Page Title **********")
        e_driver = setup
        e_driver.get(self.base_url)
        hp = HomePage(e_driver)
        page_title = hp.get_title()
        assert page_title == "EPAM | Software Engineering & Product Development Services", \
            "********** Home Page Title test case is failed **********"
        self.logger.info("********** Home Page Title test case is passed **********")

    def test_theme_switch(self, setup):
        self.logger.info("********** Test_002_Theme_Switch **********")
        self.logger.info("********** Verifying Theme Switch **********")
        e_driver = setup
        e_driver.get(self.base_url)
        hp = HomePage(e_driver)
        current_theme = hp.check_theme()
        hp.switch_theme()
        changed_theme = hp.check_theme()
        assert current_theme != changed_theme, \
            "********** Theme Switch test case is failed **********"
        self.logger.info("********** Theme Switch test case is passed **********")

    def test_language_switch(self, setup):
        self.logger.info("********** Test_003_Language_Switch **********")
        self.logger.info("********** Verifying Language Switch **********")
        e_driver = setup
        e_driver.get(self.base_url)
        hp = HomePage(e_driver)
        hp.switch_language()
        assert e_driver.current_url == "https://careers.epam.ua/", \
            "********** Language Switch test case is failed **********"
        self.logger.info("********** Language Switch test case is passed **********")

    def test_policies_list(self, setup):
        self.logger.info("********** Test_004_Policies_List **********")
        self.logger.info("********** Verifying Policies List **********")
        e_driver = setup
        e_driver.get(self.base_url)
        e_driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        hp = HomePage(e_driver)
        policies_list_correct = hp.check_policies_list()
        assert policies_list_correct, \
            "********** Policies List test case is failed **********"
        self.logger.info("********** Policies List test case is passed **********")

    def test_location_list(self, setup):
        self.logger.info("********** Test_005_1_Location_List **********")
        self.logger.info("********** Verifying Location List **********")
        e_driver = setup
        e_driver.get(self.base_url)
        hp = HomePage(e_driver)
        location_list_correct = hp.check_location_list()
        assert location_list_correct, \
            "********** Location List test case is failed **********"
        self.logger.info("********** Location List test case is passed **********")

    def test_location_switch(self, setup):
        self.logger.info("********** Test_005_2_Location_Switch **********")
        self.logger.info("********** Verifying Location Switch **********")
        e_driver = setup
        e_driver.get(self.base_url)
        hp = HomePage(e_driver)

        location_switched_to_emea = hp.switch_location('EMEA')
        assert location_switched_to_emea == "EMEA", \
            "********** Location Switch to EMEA test case is failed **********"
        self.logger.info("********** Location Switch to EMEA test case is passed **********")

        location_switched_to_apac = hp.switch_location('APAC')
        assert location_switched_to_apac == "APAC", \
            "********** Location Switch to APAC test case is failed **********"
        self.logger.info("********** Location Switch to APAC test case is passed **********")

        location_switched_to_americas = hp.switch_location('AMERICAS')
        assert location_switched_to_americas == "AMERICAS", \
            "********** Location Switch to AMERICAS test case is failed **********"
        self.logger.info("********** Location Switch to AMERICAS test case is passed **********")

    def test_search_function(self, setup):
        self.logger.info("********** Test_006_Search_Function **********")
        self.logger.info("********** Verifying Search Function **********")
        e_driver = setup
        e_driver.get(self.base_url)
        hp = HomePage(e_driver)
        hp.check_search("AI")
        assert e_driver.current_url == "https://www.epam.com/search?q=AI", \
            "********** Search Function test case is failed **********"
        self.logger.info("********** Search Function test case is passed **********")
