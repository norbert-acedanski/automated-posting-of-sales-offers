from typing import Union, Literal

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from vinted.vinted_constants import MODALS_TIMEOUT
from vinted.vinted_generic_modal import VintedGenericModal
from vinted.vinted_login_by_email_modal import VintedLoginByEmailModal
from vinted.vinted_register_by_email_modal import VintedRegisterByEmailModal


class VintedRegisterLoginModal(VintedGenericModal):
    continue_with_facebook_button_xpath = "//span[@data-icon-name='signup/facebook']/ancestor::button"
    continue_with_google_button_xpath = "//span[@data-icon-name='signup/google']/ancestor::button"
    continue_with_apple_button_xpath = "//span[@data-icon-name='signup/apple']/ancestor::button"
    register_by_email_xpath = "//span[@data-testid='auth-select-type--register-email']"
    login_by_email_xpath = "//span[@data-testid='auth-select-type--login-email']"
    login_register_switch_xpath = "//span[@data-testid='auth-select-type--{}-switch']"

    def __init__(self, driver: webdriver.Chrome):
        super().__init__(driver=driver)
        self.wait_for_essentials()

    def wait_for_essentials(self, timeout: Union[float, int] = MODALS_TIMEOUT) -> None:
        for element_xpath in [self.x_button_xpath, self.continue_with_facebook_button_xpath,
                              self.continue_with_google_button_xpath, self.continue_with_apple_button_xpath,
                              self.register_by_email_xpath, self.login_register_switch_xpath.format("register")]:
            WebDriverWait(self.driver, timeout=timeout).\
                until(EC.element_to_be_clickable((By.XPATH, self.modal_xpath + element_xpath)))

    def click_register_by_email(self) -> VintedRegisterByEmailModal:
        self.driver.find_element(by=By.XPATH, value=self.modal_xpath + self.register_by_email_xpath).click()
        return VintedRegisterByEmailModal(self.driver)

    def click_login_by_email(self) -> VintedLoginByEmailModal:
        self.driver.find_element(by=By.XPATH, value=self.modal_xpath + self.login_by_email_xpath).click()
        return VintedLoginByEmailModal(self.driver)

    def switch_login_register(self, to_option: Literal["login", "register"]):
        to_option_dict = {"login": "register", "register": "login"}
        element_xpath = self.modal_xpath + self.login_register_switch_xpath.format(to_option_dict[to_option])
        if self.driver.find_elements(by=By.XPATH, value=element_xpath):
            self.driver.find_element(by=By.XPATH, value=element_xpath).click()
