from typing import Union, Literal

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from vinted.vinted_constants import MODALS_TIMEOUT
from vinted.vinted_register_by_email_modal import VintedRegisterByEmailModal


class VintedRegisterLoginModal:
    modal_xpath = "//div[contains(@class, 'ReactModal__Content--after-open')]"
    x_button_xpath = "//span[@data-icon-name='x']//ancestor::button"
    register_by_email_xpath = "//span[@data-testid='auth-select-type--register-email' or " \
                              "@data-testid='auth-select-type--login-email']"
    login_register_switch_xpath = "//span[@data-testid='auth-select-type--{}-switch']"

    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver
        self.wait_for_essentials()

    def wait_for_essentials(self, timeout: Union[float, int] = MODALS_TIMEOUT) -> None:
        for element_xpath in [self.x_button_xpath, self.register_by_email_xpath, self.login_register_switch_xpath]:
            WebDriverWait(self.driver, timeout=timeout).\
                until(EC.element_to_be_clickable((By.XPATH, self.modal_xpath + element_xpath)))

    def click_x_button(self) -> None:
        self.driver.find_element(by=By.XPATH, value=self.modal_xpath + self.x_button_xpath).click()

    def click_register_by_email(self) -> VintedRegisterByEmailModal:
        self.driver.find_element(by=By.XPATH, value=self.modal_xpath + self.register_by_email_xpath).click()
        return VintedRegisterByEmailModal(self.driver)

    def switch_login_register(self, to_option: Literal["login", "register"]):
        to_option_dict = {"login": "register", "register": "login"}
        element_xpath = self.modal_xpath + self.login_register_switch_xpath.format(to_option_dict[to_option])
        if self.driver.find_element(by=By.XPATH, value=element_xpath).is_displayed():
            self.driver.find_element(by=By.XPATH, value=element_xpath).click()
