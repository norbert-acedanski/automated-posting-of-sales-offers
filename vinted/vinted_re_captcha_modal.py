from typing import Union

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from vinted.vinted_constants import CAPTCHA_TIMEOUT


class VintedReCaptchaModal:
    modal_xpath = "//div[contains(@class, 'ReactModal__Content--after-open')]"
    x_button_xpath = "//span[@data-icon-name='x']//ancestor::button"
    re_captcha_i_frame_xpath = "//iframe[@title='reCAPTCHA']"
    re_captcha_i_am_not_a_robot_checkbox_xpath = "//*[contains(@class, 'recaptcha-checkbox ')]"


    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver
        self.wait_for_essentials()

    def wait_for_essentials(self, timeout: Union[float, int] = CAPTCHA_TIMEOUT) -> None:
        for element_xpath in [self.x_button_xpath, self.re_captcha_i_frame_xpath]:
            WebDriverWait(self.driver, timeout=timeout).\
                until(EC.element_to_be_clickable((By.XPATH, self.modal_xpath + element_xpath)))

    def click_x_button(self) -> None:
        self.driver.find_element(by=By.XPATH, value=self.modal_xpath + self.x_button_xpath).click()

    def click_i_am_not_a_robot_checkbox(self) -> None:
        self.driver.switch_to.frame(self.driver.find_element(by=By.XPATH, value=self.re_captcha_i_frame_xpath))
        self.wait_for_iframe_essentials()
        self.driver.find_element(by=By.XPATH, value=self.re_captcha_i_am_not_a_robot_checkbox_xpath).click()

    def wait_for_iframe_essentials(self) -> None:
        for element_xpath in [self.re_captcha_i_am_not_a_robot_checkbox_xpath]:
            WebDriverWait(self.driver, timeout=CAPTCHA_TIMEOUT).\
                until(EC.element_to_be_clickable((By.XPATH, element_xpath)))
