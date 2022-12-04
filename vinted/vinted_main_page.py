from typing import Literal, Union

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from vinted.vinted_constants import PAGES_TIMEOUT
from vinted.vinted_manage_cookies_modal import VintedManageCookiesModal
from vinted.vinted_sell_item_page import VintedSellItemPage
from vinted.vinter_register_login_modal import VintedRegisterLoginModal


class VintedMainPage:
    page_xpath = "//div[contains(@id, 'InAppMessage')]/parent::body"
    vinted_logo_xpath = "//div[@data-testid='header-logo-id']"
    search_bar_xpath = "//input[@id='search_text']"
    register_login_button_xpath = "//a[@role='button' and @data-testid='header--login-button']"
    sell_button_xpath = "//a[@role='button' and @rel='nofollow']"
    tabs_component_xpath = "//ul[@class='web_ui__Tabs__content']"
    cookie_buttons_component_xpath = "//div[@id='onetrust-button-group-parent']"
    cookie_button_xpath = "//button[@id='onetrust-{}-handler']"

    def __init__(self, driver: webdriver.Chrome, wait_for_essentials: bool = True, wait_for_cookies: bool = False):
        self.driver: webdriver = driver
        if wait_for_essentials:
            self.wait_for_essentials()
        if wait_for_cookies:
            self.wait_for_cookies()

    def wait_for_essentials(self, timeout: Union[float, int] = PAGES_TIMEOUT) -> None:
        for element_xpath in [self.vinted_logo_xpath, self.search_bar_xpath, self.sell_button_xpath,
                              self.tabs_component_xpath]:
            WebDriverWait(self.driver, timeout=timeout).\
                until(EC.element_to_be_clickable((By.XPATH, self.page_xpath + element_xpath)))

    def wait_for_cookies(self) -> None:
        option_xpath_dict = {"accept": "accept-btn", "reject": "reject-all", "manage": "pc-btn"}
        for xpath_format in ["accept", "reject", "manage"]:
            WebDriverWait(self.driver, timeout=PAGES_TIMEOUT).\
                until(EC.element_to_be_clickable((By.XPATH, self.page_xpath + self.cookie_buttons_component_xpath
                                                  + self.cookie_button_xpath.format(option_xpath_dict[xpath_format]))))

    def choose_cookies_option(self, option: Literal["accept", "reject", "manage"]) \
            -> Union[None, VintedManageCookiesModal]:
        option_xpath_dict = {"accept": "accept-btn", "reject": "reject-all", "manage": "pc-btn"}
        self.driver.find_element(by=By.XPATH, value=self.page_xpath + self.cookie_buttons_component_xpath +
                                                    self.cookie_button_xpath.format(option_xpath_dict[option])).click()
        if option == "manage":
            return VintedManageCookiesModal(self.driver)
        else:
            self.wait_for_essentials()

    def click_register_login_button(self) -> VintedRegisterLoginModal:
        self.driver.find_element(by=By.XPATH, value=self.page_xpath + self.register_login_button_xpath).click()
        return VintedRegisterLoginModal(self.driver)

    def click_sell_button(self) -> VintedSellItemPage:
        self.driver.find_element(by=By.XPATH, value=self.page_xpath + self.sell_button_xpath).click()
        return VintedSellItemPage(self.driver)
