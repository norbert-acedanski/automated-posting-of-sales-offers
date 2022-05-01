import os
import json

from selenium import webdriver
from credentials import Credentials
from prepare_and_check_offers import PrepareAndCheckOffers
from logging_to_sites import LoginOLX, LoginAllegroLokalnie, LoginSprzedajemy, LoginVinted
from opening_sites import OpenOLX, OpenAllegroLokalnie, OpenSprzedajemy, OpenVinted
from post_offers import PostOLX, PostAllegroLokalnie, PostSprzedajemy, PostVinted
from prepare_and_check_offers import OFFERS_FOLDER_NAME

LIST_OF_BROWSERS = ["chrome", "edge", "firefox", "ie"]
LIST_OF_DRIVERS = [webdriver.Chrome, webdriver.Edge, webdriver.Firefox, webdriver.Ie]
BROWSER_DRIVER_DICTIONARY = {browser: driver for browser, driver in zip(LIST_OF_BROWSERS, LIST_OF_DRIVERS)}
PRIVATE_OFFER, BUSINESS_OFFER = "Prywatne", "Firmowe"
OFFERS_FOLDER_PATH = os.path.dirname(__file__) + "/"+ OFFERS_FOLDER_NAME + "/"
driver = None
credentials = Credentials()

def prepare_and_check_offers():
    offer_poster = PrepareAndCheckOffers()
    offer_poster.add_offer_folders_with_photos(["Sample offer 1", "Sample offer 2"])
    offer_poster.add_properties_file_to_each_offer_folder()
    offer_poster.print_all_limitations()
    offer_poster.check_all_properties()

def open_browser():
    global driver
    print("List of available browsers:")
    for browser_number, browser in enumerate(LIST_OF_BROWSERS, 1):
        print(f"{browser_number}: {browser}")
    browser_number = int(input("Choose browser: ")) - 1
    if browser_number not in range(len(LIST_OF_BROWSERS)):
        raise ValueError("Wrong number!")
    browser = LIST_OF_BROWSERS[browser_number]
    driver = BROWSER_DRIVER_DICTIONARY[browser](f"./resources/drivers/{browser}driver.exe")
    driver.maximize_window()

def post_offers_olx():
    global credentials
    OpenOLX.launch_page(driver)
    credentials.get_olx_credentials()
    olx = LoginOLX(driver)
    olx.login_to_page(credentials.login_olx, credentials.password_olx)
    del credentials.password_olx
    post_offer_olx = PostOLX(driver)
    list_of_offers = [offer.path for offer in os.scandir(OFFERS_FOLDER_PATH) if offer.is_dir()]
    for offer_path in list_of_offers:
        with open(offer_path + "/properties.json", "r") as properties_file:
            properties_data = json.load(properties_file)
        post_offer_olx.click_add_new_offer()
        post_offer_olx.fill_offer_with_data(properties_data, offer_path + "/photos")
        post_offer_olx.click_add_offer()
    olx.click_logout()

def post_offers_allegro_lokalnie():
    global credentials
    OpenAllegroLokalnie.launch_page(driver)
    credentials.get_allegro_lokalnie_credentials()
    allegro_lokalnie = LoginAllegroLokalnie(driver)
    allegro_lokalnie.login_to_page(credentials.login_allegro_lokalnie, credentials.password_allegro_lokalnie)
    del credentials.password_allegro_lokalnie
    post_offer_allegro_lokalnie = PostAllegroLokalnie(driver)
    list_of_offers = [offer.path for offer in os.scandir(OFFERS_FOLDER_PATH) if offer.is_dir()]
    for offer_path in list_of_offers:
        with open(offer_path + "/properties.json", "r") as properties_file:
            properties_data = json.load(properties_file)
        post_offer_allegro_lokalnie.click_add_new_offer()
        post_offer_allegro_lokalnie.fill_offer_with_data(properties_data, offer_path + "/photos")
        post_offer_allegro_lokalnie.click_add_offer()
    allegro_lokalnie.click_logout()

def post_offers_sprzedajemy():
    global credentials
    OpenSprzedajemy.launch_page(driver)
    credentials.get_sprzedajemy_credentials()
    sprzedajemy = LoginSprzedajemy(driver)
    sprzedajemy.login_to_page(credentials.login_sprzedajemy, credentials.password_sprzedajemy)
    del credentials.password_sprzedajemy
    post_offer_sprzedajemy = PostSprzedajemy(driver)
    list_of_offers = [offer.path for offer in os.scandir(OFFERS_FOLDER_PATH) if offer.is_dir()]
    for offer_path in list_of_offers:
        with open(offer_path + "/properties.json", "r") as properties_file:
            properties_data = json.load(properties_file)
        post_offer_sprzedajemy.click_add_new_offer()
        post_offer_sprzedajemy.fill_offer_with_data(properties_data, offer_path + "/photos")
        post_offer_sprzedajemy.click_add_offer()
    sprzedajemy.click_logout()

def post_offers_vinted():
    global credentials
    OpenVinted.launch_page(driver)
    credentials.get_vinted_credentials()
    vinted = LoginVinted(driver)
    vinted.login_to_page(credentials.login_vinted, credentials.password_vinted)
    del credentials.password_vinted
    post_offer_vinted = PostVinted(driver)
    list_of_offers = [offer.path for offer in os.scandir(OFFERS_FOLDER_PATH) if offer.is_dir()]
    for offer_path in list_of_offers:
        with open(offer_path + "/properties.json", "r") as properties_file:
            properties_data = json.load(properties_file)
        post_offer_vinted.click_add_new_offer()
        post_offer_vinted.fill_offer_with_data(properties_data, offer_path + "/photos")
        post_offer_vinted.click_add_offer()
    vinted.click_logout()

if __name__ == "__main__":
    prepare_and_check_offers()
    open_browser()
    post_offers_olx()
    post_offers_allegro_lokalnie()
    post_offers_sprzedajemy()
    post_offers_vinted()