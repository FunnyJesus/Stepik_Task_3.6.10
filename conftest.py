from selenium.webdriver.chrome.options import Options
import pytest
from selenium import webdriver

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None,
                     help="Choose language")


@pytest.fixture(scope="function")
def browser(request):
    language_name = request.config.getoption("language")

    if language_name is not None:
        print("\nstart browser for test..")
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': language_name})
        browser = webdriver.Chrome(options=options)
    else:
        raise pytest.UsageError("--Choose language")
    yield browser
    print("\nquit browser..")
    browser.quit()