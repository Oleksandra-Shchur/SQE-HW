import pytest
from selenium import webdriver


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
    yield driver
    driver.quit()


def pytest_addoption(parser):
    parser.addoption("--browser",
                     action="store",
                     default="chrome",
                     help="Type in browser type")


@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")
