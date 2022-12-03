from vinted.vinted_constants import MAIN_PAGE_URL
from vinted.vinted_main_page import VintedMainPage

from selenium import webdriver


def open_vinted_main_page() -> VintedMainPage:
    driver = webdriver.Chrome()
    driver.get(MAIN_PAGE_URL)
    return VintedMainPage(driver=driver, wait_for_essentials=False, wait_for_cookies=True)
