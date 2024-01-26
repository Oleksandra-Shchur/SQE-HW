from pageObjects.AboutPage import AboutPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
import os


class Test_001_About:
    base_url = ReadConfig.get_application_url()
    logger = LogGen.loggen()
    current_dir = os.path.dirname(os.path.abspath(__file__))
    project_dir = os.path.dirname(current_dir)
    screenshots_dir = os.path.join(project_dir, 'Screenshots')

    def test_form_validation(self, setup):
        self.logger.info("********** Test_007_Form_Validation **********")
        self.logger.info("********** Verifying Form Validation **********")
        self.driver = setup
        self.driver.get(self.base_url + '/about/who-we-are/contact')
        self.driver.maximize_window()
        self.ap = AboutPage(self.driver)
        form_validated = self.ap.check_form_validation()
        if form_validated:
            assert True
            self.driver.quit()
            self.logger.info("********** Form Validation test case is passed **********")
        else:
            screenshot_file = os.path.join(self.screenshots_dir, 'test_form_validation.png')
            self.driver.save_screenshot(screenshot_file)
            self.driver.quit()
            self.logger.error("********** Form Validation test case is failed **********")
            assert False

    def test_logo_link(self, setup):
        self.logger.info("********** Test_008_Logo_Link **********")
        self.logger.info("********** Verifying Logo Link **********")
        self.driver = setup
        self.driver.get(self.base_url + '/about')
        self.ap = AboutPage(self.driver)
        self.driver.maximize_window()
        self.ap.check_logo_link()
        if self.driver.current_url == "https://www.epam.com/":
            assert True
            self.driver.quit()
            self.logger.info("********** Logo Link test case is passed **********")
        else:
            screenshot_file = os.path.join(self.screenshots_dir, 'test_logo_link.png')
            self.driver.save_screenshot(screenshot_file)
            self.driver.quit()
            self.logger.error("********** Logo Link test case is failed **********")
            assert False

    def test_report_download(self, setup):
        self.logger.info("********** Test_009_Report_Download **********")
        self.logger.info("********** Verifying Report Download **********")
        self.driver = setup
        self.driver.get(self.base_url + '/about')
        self.driver.maximize_window()
        self.ap = AboutPage(self.driver)
        report_downloaded = self.ap.check_report_download()
        if report_downloaded:
            assert True
            self.driver.quit()
            self.logger.info("********** Report Download test case is passed **********")
        else:
            screenshot_file = os.path.join(self.screenshots_dir, 'test_report_download.png')
            self.driver.save_screenshot(screenshot_file)
            self.driver.quit()
            self.logger.error("********** Report Download test case is failed **********")
            assert False
