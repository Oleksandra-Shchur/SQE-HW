from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    textbox_email_xpath = (By.XPATH, "//input[@id='Email']")
    textbox_password_xpath = (By.XPATH, "//input[@id='Password']")
    button_login_xpath = (By.XPATH, "//input[@value='Log in']")
    detected_user_name_element_xpath = (By.XPATH, "//a[normalize-space()='testuser098@example.com']")

    def __init__(self, driver):
        self.driver = driver

    def set_email(self, username):
        self.driver.find_element(*self.textbox_email_xpath).clear()
        self.driver.find_element(*self.textbox_email_xpath).send_keys(username)

    def set_password(self, password):
        self.driver.find_element(*self.textbox_password_xpath).clear()
        self.driver.find_element(*self.textbox_password_xpath).send_keys(password)

    def click_login(self):
        self.driver.find_element(*self.button_login_xpath).click()

    def check_logged_user(self, expected_username):
        wait = WebDriverWait(self.driver, 70)
        detected_username_element = wait.until(
            EC.element_to_be_clickable(self.detected_user_name_element_xpath))
        detected_username = detected_username_element.text
        return detected_username == expected_username
