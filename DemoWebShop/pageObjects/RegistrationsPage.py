
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class RegistrationsPage:
    female_radio_button_xpath = (By.XPATH, "//input[@id='gender-female']")
    male_radio_button_xpath = (By.XPATH, "//input[@id='gender-male']")
    textbox_first_name_xpath = (By.XPATH, "//input[@id='FirstName']")
    textbox_last_name_xpath = (By.XPATH, "//input[@id='LastName']")
    textbox_email_xpath = (By.XPATH, "//input[@id='Email']")
    textbox_password_xpath = (By.XPATH, "//input[@id='Password']")
    textbox_confirm_password_xpath = (By.XPATH, "//input[@id='ConfirmPassword']")
    button_register_xpath = (By.XPATH, "//input[@id='register-button']")
    detected_user_name_element_css = (By.CSS_SELECTOR, "div[class='header-links'] a[class='account']")

    def __init__(self, driver):
        self.driver = driver

    def set_gender(self, gender):
        if gender.lower() == "female":
            self.driver.find_element(*self.female_radio_button_xpath).click()
        elif gender.lower() == "male":
            self.driver.find_element(*self.male_radio_button_xpath).click()

    def set_first_name(self, first_name):
        self.driver.find_element(*self.textbox_first_name_xpath).clear()
        self.driver.find_element(*self.textbox_first_name_xpath).send_keys(first_name)

    def set_last_name(self, last_name):
        self.driver.find_element(*self.textbox_last_name_xpath).clear()
        self.driver.find_element(*self.textbox_last_name_xpath).send_keys(last_name)

    def set_email(self, email):
        self.driver.find_element(*self.textbox_email_xpath).clear()
        self.driver.find_element(*self.textbox_email_xpath).send_keys(email)

    def set_password(self, password):
        self.driver.find_element(*self.textbox_password_xpath).clear()
        self.driver.find_element(*self.textbox_password_xpath).send_keys(password)

    def set_confirm_password(self, confirmed_password):
        self.driver.find_element(*self.textbox_confirm_password_xpath).clear()
        self.driver.find_element(*self.textbox_confirm_password_xpath).send_keys(confirmed_password)

    def click_register(self):
        self.driver.find_element(*self.button_register_xpath).click()

    def check_registered_user(self, expected_username):
        wait = WebDriverWait(self.driver, 70)
        detected_username_element = wait.until(
            EC.element_to_be_clickable(self.detected_user_name_element_css))
        detected_username = detected_username_element.text
        return detected_username == expected_username
