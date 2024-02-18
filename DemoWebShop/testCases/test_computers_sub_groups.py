from DemoWebShop.pageObjects.ComputersGroup import ComputersGroup
from DemoWebShop.utilities.readProperties import ReadConfig
from DemoWebShop.utilities.customLogger import LogGen


class Test_003_ComputersGroup:
    base_url = ReadConfig.get_application_url()
    logger = LogGen.loggen()

    def test_computers_sub_groups(self, setup):
        self.logger.info("*************** Test_001_ComputersGroup *****************")
        self.logger.info("****Started Computers Sub-Groups test ****")
        e_driver = setup
        self.logger.info("****Opening URL****")
        e_driver.get(self.base_url)
        computers_group = ComputersGroup(e_driver)
        actual_sub_group_names = computers_group.get_computers_sub_groups()
        assert len(actual_sub_group_names) == 3, "**** Computers Sub-Groups count test failed ****"
        for name in ['Desktops', 'Notebooks', 'Accessories']:
            assert name in actual_sub_group_names, "**** Computers Sub-Groups name test failed ****"
        self.logger.info("**** Computers Sub-Groups test passed ****")

    def test_sorting(self, setup):
        self.logger.info("*************** Test_002_Sorting *****************")
        self.logger.info("****Started Sorting test ****")
        e_driver = setup
        self.logger.info("****Opening URL****")
        e_driver.get(self.base_url + "desktops")
        computers_group = ComputersGroup(e_driver)
        sorting_option_text = "Created on"
        products_order_before = computers_group.get_products_order()
        assert computers_group.select_sort_option(sorting_option_text), \
            "**** Sorting test failed ****"
        products_order_after = computers_group.get_products_order()
        assert products_order_before != products_order_after, \
            "**** Products order did not change after sorting ****"
        self.logger.info("**** Sorting test passed ****")

    def test_items_per_page(self, setup):
        self.logger.info("*************** Test_003_ItemsPerPage *****************")
        self.logger.info("**** Started Items Per Page Test ****")
        e_driver = setup
        self.logger.info("**** Opening URL ****")
        e_driver.get(self.base_url + "desktops")
        computers_group = ComputersGroup(e_driver)
        items_per_page_value = "4"
        is_correct_number_displayed = computers_group.select_items_per_page(items_per_page_value)
        assert is_correct_number_displayed, "**** Items Per Page Test Failed ****"
        products_count = computers_group.get_products_count()
        assert int(products_count) == int(
            items_per_page_value), "Displayed items per page did not match the selected value"
        self.logger.info("**** Items Per Page Test Passed ****")
