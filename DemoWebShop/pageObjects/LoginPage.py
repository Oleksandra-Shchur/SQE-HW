from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from DemoWebShop.pageObjects.BasePage import BasePage


class LoginPage(BasePage):
    textbox_email = (By.ID, "Email")
    textbox_password = (By.ID, "Password")
    button_login = (By.XPATH, "//input[@value='Log in']")
    detected_user_name_element = (By.XPATH, "//a[normalize-space()='testuser098@example.com']")

    def set_email(self, username):
        self.enter_text(self.textbox_email, username)

    def set_password(self, password):
        self.driver.find_element(*self.textbox_password).clear()
        self.driver.find_element(*self.textbox_password).send_keys(password)

    def click_login(self):
        self.click(self.button_login)

    def check_logged_user(self, expected_username):
        wait = WebDriverWait(self.driver, 10)
        detected_username_element = wait.until(
            EC.element_to_be_clickable(self.detected_user_name_element))
        detected_username = detected_username_element.text
        return detected_username == expected_username
