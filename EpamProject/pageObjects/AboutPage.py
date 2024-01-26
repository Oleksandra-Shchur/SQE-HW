from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import time


class AboutPage:
    download_button_xpath = "//span[@class='button__content button__content--desktop'][normalize-space()='DOWNLOAD']"
    required_fields_xpath = "//*[@data-required='true']"
    submit_button_xpath = "//button[normalize-space()='Submit']"
    validation_message_xpath = "//*[@data-required-msg='This is a required field']"
    logo_link_xpath = "//a[@class='header__logo-container desktop-logo']"

    def __init__(self, driver):
        self.driver = driver

    def check_form_validation(self):
        required_fields = self.driver.find_elements(By.XPATH, self.required_fields_xpath)
        submit_button = self.driver.find_element(By.XPATH, self.submit_button_xpath)
        submit_button.click()
        WebDriverWait(self.driver, 20).until(EC.visibility_of_any_elements_located((By.XPATH,
                                                                                    self.validation_message_xpath)))
        for field in required_fields:
            validation_message = field.find_element(By.XPATH, self.validation_message_xpath)
            if not validation_message.is_displayed():
                return False
        return True

    def check_logo_link(self):
        logo_link = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, self.logo_link_xpath)))
        self.driver.execute_script("arguments[0].click();", logo_link)
        wait = WebDriverWait(self.driver, 20)
        wait.until(EC.url_to_be("https://www.epam.com/"))

    def check_report_download(self):
        download_link = WebDriverWait(self.driver, 40).until(
            EC.element_to_be_clickable((By.XPATH, self.download_button_xpath)))
        download_link.click()
        download_dir = '/Users/oleksandra/Downloads'
        filename = 'EPAM_Corporate_Overview_Q3_october.pdf'
        while not os.path.exists(os.path.join(download_dir, filename)):
            time.sleep(1)
        if filename == 'EPAM_Corporate_Overview_Q3_october.pdf':
            return True
        else:
            return False
