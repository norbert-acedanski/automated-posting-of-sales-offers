from typing import List, Union

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from vinted.vinted_constants import MODALS_TIMEOUT
from vinted.vinted_generic_modal import VintedGenericModal


class VintedManageCookiesModal(VintedGenericModal):
    modal_xpath = "//div[@id='onetrust-pc-sdk']"
    x_button_xpath = "//button[@id='close-pc-btn-handler']"
    allow_all_cookies_xpath = "//button[@id='accept-recommended-btn-handler']"
    confirm_my_choices_xpath = "//button[contains(@class, 'onetrust-close-btn-handler')]"
    cookie_xpath = "//h4[text()='{}']/following-sibling::div"

    def __init__(self, driver: webdriver.Chrome):
        super().__init__(driver=driver)
        self.wait_for_essentials()

    def wait_for_essentials(self, timeout: Union[float, int] = MODALS_TIMEOUT) -> None:
        for element_xpath in [self.x_button_xpath, self.allow_all_cookies_xpath, self.confirm_my_choices_xpath]:
            WebDriverWait(self.driver, timeout=timeout).\
                until(EC.element_to_be_clickable((By.XPATH, self.modal_xpath + element_xpath)))

    def click_allow_all_cookies_button(self) -> None:
        self.driver.find_element(by=By.XPATH, value=self.modal_xpath + self.allow_all_cookies_xpath).click()

    def select_cookies_to_accept(self, cookies: List[str], uncheck: bool = False) -> None:
        for cookie in cookies:
            cookie_xpath = self.modal_xpath + self.cookie_xpath.format(cookie)
            current_cookie_element = self.driver.find_element(by=By.XPATH, value=cookie_xpath + "//input")
            if (current_cookie_element.get_attribute("aria-checked") == "false") is not uncheck:
                self.driver.find_element(by=By.XPATH, value=cookie_xpath).click()

    def click_confirm_my_choices_button(self) -> None:
        self.driver.find_element(by=By.XPATH, value=self.modal_xpath + self.confirm_my_choices_xpath).click()
