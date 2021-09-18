import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

supported_browsers = {
    'chrome': webdriver.Chrome,
    'firefox': webdriver.Firefox
}

def pytest_addoption(parser):
    parser.addoption("--browser_name", action='store', default='chrome', help="Choose browser: chrome or firefox")


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    browser = None

    if browser_name in supported_browsers:
        print(f"\nstart {browser_name} browser for test..")
        browser = supported_browsers.get("browser_name")()
    else:
        joined_browsers = ', '.join(supported_browsers.keys())
        raise pytest.UsageError(f"--browser_name should be one of: {joined_browsers}")
    yield browser
    print("\nquit browser..")
    browser.quit()
