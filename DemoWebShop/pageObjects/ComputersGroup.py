from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from DemoWebShop.pageObjects.BasePage import BasePage


class ComputersGroup(BasePage):
    computers_element = (By.XPATH, "//li[@class='inactive']//a[normalize-space()='Computers']")
    sub_group_elements = (By.XPATH, "//ul[@class='sublist']/li[@class='inactive']/a")
    sort_dropdown = (By.XPATH, "//select[@id='products-orderby']")
    items_per_page_dropdown = (By.XPATH, "//select[@id='products-pagesize']")
    products_locator = (By.CLASS_NAME, "product-grid")

    def get_products_order(self):
        product_elements = self.driver.find_elements(*self.products_locator)
        return [product.text.strip() for product in product_elements]

    def get_products_count(self):
        product_element = self.wait.until(EC.presence_of_element_located(self.products_locator))
        product_text = product_element.text.strip()
        products = product_text.split("\n")
        num_products = len(products) // 2
        return num_products

    def get_computers_sub_groups(self):
        self.click(self.computers_element)
        sub_group_elements = self.driver.find_elements(*self.sub_group_elements)
        return [element.text.strip() for element in sub_group_elements]

    def select_sort_option(self, option_text):
        return self.select_from_dropdown(self.sort_dropdown, option_text)

    def select_items_per_page(self, items_per_page):
        return self.select_from_dropdown(self.items_per_page_dropdown, str(items_per_page))
