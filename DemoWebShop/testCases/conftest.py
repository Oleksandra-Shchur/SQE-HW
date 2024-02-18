import pytest
import os
from selenium import webdriver
from utilities.customLogger import LogGen
from utilities.DriverListener import DriverListener
from selenium.webdriver.support.events import EventFiringWebDriver

logger = LogGen.loggen()
current_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.dirname(current_dir)
screenshots_dir = os.path.join(project_dir, 'Screenshots')


@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome()
        print("Launching chrome browser.........")
    elif browser == 'firefox':
        driver = webdriver.Firefox()
        print("Launching firefox browser.........")
    elif browser == 'safari':
        driver = webdriver.Safari()
        print("Launching Safari browser.........")
    else:
        raise Exception("No browser provided ")
    driver.maximize_window()
    e_driver = EventFiringWebDriver(driver, DriverListener(driver, logger, screenshots_dir))
    yield e_driver
    e_driver.quit()


def pytest_addoption(parser):
    parser.addoption("--browser",
                     action="store",
                     default="chrome",
                     help="Type in browser type")


@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")
