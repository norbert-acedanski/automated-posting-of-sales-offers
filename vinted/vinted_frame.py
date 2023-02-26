from typing import Union

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from vinted.vinted_constants import PAGES_TIMEOUT

from vinted.vinted_notifications_dropdown import VintedNotificationsDropdown
from vinted.vinter_register_login_modal import VintedRegisterLoginModal


class VintedFrame:
    page_xpath = "//div[contains(@id, 'InAppMessage')]/parent::body"
    vinted_logo_xpath = "//*[@data-testid='header-logo-id']"
    search_bar_xpath = "//input[@id='search_text']"
    inbox_button_xpath = "//span[@data-icon-name='envelope']"
    notifications_button_xpath = "//span[@data-icon-name='bell']"
    new_notifications_icon_xpath = notifications_button_xpath + "/*"
    notifications_dropdown_xpath = notifications_button_xpath + "/ancestor::a[@role='button']/following-sibling::div[@class='header-notification-dropdown']"
    favorites_button_xpath = "//span[@data-icon-name='heart']"
    register_login_button_xpath = "//a[@role='button' and @data-testid='header--login-button']"
    user_menu_button_xpath = "//div[@id='user-menu-button']"
    sell_button_xpath = "//a[@role='button' and @rel='nofollow']"

    def __init__(self, driver: webdriver.Chrome, wait_for_essentials: bool = True):
        self.driver = driver
        if wait_for_essentials:
            self.wait_for_essentials()

    def wait_for_essentials(self, timeout: Union[float, int] = PAGES_TIMEOUT,
                            include_elements_after_login: bool = False) -> None:
        for element_xpath in [self.vinted_logo_xpath, self.search_bar_xpath, self.sell_button_xpath]:
            WebDriverWait(self.driver, timeout=timeout).\
                until(EC.element_to_be_clickable((By.XPATH, self.page_xpath + element_xpath)))
        if include_elements_after_login:
            for element_xpath in [self.inbox_button_xpath, self.notifications_button_xpath, self.favorites_button_xpath,
                                  self.user_menu_button_xpath]:
                WebDriverWait(self.driver, timeout=timeout).\
                    until(EC.element_to_be_clickable((By.XPATH, self.page_xpath + element_xpath)))
        else:
            WebDriverWait(self.driver, timeout=timeout).\
                until(EC.element_to_be_clickable((By.XPATH, self.page_xpath + self.register_login_button_xpath)))

    def click_vinted_logo(self):
        self.driver.find_element(by=By.XPATH, value=self.page_xpath + self.vinted_logo_xpath).click()
        from vinted.vinted_main_page import VintedMainPage
        return VintedMainPage(self.driver)

    def click_inbox_button(self):
        self.driver.find_element(by=By.XPATH, value=self.page_xpath + self.inbox_button_xpath).click()
        from vinted.vinted_inbox_page import VintedInboxPage
        return VintedInboxPage(self.driver)

    def is_there_a_new_notification(self) -> bool:
        try:
            int(self.driver.find_element(by=By.XPATH, value=self.page_xpath + self.new_notifications_icon_xpath).
                get_attribute("aria-label").split()[0])
        except ValueError:
            return False
        return True

    def get_number_of_unread_notifications(self) -> int:
        if self.is_there_a_new_notification():
            return int(self.driver.find_element(by=By.XPATH, value=self.page_xpath + self.new_notifications_icon_xpath).
                       get_attribute("aria-label").split()[0])
        return 0

    def click_notifications_button(self) -> VintedNotificationsDropdown:
        self.driver.find_element(by=By.XPATH, value=self.page_xpath + self.notifications_button_xpath).click()
        return VintedNotificationsDropdown(self.driver)

    def is_notifications_dropdown_opened(self) -> bool:
        try:
            self.driver.find_element(by=By.XPATH, value=self.page_xpath + self.notifications_dropdown_xpath)
        except NoSuchElementException:
            return False
        return True

    def click_favorites_button(self) -> VintedFavoritesPage:
        self.driver.find_element(by=By.XPATH, value=self.page_xpath + self.favorites_button_xpath).click()
        return VintedFavoritesPage(self.driver)  # TODO: Not implemented

    def click_register_login_button(self) -> VintedRegisterLoginModal:
        self.driver.find_element(by=By.XPATH, value=self.page_xpath + self.register_login_button_xpath).click()
        return VintedRegisterLoginModal(self.driver)

    def click_user_menu_button(self) -> VintedUserMenuDropdown:
        self.driver.find_element(by=By.XPATH, value=self.page_xpath + self.register_login_button_xpath).click()
        return VintedUserMenuDropdown(self.driver)  # TODO: Not implemented

    def click_sell_button(self):
        self.driver.find_element(by=By.XPATH, value=self.page_xpath + self.sell_button_xpath).click()
        from vinted.vinted_sell_item_page import VintedSellItemPage
        return VintedSellItemPage(self.driver)
