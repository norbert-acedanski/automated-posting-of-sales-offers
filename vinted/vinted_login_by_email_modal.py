from typing import Union

from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from vinted.vinted_constants import MODALS_TIMEOUT
from vinted.vinted_re_captcha_modal import VintedReCaptchaModal
from vinted.vinted_two_factor_verification_modal import VintedTwoFactorVerificationModal


class VintedLoginByEmailModal:
    modal_xpath = "//div[contains(@class, 'ReactModal__Content--after-open')]"
    x_button_xpath = "//span[@data-icon-name='x']//ancestor::button"
    email_or_profile_name_textfield_xpath = "//input[@id='username']"
    password_textfield_xpath = "//input[@id='password']"
    continue_button_xpath = "//button[@type='submit']"
    incorrect_login_or_password_warning_xpath = "//span[contains(@class, 'Text__warning')]"
    loading_indicator_xpath = "//*[local-name()='circle']"

    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver
        self.wait_for_essentials()

    def wait_for_essentials(self, timeout: Union[float, int] = MODALS_TIMEOUT) -> None:
        for element_xpath in [self.x_button_xpath, self.email_or_profile_name_textfield_xpath,
                              self.password_textfield_xpath, self.continue_button_xpath]:
            WebDriverWait(self.driver, timeout=timeout).\
                until(EC.element_to_be_clickable((By.XPATH, self.modal_xpath + element_xpath)))

    def click_x_button(self) -> None:
        self.driver.find_element(by=By.XPATH, value=self.modal_xpath + self.x_button_xpath).click()

    def fill_email_profile_name(self, email_profile_name: str) -> None:
        self.driver.find_element(by=By.XPATH, value=self.modal_xpath + self.email_or_profile_name_textfield_xpath).\
            send_keys(email_profile_name)

    def fill_password(self, password: str) -> None:
        self.driver.find_element(by=By.XPATH,
                                 value=self.modal_xpath + self.password_textfield_xpath).send_keys(password)

    def click_continue_button(self) -> None:
        self.driver.find_element(by=By.XPATH, value=self.modal_xpath + self.continue_button_xpath).click()
        if self._is_recaptcha_visible():
            input("Unfortunately, reCAPTCHA modal was opened while login attempt. "
                  "Complete recaptcha and click Enter...")
        if self.driver.find_elements(by=By.XPATH, value=self.modal_xpath +
                                                        self.incorrect_login_or_password_warning_xpath):
            raise ValueError("Wrong login or password!")
        if self._is_confirm_your_activity_visible():
            input("Unfortunately, a two factor verification modal was opened while login attempt. "
                  "Input the code received and click Enter here...")
        WebDriverWait(self.driver, timeout=MODALS_TIMEOUT). \
            until_not(EC.presence_of_element_located((By.XPATH, self.modal_xpath + self.loading_indicator_xpath)))

    def _is_recaptcha_visible(self) -> bool:
        try:
            re_captcha_modal = VintedReCaptchaModal(self.driver)
        except TimeoutException:
            return False
        re_captcha_modal.click_i_am_not_a_robot_checkbox()
        return True

    def _is_confirm_your_activity_visible(self) -> bool:
        try:
            VintedTwoFactorVerificationModal(self.driver)
        except TimeoutException:
            return False
        return True
