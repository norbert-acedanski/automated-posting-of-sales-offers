from typing import Union, List

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from vinted.vinted_constants import MODALS_TIMEOUT
from vinted.vinted_member_page import VintedMemberPage
from vinted.vinted_personalize_page import VintedPersonalizePage
from vinted.vinted_settings_page import VintedSettingsPage
from vinted.vinted_wallet_page import VintedWalletPage


class VintedUserMenuDropdown:
    dropdown_xpath = "//div[@class='user-menu-group']"
    my_profile_option_xpath = "//a[contains(@href, 'members')]"
    settings_option_xpath = "//a[contains(@href, 'settings/profile')]"
    personalize_option_xpath = "//a[contains(@href, 'personalization')]"
    wallet_option_xpath = "//a[contains(@href, 'wallet')]"
    wallet_current_value_xpath = "//h4"
    charity_option_xpath = "//a[contains(@href, 'donations')]"
    logout_option_xpath = "//button"

    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver
        self.wait_for_essentials()

    def wait_for_essentials(self, timeout: Union[float, int] = MODALS_TIMEOUT) -> None:
        for element_xpath in [self.my_profile_option_xpath, self.settings_option_xpath, self.personalize_option_xpath,
                              self.wallet_option_xpath, self.charity_option_xpath, self.logout_option_xpath]:
            WebDriverWait(self.driver, timeout=timeout).\
                until(EC.element_to_be_clickable((By.XPATH, self.dropdown_xpath + element_xpath)))

    def click_my_profile_option(self) -> VintedMemberPage:
        self.driver.find_element(by=By.XPATH, value=self.dropdown_xpath + self.my_profile_option_xpath).click()
        return VintedMemberPage(self.driver)

    def click_settings_option(self) -> VintedSettingsPage:
        self.driver.find_element(by=By.XPATH, value=self.dropdown_xpath + self.settings_option_xpath).click()
        return VintedSettingsPage(self.driver)

    def click_personalize_option(self) -> VintedPersonalizePage:
        self.driver.find_element(by=By.XPATH, value=self.dropdown_xpath + self.personalize_option_xpath).click()
        return VintedPersonalizePage(self.driver)

    def click_wallet_option(self) -> VintedWalletPage:
        self.driver.find_element(by=By.XPATH, value=self.dropdown_xpath + self.wallet_option_xpath).click()
        return VintedWalletPage(self.driver)

    def get_current_wallet_value(self) -> float:
        wallet_value = self.driver.find_element(by=By.XPATH, value=self.dropdown_xpath +
                                                                   self.wallet_current_value_xpath).text
        return float(wallet_value.split()[0].replace(",", ""))

    def click_charity_option(self) -> VintedSettingsPage:
        self.driver.find_element(by=By.XPATH, value=self.dropdown_xpath + self.wallet_option_xpath).click()
        return VintedSettingsPage(self.driver)

    def click_logout_option(self):
        self.driver.find_element(by=By.XPATH, value=self.dropdown_xpath + self.logout_option_xpath).click()
        from vinted.vinted_main_page import VintedMainPage
        return VintedMainPage(self.driver)
