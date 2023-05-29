# this conftest file is used for avoid duplicates steps
# here webdriver.chrome() using each and every function in tes_login.py
from selenium import webdriver
import pytest


@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome()
        print("Launching Chrome browser")
    elif browser == 'firefox':
        driver = webdriver.Firefox()
        print("Launching firefox browser")
    return driver


def pytest_addoption(parser):    # this will get value from CLI/hooks
    parser.addoption("--browser")


@pytest.fixture()   # this will returns the browser value to setup method
def browser(request):
    return request.config.getoption("--browser")


#### Pytest htnl report3####################

# it is hook for adding environment info to HTML report
def pytest_configure(config):
    config._metadata['Project Name'] = 'nop commerce'
    config._metadata['Module Name'] = 'Customers'
    config._metadata['Tester'] = 'Paddu'


#It is hook for delete/modify environment info to HTML Report
@pytest.hookimpl(optionalhook=True)
def pytest_metadata(metadata):
    metadata.pop("java home", None)
    metadata.pop("Plugins", None)
