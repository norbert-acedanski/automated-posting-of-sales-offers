from typing import Union

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from vinted.vinted_constants import MODALS_TIMEOUT


class VintedRegisterByEmailModal:
    modal_xpath = "//div[contains(@class, 'ReactModal__Content--after-open')]"
    x_button_xpath = "//span[@data-icon-name='x']//ancestor::button"
    full_name_textfield_xpath = "//input[@id='realName']"
    profile_name_textfield_xpath = "//input[@id='login']"
    email_textfield_xpath = "//input[@id='email']"
    password_textfield_xpath = "//input[@id='password']"
    want_to_receive_personalized_offers_checkbox_xpath = "//input[@id='subscribeToNewsletter']/span"
    confirm_regulations_checkbox_xpath = "//input[@id='agreeRules']/span"
    continue_button_xpath = "//button[@type='submit']"

    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver
        self.wait_for_essentials()

    def wait_for_essentials(self, timeout: Union[float, int] = MODALS_TIMEOUT) -> None:
        for element_xpath in [self.x_button_xpath, self.full_name_textfield_xpath, self.profile_name_textfield_xpath,
                              self.email_textfield_xpath, self.password_textfield_xpath,
                              self.want_to_receive_personalized_offers_checkbox_xpath,
                              self.confirm_regulations_checkbox_xpath, self.continue_button_xpath]:
            WebDriverWait(self.driver, timeout=timeout).\
                until(EC.element_to_be_clickable((By.XPATH, self.modal_xpath + element_xpath)))

    def fill_full_name(self, full_name: str) -> None:
        self.driver.find_element(by=By.XPATH,
                                 value=self.modal_xpath + self.full_name_textfield_xpath).send_keys(full_name)

    def fill_profile_name(self, profile_name: str) -> None:
        self.driver.find_element(by=By.XPATH,
                                 value=self.modal_xpath + self.profile_name_textfield_xpath).send_keys(profile_name)

    def fill_email(self, email: str) -> None:
        self.driver.find_element(by=By.XPATH, value=self.modal_xpath + self.email_textfield_xpath).send_keys(email)

    def fill_password(self, password: str) -> None:
        self.driver.find_element(by=By.XPATH,
                                 value=self.modal_xpath + self.password_textfield_xpath).send_keys(password)

    def click_on_select_personalized_offers_checkbox(self) -> None:
        self.driver.find_element(by=By.XPATH, value=self.modal_xpath +
                                                    self.want_to_receive_personalized_offers_checkbox_xpath).click()

    def click_on_confirm_regulations_checkbox(self) -> None:
        self.driver.find_element(by=By.XPATH, value=self.modal_xpath +
                                                    self.confirm_regulations_checkbox_xpath).click()

    def click_continue_button(self) -> NotImplemented:
        self.driver.find_element(by=By.XPATH, value=self.modal_xpath + self.continue_button_xpath)
        return NotImplemented
