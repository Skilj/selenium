from selenium import webdriver


def test_open_url():
    """this test checks url"""

    browser = webdriver.Chrome()
    browser.maximize_window()

    browser.get("https://www.ya.ru/")
    actual_title = browser.title
    actual_url = browser.current_url

    assert actual_title == "Яндекс" or actual_title == "Oops, Captcha!"
    assert "https://www.ya.ru/" in actual_url

    browser.close()
    browser.quit()
