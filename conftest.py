import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options as OptionsFirefox

def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chrome', help='Choose browser (chrome of firefox')
    parser.addoption("--language", action='store', default="ru", help='Choose language')

@pytest.fixture(scope="function")
def browser(request):
    print("\nstart browser for test..")
    user_language = request.config.getoption("language")
    browser_name = request.config.getoption('browser_name')

    if browser_name == 'chrome':
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("disable-dev-shm-usage")
        options.add_argument("--window-size=1920,1080")
        options.add_argument("browserName: chrome")
        desired_capabilities = {
            "browserName": "chrome",
            "browserVersion": "latest",
            "video": "True",
            "platform": "WIN10",
            "platformName": "windows",
        }
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        browser = webdriver.Remote(options=options, desired_capabilities=desired_capabilities)

    elif browser_name == 'firefox':
        options = OptionsFirefox()
        options.set_preference("intl.accept_languages", user_language)
        browser = webdriver.Firefox(options=options)
    else:
        raise pytest.UsageError("browser_name should be 'chrome' of 'firefox'")
    yield browser
    print("\nquit browser..")
    browser.quit()
