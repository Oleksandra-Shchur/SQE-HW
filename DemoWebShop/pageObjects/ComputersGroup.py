from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select


class ComputersGroup:
    computers_element_xpath = (By.XPATH, "//li[@class='inactive']//a[normalize-space()='Computers']")
    sub_group_elements_xpath = (By.XPATH, "//ul[@class='sublist']/li[@class='inactive']/a")
    sort_dropdown_xpath = (By.XPATH, "//select[@id='products-orderby']")
    items_per_page_dropdown_xpath = (By.XPATH, "//select[@id='products-pagesize']")

    def __init__(self, driver):
        self.driver = driver

    def verify_computers_sub_groups(self):
        wait = WebDriverWait(self.driver, 10)
        computers_element = wait.until(
            EC.element_to_be_clickable(self.computers_element_xpath))
        computers_element.click()
        sub_group_elements = self.driver.find_elements(*self.sub_group_elements_xpath)
        # Validate the count of subgroup

        # expected categories and number of categories should be moved to test
        # in pages should be just logic how to get this names/numbers
        # if also should be changed to assert in test for better readability of test
        expected_sub_group_names = ['Desktops', 'Notebooks', 'Accessories']
        actual_sub_group_names = [element.text.strip() for element in sub_group_elements]
        if len(actual_sub_group_names) == 3:
            for name in expected_sub_group_names:
                if name not in actual_sub_group_names:
                    return False
            return True
        else:
            return False

    # Select from dropdown also shuld be moved to universal base method as click and enter text
    def select_sort_option(self, option_text):
        wait = WebDriverWait(self.driver, 10)
        sort_dropdown = wait.until(EC.element_to_be_clickable(self.sort_dropdown_xpath))
        select = Select(sort_dropdown)
        select.select_by_visible_text(option_text)
        sort_dropdown = wait.until(EC.element_to_be_clickable(self.sort_dropdown_xpath))
        select = Select(sort_dropdown)
        selected_option = select.first_selected_option.text.strip()
        return selected_option == option_text

    def select_items_per_page(self, items_per_page):
        wait = WebDriverWait(self.driver, 10)
        dropdown = wait.until(EC.element_to_be_clickable(self.items_per_page_dropdown_xpath))
        select = Select(dropdown)
        select.select_by_visible_text(str(items_per_page))
        dropdown = wait.until(EC.element_to_be_clickable(self.items_per_page_dropdown_xpath))
        select = Select(dropdown)
        selected_option = select.first_selected_option.text.strip()
        return selected_option == items_per_page
