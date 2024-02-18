from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def click(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def enter_text(self, locator, text):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.clear()
        element.send_keys(text)

    def select_from_dropdown(self, locator, option_text):
        dropdown_element = self.wait.until(EC.element_to_be_clickable(locator))
        select = Select(dropdown_element)
        select.select_by_visible_text(option_text)
        dropdown_element = self.wait.until(EC.element_to_be_clickable(locator))
        select = Select(dropdown_element)
        selected_option = select.first_selected_option.text.strip()
        return selected_option == option_text
