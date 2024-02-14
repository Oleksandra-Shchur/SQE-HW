from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import time


class AboutPage:
    download_button = (By.XPATH,
                       "//span[@class='button__content button__content--desktop'][normalize-space()='DOWNLOAD']")
    required_fields = (By.XPATH, "//*[@data-required='true']")
    submit_button = (By.XPATH, "//button[normalize-space()='Submit']")
    validation_message = (By.XPATH, "//*[@data-required-msg='This is a required field']")
    logo_link = (By.XPATH, "//a[@class='header__logo-container desktop-logo']")

    def __init__(self, driver):
        self.driver = driver

    def check_form_validation(self):
        required_fields = self.driver.find_elements(*self.required_fields)
        submit_button = self.driver.find_element(*self.submit_button)
        self.driver.execute_script("arguments[0].click();", submit_button)
        (WebDriverWait(self.driver, 20)
         .until(EC.visibility_of_any_elements_located(self.validation_message)))
        for field in required_fields:
            validation_message = field.find_element(*self.validation_message)
            if not validation_message.is_displayed():
                return False
        return True

    def check_logo_link(self):
        logo_link = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(self.logo_link))
        self.driver.execute_script("arguments[0].click();", logo_link)
        wait = WebDriverWait(self.driver, 20)
        wait.until(EC.url_to_be("https://www.epam.com/"))

    def check_report_download(self):
        download_link = WebDriverWait(self.driver, 40).until(
            EC.element_to_be_clickable(self.download_button))
        self.driver.execute_script("arguments[0].click();", download_link)
        download_dir = '/Users/oleksandra/Downloads'
        filename = 'EPAM_Corporate_Overview_Q3_october.pdf'
        counter = 0
        max_attempts = 10
        while not os.path.exists(os.path.join(download_dir, filename)) and counter < max_attempts:
            time.sleep(1)
            counter += 1
        if counter < max_attempts:
            return True
        return False
