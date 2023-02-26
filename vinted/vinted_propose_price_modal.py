from typing import Union

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from vinted.vinted_constants import MODALS_TIMEOUT
from vinted.vinted_generic_modal import VintedGenericModal


class VintedProposePriceModal(VintedGenericModal):
    propose_price_textfield_xpath = "//input[@name='offer']"
    propose_price_button_xpath = "//button[@type='submit']"
    success_icon_xpath = "//span[@data-testid='loader']"

    def __init__(self, driver: webdriver.Chrome):
        super().__init__(driver=driver)
        self.wait_for_essentials()

    def wait_for_essentials(self, timeout: Union[float, int] = MODALS_TIMEOUT) -> None:
        for element_xpath in [self.x_button_xpath, self.propose_price_textfield_xpath, self.propose_price_button_xpath]:
            WebDriverWait(self.driver, timeout=timeout).\
                until(EC.element_to_be_clickable((By.XPATH, self.modal_xpath + element_xpath)))

    def input_proposed_price(self, price: float, clear_before: bool = True) -> None:
        textfield = self.driver.find_element(by=By.XPATH, value=self.modal_xpath + self.propose_price_textfield_xpath)
        if clear_before:
            textfield.send_keys(f"{Keys.CONTROL}a{Keys.DELETE}")
        textfield.send_keys(price)

    def click_propose_price_button(self) -> None:
        self.driver.find_element(by=By.XPATH, value=self.modal_xpath + self.propose_price_button_xpath).click()
        WebDriverWait(self.driver, timeout=5). \
            until(EC.visibility_of_element_located((By.XPATH, self.success_icon_xpath)))
        WebDriverWait(self.driver, timeout=5). \
            until(EC.invisibility_of_element((By.XPATH, self.success_icon_xpath)))
