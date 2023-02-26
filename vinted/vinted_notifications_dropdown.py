from typing import Union, List

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from vinted.vinted_constants import MODALS_TIMEOUT
from vinted.vinted_notifications_page import VintedNotificationsPage


class VintedNotificationsDropdown:
    dropdown_xpath = "//span[@data-icon-name='bell']/ancestor::a[@role='button']/following-sibling::div[@class='header-notification-dropdown']"
    notification_general_xpath = "//a[@data-testid]"
    see_all_button_xpath = "//a[@role='button']"

    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver
        self.wait_for_essentials()

    def wait_for_essentials(self, timeout: Union[float, int] = MODALS_TIMEOUT) -> None:
        for element_xpath in [self.notification_general_xpath, self.see_all_button_xpath]:
            WebDriverWait(self.driver, timeout=timeout).\
                until(EC.element_to_be_clickable((By.XPATH, self.dropdown_xpath + element_xpath)))

    def get_all_notifications_text(self) -> List[str]:
        return [element.text for element in self.driver.find_elements(by=By.XPATH,
                                                                      value=self.dropdown_xpath +
                                                                            self.notification_general_xpath)]

    def click_notification_by_index(self, index: int):
        """Starts at 1"""
        self.driver.find_element(by=By.XPATH, value=f"({self.dropdown_xpath + self.notification_general_xpath})"
                                                    f"[{index}]").click()

    def click_see_all(self) -> VintedNotificationsPage:
        self.driver.find_element(by=By.XPATH, value=self.dropdown_xpath + self.see_all_button_xpath).click()
        return VintedNotificationsPage(self.driver)
