from typing import List, Union

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from vinted.vinted_constants import PAGES_TIMEOUT
from vinted.vinted_frame import VintedFrame


class VintedNotificationsPage(VintedFrame):
    title_xpath = "//div[contains(@class, 'Cell__cell') and @role='button']"
    notification_item_xpath = "//a[@data-testid='user-notification-item']"

    def __init__(self, driver: webdriver.Chrome):
        super().__init__(driver=driver, wait_for_essentials=False)
        self.wait_for_essentials()

    def wait_for_essentials(self, timeout: Union[float, int] = PAGES_TIMEOUT,
                            include_elements_after_login: bool = True) -> None:
        super().wait_for_essentials(timeout=timeout, include_elements_after_login=include_elements_after_login)
        for element_xpath in [self.title_xpath]:
            WebDriverWait(self.driver, timeout=timeout).\
                until(EC.element_to_be_clickable((By.XPATH, self.page_xpath + element_xpath)))

    def get_all_notifications(self) -> List[str]:
        return [notification.text for notification in self.driver.find_elements(by=By.XPATH,
                                                                                value=self.page_xpath +
                                                                                      self.notification_item_xpath)]
