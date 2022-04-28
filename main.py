from selenium import webdriver
from credentials import Credentials
from prepare_and_check_offers import PrepareAndCheckOffers
from logging_to_sites import LoginOLX, LoginAllegroLokalnie, LoginSprzedajemy, LoginVinted
from opening_sites import OLXPage, AllegroLokalniePage, SprzedajemyPage, VintedPage

LIST_OF_SITES = ["OLX", "Allegro Lokalnie", "Sprzedajemy", "Vinted"]
credentials = Credentials()
LIST_OF_SITE_CREDENTIAL_FUNCTIONS = [credentials.get_olx_credentials, credentials.get_allegro_lokalnie_credentials, 
                                     credentials.get_sprzedajemy_credentials, credentials.get_vinted_credentials]
SITE_CREDENTIAL_FUNCTIONS_DICTIONARY = {site: credentials_function for site, credentials_function in zip(LIST_OF_SITES, LIST_OF_SITE_CREDENTIAL_FUNCTIONS)}
LIST_OF_BROWSERS = ["chrome", "edge", "firefox", "ie"]
LIST_OF_DRIVERS = [webdriver.Chrome, webdriver.Edge, webdriver.Firefox, webdriver.Ie]
BROWSER_DRIVER_DICTIONARY = {browser: driver for browser, driver in zip(LIST_OF_BROWSERS, LIST_OF_DRIVERS)}
driver = None

def prepare_and_check_offers():
    offer_poster = PrepareAndCheckOffers()
    offer_poster.add_offer_folders_with_photos(["Sample offer 1", "Sample offer 2"])
    offer_poster.add_properties_file_to_each_offer_folder()
    offer_poster.print_all_limitations()
    offer_poster.check_all_properties()

def get_credentials(desired_sites: list):
    for site in desired_sites:
        SITE_CREDENTIAL_FUNCTIONS_DICTIONARY[site]()

def open_choosen_browser():
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

if __name__ == "__main__":
    prepare_and_check_offers()
    get_credentials(LIST_OF_SITES)
    open_choosen_browser()