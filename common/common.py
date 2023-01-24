from selenium.webdriver.chrome.service import Service

from selenium import webdriver


def open_browser() -> webdriver:
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("start-maximized")
    chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])
    return webdriver.Chrome(service=Service("./chromedriver/chromedriver.exe"), options=chrome_options)
