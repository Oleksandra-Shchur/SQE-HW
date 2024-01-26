from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HomePage:
    search_field_xpath = "//div[@class='search-results__action-section']"
    search_button_xpath = "//button[@class='header-search__button header__icon']"
    theme_switch_xpath = "//header/div[1]/div[1]/section[1]/div[1]"
    language_ukrainian_css = ".location-selector__link[href='https://careers.epam.ua']"
    language_indicator_xpath = ("//button[@class='location-selector__button']"
                                "//span[@class='location-selector__button-language']")
    policies_list_xpath = "//div[@class='policies']"
    location_list_xpath = "//div[@role='tablist']"

    def __init__(self, driver):
        self.driver = driver

    def get_title(self):
        return self.driver.title

    def switch_theme(self):
        wait = WebDriverWait(self.driver, 10)
        theme_switcher = wait.until(EC.element_to_be_clickable((By.XPATH, self.theme_switch_xpath)))
        theme_switcher.click()

    def check_theme(self):
        body = self.driver.find_element(By.TAG_NAME, 'body')
        classes = body.get_attribute('class')
        if 'dark-mode' in classes:
            return 'Dark Mode'
        elif 'light-mode' in classes:
            return 'Light Mode'

    def switch_language(self):
        self.driver.find_element(By.XPATH, self.language_indicator_xpath).click()
        wait = WebDriverWait(self.driver, 20)
        language_switcher = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.language_ukrainian_css)))
        language_switcher.click()
        wait.until(EC.url_contains("https://careers.epam.ua/"))

    def check_policies_list(self):
        expected_policies_items = ["INVESTORS", "COOKIE POLICY", "OPEN SOURCE", "APPLICANT PRIVACY NOTICE",
                                   "PRIVACY POLICY", "WEB ACCESSIBILITY"]
        policies_list = self.driver.find_element(By.XPATH, self.policies_list_xpath)
        actual_policies_items = [item.text.strip() for item in policies_list.find_elements(By.TAG_NAME, "li")]
        if sorted(actual_policies_items) == sorted(expected_policies_items):
            return True
        else:
            return False

    def switch_location(self, region):
        actual_location_link = self.driver.find_element(By.XPATH, f".//a[text()='{region}']")
        actual_location_link.click()
        if actual_location_link.text == 'EMEA':
            return 'EMEA'
        elif actual_location_link.text == 'APAC':
            return 'APAC'
        elif actual_location_link.text == 'AMERICAS':
            return 'AMERICAS'

    def check_location_list(self):
        expected_location_items = ["AMERICAS", "EMEA", "APAC"]
        location_list = self.driver.find_element(By.XPATH, self.location_list_xpath)
        actual_location_items = [item.text.strip() for item in location_list.find_elements(By.TAG_NAME, "a")]
        if actual_location_items == expected_location_items:
            return True
        else:
            return False

    def check_search(self, query):
        search_button = self.driver.find_element(By.XPATH, self.search_button_xpath)
        search_button.click()
        search_field = self.driver.find_element(By.XPATH, self.search_field_xpath)
        wait = WebDriverWait(self.driver, 20)
        wait.until(EC.element_to_be_clickable((By.XPATH, self.search_field_xpath)))
        search_field.send_keys(query + Keys.RETURN)
        wait.until(EC.url_contains("https://www.epam.com/search?q=AI"))
