from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class RegistrationsPage:
    female_radio_button = (By.ID, "gender-female")
    male_radio_button = (By.ID, "gender-male")
    textbox_first_name = (By.ID, "FirstName")
    textbox_last_name = (By.ID, "LastName")
    textbox_email = (By.ID, "Email")
    textbox_password = (By.ID, "Password")
    textbox_confirm_password = (By.ID, "ConfirmPassword")
    button_register = (By.ID, "register-button")
    detected_user_name_element = (By.CSS_SELECTOR, "div[class='header-links'] a[class='account']")

    def __init__(self, driver):
        self.driver = driver

    def set_gender(self, gender):
        if gender.lower() == "female":
            self.driver.find_element(*self.female_radio_button).click()
        elif gender.lower() == "male":
            self.driver.find_element(*self.male_radio_button).click()

    def set_first_name(self, first_name):
        self.driver.find_element(*self.textbox_first_name).clear()
        self.driver.find_element(*self.textbox_first_name).send_keys(first_name)

    def set_last_name(self, last_name):
        self.driver.find_element(*self.textbox_last_name).clear()
        self.driver.find_element(*self.textbox_last_name).send_keys(last_name)

    def set_email(self, email):
        self.driver.find_element(*self.textbox_email).clear()
        self.driver.find_element(*self.textbox_email).send_keys(email)

    def set_password(self, password):
        self.driver.find_element(*self.textbox_password).clear()
        self.driver.find_element(*self.textbox_password).send_keys(password)

    def set_confirm_password(self, confirmed_password):
        self.driver.find_element(*self.textbox_confirm_password).clear()
        self.driver.find_element(*self.textbox_confirm_password).send_keys(confirmed_password)

    def click_register(self):
        self.driver.find_element(*self.button_register).click()

    def check_registered_user(self, expected_username):
        wait = WebDriverWait(self.driver, 10)
        detected_username_element = wait.until(
            EC.element_to_be_clickable(self.detected_user_name_element))
        detected_username = detected_username_element.text
        return detected_username == expected_username
