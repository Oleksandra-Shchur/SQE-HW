from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HomePage:
    search_field = (By.XPATH, "//input[@id='new_form_search']")
    search_button = (By.XPATH, "//button[@class='header-search__button header__icon']")
    theme_switch = (By.XPATH, "//header/div[1]/div[1]/section[1]/div[1]")
    language_ukrainian = (By.CSS_SELECTOR, ".location-selector__link[href='https://careers.epam.ua']")
    language_indicator = (By.XPATH,
                          "//button[@class='location-selector__button']"
                          "//span[@class='location-selector__button-language']")
    policies_list = (By.XPATH, "//div[@class='policies']")
    location_list = (By.XPATH, "//div[@role='tablist']")

    def __init__(self, driver):
        self.driver = driver

    def get_title(self):
        return self.driver.title

    def switch_theme(self):
        wait = WebDriverWait(self.driver, 10)
        theme_switcher = wait.until(EC.element_to_be_clickable(self.theme_switch))
        theme_switcher.click()

    def check_theme(self):
        body = self.driver.find_element(By.TAG_NAME, 'body')
        classes = body.get_attribute('class')
        if 'dark-mode' in classes:
            return 'Dark Mode'
        elif 'light-mode' in classes:
            return 'Light Mode'

    def switch_language(self):
        self.driver.find_element(*self.language_indicator).click()
        wait = WebDriverWait(self.driver, 10)
        language_switcher = wait.until(EC.element_to_be_clickable(self.language_ukrainian))
        language_switcher.click()
        wait.until(EC.url_contains("https://careers.epam.ua/"))

    def check_policies_list(self):
        expected_policies_items = ["INVESTORS", "COOKIE POLICY", "OPEN SOURCE", "APPLICANT PRIVACY NOTICE",
                                   "PRIVACY POLICY", "WEB ACCESSIBILITY"]
        policies_list = self.driver.find_element(*self.policies_list)
        actual_policies_items = [item.text.strip() for item in policies_list.find_elements(By.TAG_NAME, "li")]
        return sorted(actual_policies_items) == sorted(expected_policies_items)

    def switch_location(self, region):
        actual_location_link = self.driver.find_element(By.XPATH, f".//a[text()='{region}']")
        self.driver.execute_script("arguments[0].click();", actual_location_link)
        return actual_location_link.text

    def check_location_list(self):
        expected_location_items = ["AMERICAS", "EMEA", "APAC"]
        location_list = self.driver.find_element(*self.location_list)
        actual_location_items = [item.text.strip() for item in location_list.find_elements(By.TAG_NAME, "a")]
        return actual_location_items == expected_location_items

    def check_search(self, query):
        search_button = self.driver.find_element(*self.search_button)
        search_button.click()
        wait = WebDriverWait(self.driver, 10)
        search_field = wait.until(EC.element_to_be_clickable(self.search_field))
        search_field.click()
        search_field.send_keys(query + Keys.RETURN)
        wait.until(EC.url_contains("https://www.epam.com/search?q=" + query))
