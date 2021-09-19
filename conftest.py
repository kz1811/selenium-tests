import pytest
from selenium import webdriver


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome(executable_path=r'c:\chromedriver\chromedriver.exe', language="en")
    yield browser
    print("\nquit browser..")
    browser.quit()
