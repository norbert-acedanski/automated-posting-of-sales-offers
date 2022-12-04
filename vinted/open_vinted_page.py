from selenium.webdriver.chrome.service import Service

from vinted.vinted_constants import MAIN_PAGE_URL
from vinted.vinted_main_page import VintedMainPage

from selenium import webdriver


def open_vinted_main_page() -> VintedMainPage:
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("start-maximized")
    chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])
    driver = webdriver.Chrome(service=Service("./chromedriver/chromedriver.exe"), options=chrome_options)
    driver.get(MAIN_PAGE_URL)
    return VintedMainPage(driver=driver, wait_for_essentials=False, wait_for_cookies=True)
