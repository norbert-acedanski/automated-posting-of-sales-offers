from typing import Dict, List, Union

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from vinted.vinted_constants import PAGES_TIMEOUT
from vinted.vinted_frame import VintedFrame


class VintedFavoritesPage(VintedFrame):
    title_xpath = "//h1"
    favorite_item_xpath = "//div[@data-testid='grid-item']"
    favorite_item_url_xpath = favorite_item_xpath + "//a[contains(@data-testid, 'product-item-id-')]"
    favorite_item_member_xpath = favorite_item_xpath + "//h4[contains(@data-testid, 'owner-name')]"

    def __init__(self, driver: webdriver.Chrome):
        super().__init__(driver=driver, wait_for_essentials=False)
        self.wait_for_essentials()

    def wait_for_essentials(self, timeout: Union[float, int] = PAGES_TIMEOUT,
                            include_elements_after_login: bool = True) -> None:
        super().wait_for_essentials(timeout=timeout, include_elements_after_login=include_elements_after_login)
        for element_xpath in [self.title_xpath]:
            WebDriverWait(self.driver, timeout=timeout).\
                until(EC.element_to_be_clickable((By.XPATH, self.page_xpath + element_xpath)))
        self.wait_for_loading_indicator_to_disappear(timeout=5, include_page_xpath=False)

    def get_all_favourites_urls_by_member(self) -> Dict[str, str]:
        previous_count, current_count = -1, 0
        while previous_count != current_count:
            self.scroll_max_down()
            self.wait_for_loading_indicator_to_disappear(timeout=2)
            previous_count, current_count = current_count, len(self._get_visible_favorite_items())
        result: dict = {}
        for index, _ in enumerate(self._get_visible_favorite_items(), 1):
            member = \
                self.driver.find_element(by=By.XPATH,
                                         value=f"({self.page_xpath + self.favorite_item_member_xpath})[{index}]").text
            url = self.driver.find_element(by=By.XPATH,
                                           value=f"({self.page_xpath + self.favorite_item_url_xpath})[{index}]").\
                get_attribute("href")
            result[member] = [url] if member not in result else result[member] + [url]
        return result

    def _get_visible_favorite_items(self) -> List[WebElement]:
        """Returns only the currently visible list of items"""
        return self.driver.find_elements(by=By.XPATH, value=self.page_xpath + self.favorite_item_url_xpath)
