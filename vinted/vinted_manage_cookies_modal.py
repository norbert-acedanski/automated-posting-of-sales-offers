from typing import List

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

MODALS_TIMEOUT = 10


class VintedManageCookiesModal:
    modal_xpath = "//div[@id='onetrust-pc-sdk']"
    x_button_xpath = "//button[@id='close-pc-btn-handler']"
    allow_all_cookies_xpath = "//button[@id='accept-recommended-btn-handler']"
    confirm_my_choices_xpath = "//button[]"
    cookie_xpath = "//h4[text()='{}']/following-sibling::div//input"

    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver
        self.wait_for_essentials()

    def wait_for_essentials(self) -> None:
        for element_xpath in [self.x_button_xpath, self.allow_all_cookies_xpath, self.confirm_my_choices_xpath]:
            WebDriverWait(self.driver, timeout=MODALS_TIMEOUT).\
                until(EC.element_to_be_clickable((By.XPATH, self.modal_xpath + element_xpath)))

    def click_x_button(self) -> None:
        self.driver.find_element(by=By.XPATH, value=self.modal_xpath + self.x_button_xpath).click()

    def click_allow_all_cookies_button(self) -> None:
        self.driver.find_element(by=By, value=self.modal_xpath + self.allow_all_cookies_xpath).click()

    def select_cookies_to_accept(self, cookies: List[str]) -> None:
        for cookie in cookies:
            current_cookie_element = self.driver.find_element(by=By.XPATH, value=cookie)
            if current_cookie_element.get_attribute("aria-checked") == "false":
                current_cookie_element.click()

    def click_confirm_my_choices_button(self) -> None:
        self.driver.find_element(by=By, value=self.modal_xpath + self.confirm_my_choices_xpath).click()
