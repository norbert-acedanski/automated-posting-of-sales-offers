from typing import Union

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from vinted.vinted_constants import TWO_FACTOR_VERIFICATION_TIMEOUT


class VintedTwoFactorVerificationModal:
    modal_xpath = "//div[contains(@id, 'TwoFactorVerification')]"
    verification_code_textfield_xpath = "//input[@id='verification_code']"
    trusted_device_checkbox_xpath = "//input[@id='isTrustedDevice']"
    verify_button_xpath = "//button"
    new_code_button_xpath = "//div/span/h4"

    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver
        self.wait_for_essentials()

    def wait_for_essentials(self, timeout: Union[float, int] = TWO_FACTOR_VERIFICATION_TIMEOUT) -> None:
        for element_xpath in [self.verification_code_textfield_xpath, self.trusted_device_checkbox_xpath,
                              self.verify_button_xpath, self.new_code_button_xpath]:
            WebDriverWait(self.driver, timeout=timeout).\
                until(EC.presence_of_element_located((By.XPATH, self.modal_xpath + element_xpath)))

    def click_remember_device_checkbox(self) -> None:
        self.driver.find_element(by=By.XPATH, value=self.modal_xpath + self.trusted_device_checkbox_xpath).click()

    def click_verify(self) -> None:
        self.driver.find_element(by=By.XPATH, value=self.modal_xpath + self.verify_button_xpath).click()

    def click_new_code(self) -> None:
        self.driver.find_element(by=By.XPATH, value=self.modal_xpath + self.new_code_button_xpath).click()
