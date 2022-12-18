import time
from typing import Union, List, Dict

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from vinted_edit_profile_page import VintedEditProfilePage
from vinted_constants import PAGES_TIMEOUT, SHORT_TIMEOUT


class VintedMemberPage:
    page_xpath = "//div[contains(@id, 'InAppMessage')]/parent::body"
    profile_picture_xpath = "//div[@class='u-flexbox']/div/div[contains(@class, 'Image__image')]"
    profile_name = "//h1"
    profile_rating = "//button[@data-testid='rating-button']"
    number_of_stars = profile_rating + "//div[contains(@class, 'Rating__rating')]"
    number_of_comments_xpath = profile_rating + "//div[contains(@class, 'Rating__label')]"
    edit_profile_button_xpath = "//span[@data-icon-name='pencil']/ancestor::a[@role='button']"

    my_closet_tab_xpath = "//li[@id='closet']"
    items_count_xpath = "//h2/span"
    items_general_xpath = "//div[contains(@class, 'feed-grid__item ')]"

    feedback_tab_xpath = "//li[@id='feedback']"
    feedback_part_xpath = "//div[@class='profile u-flex-direction-column']/div[contains(@class, 'Cell__default')]"
    comment_general_xpath = feedback_part_xpath + "/div/div/div[contains(@class, 'Cell__cell')]"
    comment_user_name_xpath = comment_general_xpath + "//div[@data-testid='feedback-item--title']/*"
    comment_rating_xpath = comment_general_xpath + "//div[contains(@class, 'Rating__regular')]"
    comment_comment_xpath = comment_rating_xpath + "/following-sibling::span"

    def __init__(self, driver: webdriver.Chrome):
        self.driver: webdriver = driver
        self.wait_for_essentials()

    def wait_for_essentials(self, timeout: Union[float, int] = PAGES_TIMEOUT) -> None:
        for element_xpath in [self.profile_picture_xpath, self.profile_name, self.profile_rating,
                              self.number_of_comments_xpath, self.edit_profile_button_xpath, self.my_closet_tab_xpath,
                              self.feedback_tab_xpath, self.items_count_xpath, self.items_general_xpath]:
            WebDriverWait(self.driver, timeout=timeout).\
                until(EC.element_to_be_clickable((By.XPATH, self.page_xpath + element_xpath)))

    def get_profile_name(self) -> str:
        return self.driver.find_element(by=By.XPATH, value=self.page_xpath + self.profile_name).text

    def get_profile_rating(self) -> int:
        """Returns rating of a profile from 1 to 5 including"""
        member_rating = self.driver.find_element(by=By.XPATH, value=self.page_xpath + self.number_of_stars).\
            get_attribute("aria-label")
        return int(member_rating.replace("Member rated ", "").split(" out of ")[0])

    def get_number_of_comments(self) -> int:
        element_text = self.driver.find_element(by=By.XPATH, value=self.page_xpath + self.number_of_comments_xpath).text
        return int(element_text.split()[0])

    def click_edit_profile_button(self) -> VintedEditProfilePage:
        self.driver.find_element(by=By.XPATH, value=self.page_xpath + self.edit_profile_button_xpath).click()
        return VintedEditProfilePage(self.driver)  # TODO: Not implemented

    def click_my_closet_tab(self) -> None:
        self.scroll_max_up()
        self.driver.find_element(by=By.XPATH, value=self.page_xpath + self.my_closet_tab_xpath).click()
        WebDriverWait(self.driver, timeout=SHORT_TIMEOUT). \
            until(EC.invisibility_of_element_located(
                (By.XPATH, self.page_xpath + "//div[@class='web_ui__Spacer__large web_ui__Spacer__horizontal']")))

    def get_number_of_user_items(self) -> int:
        return int(self.driver.find_element(by=By.XPATH, value=self.page_xpath + self.items_count_xpath).
                   text.split()[0])

    def get_number_of_visible_items(self) -> int:
        return len(self.driver.find_elements(by=By.XPATH, value=self.page_xpath + self.items_general_xpath))

    def get_links_to_all_items(self) -> List[str]:
        while self.get_number_of_visible_items() != self.get_number_of_user_items():
            self.scroll_max_down()
        all_items = self.driver.find_elements(by=By.XPATH, value=self.page_xpath + self.items_general_xpath + "//a")
        return [item.get_attribute("href") for item in all_items]

    def click_feedback_tab(self) -> None:
        self.scroll_max_up()
        self.driver.find_element(by=By.XPATH, value=self.page_xpath + self.feedback_tab_xpath).click()
        WebDriverWait(self.driver, timeout=SHORT_TIMEOUT). \
            until(EC.visibility_of_element_located(
                (By.XPATH, self.page_xpath + "//div[@class='web_ui__Spacer__large web_ui__Spacer__horizontal']")))

    def get_number_of_visible_comments(self) -> int:
        return len(self.driver.find_elements(by=By.XPATH, value=self.page_xpath + self.comment_general_xpath))

    def get_comments_and_rating_from_users_feedback(self) -> Dict[str, Dict[str, Union[str, int]]]:
        while self.get_number_of_visible_comments() != self.get_number_of_comments():
            self.scroll_max_down()
        comments_and_ratings_dict = {}
        for index in range(1, self.get_number_of_comments() + 1):
            current_user_name = self.driver.find_element(by=By.XPATH,
                                                         value=f"({self.comment_user_name_xpath})[{index}]").text
            current_user_rating = \
                int(self.driver.find_element(by=By.XPATH, value=f"({self.comment_rating_xpath})[{index}]").
                    get_attribute("aria-label").replace("Member rated ", "").split(" out of ")[0])
            current_user_comment = self.driver.find_element(by=By.XPATH,
                                                            value=f"({self.comment_comment_xpath})[{index}]").text
            comments_and_ratings_dict[current_user_name] = {"rating": current_user_rating,
                                                            "comment": current_user_comment}
        return comments_and_ratings_dict

    def scroll_max_down(self) -> None:
        self.driver.execute_script("window.scrollTo(0,0)")
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        time.sleep(0.5)

    def scroll_max_up(self) -> None:
        self.driver.execute_script("window.scrollTo(0,0)")
