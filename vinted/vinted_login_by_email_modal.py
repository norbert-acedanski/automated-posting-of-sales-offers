from typing import Union

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from vinted.vinted_constants import MODALS_TIMEOUT
from vinted.vinted_main_page import VintedMainPage


class VintedLoginByEmailModal:
    modal_xpath = "//div[contains(@class, 'ReactModal__Content--after-open')]"
    x_button_xpath = "//span[@data-icon-name='x']//ancestor::button"
    email_or_profile_name_textfield_xpath = "//input[@id='username']"
    password_textfield_xpath = "//input[@id='password']"
    continue_button_xpath = "//button[@type='submit']"

    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver
        self.wait_for_essentials()

    def wait_for_essentials(self, timeout: Union[float, int] = MODALS_TIMEOUT) -> None:
        for element_xpath in [self.x_button_xpath, self.email_or_profile_name_textfield_xpath,
                              self.password_textfield_xpath, self.continue_button_xpath]:
            WebDriverWait(self.driver, timeout=timeout).\
                until(EC.element_to_be_clickable((By.XPATH, self.modal_xpath + element_xpath)))

    def fill_email_profile_name(self, email_profile_name: str) -> None:
        self.driver.find_element(by=By.XPATH, value=self.modal_xpath + self.email_or_profile_name_textfield_xpath).\
            send_keys(email_profile_name)

    def fill_password(self, password: str) -> None:
        self.driver.find_element(by=By.XPATH,
                                 value=self.modal_xpath + self.password_textfield_xpath).send_keys(password)

    def click_continue_button(self) -> VintedMainPage:
        self.driver.find_element(by=By.XPATH, value=self.modal_xpath + self.continue_button_xpath)
        return VintedMainPage(self.driver)
