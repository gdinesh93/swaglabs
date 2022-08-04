from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import pytest

@pytest.fixture()
def setup():
    serv_obj=Service("E:\\chromedriver_win32\\chromedriver.exe")
    driver = webdriver.Chrome(service=serv_obj)
    return driver

def pytest_configure(config):
    config._metadata['project name'] = 'Swag Labs'
    config._metadata['Module name'] = 'Customers'
    config._metadata['Tester'] = 'Dinesh'