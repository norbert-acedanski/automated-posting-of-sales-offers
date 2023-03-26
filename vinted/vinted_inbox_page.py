from typing import Union, Dict

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from vinted.vinted_constants import PAGES_TIMEOUT, SHORT_TIMEOUT
from vinted.vinted_frame import VintedFrame
from vinted.vinted_propose_price_modal import VintedProposePriceModal


class VintedInboxPage(VintedFrame):
    page_xpath = "//div[contains(@class, 'fullpage-layout')]/ancestor::body"
    new_message_button_xpath = "//span[@data-icon-name='new-message']"
    choose_user_textfield_xpath = "//input[@id='new_recipient_select']"
    searched_user_xpath = "//span[@data-testid='user']//div[text()='{}']"
    current_inbox_user_name_xpath = "//div[@class='conversation-header']//div[@role='presentation']"
    current_inbox_item_name_xpath = "//a[@href]//h2"
    current_inbox_item_price_xpath = "//h3[@data-testid='service-fee-included-title']/../../span"
    propose_price_button_xpath = "//div[@class='u-flexbox']/button"
    send_message_textfield_xpath = "//textarea[@id='composerInput']"
    inbox_general_xpath = "//div[contains(@data-testid, 'inbox-list-item-') and contains(@class, 'cell')]"

    def __init__(self, driver: webdriver.Chrome):
        super().__init__(driver=driver)
        self.wait_for_essentials()
        self.wait_for_loading_indicator_to_disappear(timeout=SHORT_TIMEOUT)

    def wait_for_essentials(self, timeout: Union[float, int] = PAGES_TIMEOUT,
                            include_elements_after_login: bool = True) -> None:
        super().wait_for_essentials(timeout=timeout, include_elements_after_login=include_elements_after_login)
        for element_xpath in [self.new_message_button_xpath]:
            WebDriverWait(self.driver, timeout=timeout).\
                until(EC.element_to_be_clickable((By.XPATH, self.page_xpath + element_xpath)))

    def click_new_message_button(self) -> None:
        self.driver.find_element(by=By.XPATH, value=self.page_xpath + self.new_message_button_xpath).click()

    def choose_user(self, user_name: str) -> None:
        self.driver.find_element(by=By.XPATH, value=self.page_xpath +
                                                    self.choose_user_textfield_xpath).send_keys(user_name)
        WebDriverWait(self.driver, timeout=SHORT_TIMEOUT). \
            until(EC.element_to_be_clickable((By.XPATH, self.page_xpath + self.searched_user_xpath.format(user_name))))
        self.driver.find_element(by=By.XPATH, value=self.page_xpath + self.searched_user_xpath.format(user_name)).click()

    def get_current_inbox_user_name(self) -> str:
        return self.driver.find_element(by=By.XPATH, value=self.page_xpath + self.current_inbox_user_name_xpath).text

    def get_current_inbox_item_data(self) -> Dict[str, Union[str, float]]:
        item_name = self.driver.find_element(by=By.XPATH, value=self.page_xpath +
                                                                self.current_inbox_item_name_xpath).text
        item_price = self.driver.find_element(by=By.XPATH,
                                              value=self.page_xpath +
                                                    self.current_inbox_item_price_xpath).text.replace(",", ".")
        return {"name": item_name, "price": float(item_price.split()[0]), "currency": item_price.split()[1]}

    def click_propose_price_button(self) -> VintedProposePriceModal:
        self.driver.find_element(by=By.XPATH, value=self.page_xpath + self.propose_price_button_xpath).click()
        return VintedProposePriceModal(self.driver)

    def get_all_visible_inboxes_data(self) -> Dict[str, Dict[str, str]]:
        data = {}
        rough_data = [inbox.text.split("\n") for inbox in self.driver.find_elements(by=By.XPATH,
                                                                                    value=self.page_xpath +
                                                                                          self.inbox_general_xpath)]
        for inbox in rough_data:
            user, time, message = inbox[0], inbox[1], inbox[2]
            if user not in data:
                data[user] = {message: time}
            else:
                data[user].update({message: time})
        return data

    def send_message(self, message: str) -> None:
        message_textfield = self.driver.find_element(by=By.XPATH, value=self.page_xpath +
                                                                        self.send_message_textfield_xpath)
        message_textfield.send_keys(message)
        message_textfield.send_keys(Keys.ENTER)
