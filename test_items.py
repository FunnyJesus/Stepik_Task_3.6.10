from selenium.webdriver.common.by import By
import pytest
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_button(browser):
    browser.get(link)
    search_button = browser.find_element(By.CSS_SELECTOR, '.btn-add-to-basket')
    add_to_basket = search_button.text
    time.sleep(10)
    assert len(add_to_basket) > 0 , "Кнопки нет"


if __name__ == '__main__':
    pytest.main()