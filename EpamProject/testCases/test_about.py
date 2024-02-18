from EpamProject.pageObjects.AboutPage import AboutPage
from EpamProject.utilities.readProperties import ReadConfig
from EpamProject.utilities.customLogger import LogGen


class Test_001_About:
    base_url = ReadConfig.get_application_url()
    logger = LogGen.loggen()

    def test_form_validation(self, setup):
        self.logger.info("********** Test_007_Form_Validation **********")
        self.logger.info("********** Verifying Form Validation **********")
        e_driver = setup
        e_driver.get(self.base_url + '/about/who-we-are/contact')
        ap = AboutPage(e_driver)
        form_validated = ap.check_form_validation()
        assert form_validated, "********** Form Validation test case is failed **********"
        self.logger.info("********** Form Validation test case is passed **********")

    def test_logo_link(self, setup):
        self.logger.info("********** Test_008_Logo_Link **********")
        self.logger.info("********** Verifying Logo Link **********")
        e_driver = setup
        e_driver.get(self.base_url + '/about')
        ap = AboutPage(e_driver)
        ap.check_logo_link()
        assert e_driver.current_url == "https://www.epam.com/", "********** Logo Link test case is failed **********"
        self.logger.info("********** Logo Link test case is passed **********")

    def test_report_download(self, setup):
        self.logger.info("********** Test_009_Report_Download **********")
        self.logger.info("********** Verifying Report Download **********")
        e_driver = setup
        e_driver.get(self.base_url + '/about')
        ap = AboutPage(e_driver)
        report_downloaded = ap.check_report_download()
        assert report_downloaded, "********** Report Download test case is failed **********"
        self.logger.info("********** Report Download test case is passed **********")
