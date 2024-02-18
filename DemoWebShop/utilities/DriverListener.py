# not used and broken imports, should be deleted before commit

import os
from selenium.webdriver.support.events import AbstractEventListener


class DriverListener(AbstractEventListener):
    def __init__(self, driver, logger, screenshots_dir):
        self.driver = driver
        self.logger = logger
        self.screenshots_dir = screenshots_dir

    def on_exception(self, exception, driver):
        test_name = os.environ.get('PYTEST_CURRENT_TEST').split('::')[-1].split(' ')[0]
        screenshot_file = os.path.join(self.screenshots_dir, f'{test_name}.png')
        driver.save_screenshot(screenshot_file)
        self.logger.error(f'{test_name} is failed')