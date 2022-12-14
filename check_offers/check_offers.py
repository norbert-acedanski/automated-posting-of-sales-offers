import json
import os
from typing import List, Dict, Union

from colors.colors import ForegroundColors as FC, BackgroundColors as BC, Styles
from common.common import OFFERS_FOLDER_PATH, PROPERTIES_JSON, PHOTOS
from common.limits import GeneralLimits, OLXLimits, AllegroLokalnieLimits, SprzedajemyLimits, VintedLimits


class CheckOffersForSites:
    def __init__(self):
        self.global_offers_path = os.path.dirname(__file__)[:os.path.dirname(__file__).rfind("\\")] + OFFERS_FOLDER_PATH
        self.title_boundaries = {"OLX": OLXLimits.title, "Allegro Lokalnie": AllegroLokalnieLimits.title,
                                 "Sprzedajemy": SprzedajemyLimits.title, "Vinted": VintedLimits.title}
        self.description_boundaries = {"OLX": OLXLimits.description,
                                       "Allegro Lokalnie": AllegroLokalnieLimits.description,
                                       "Sprzedajemy": SprzedajemyLimits.description,
                                       "Vinted": VintedLimits.description}
        self.number_of_photos_boundaries = {"OLX": OLXLimits.number_of_photos,
                                            "Allegro Lokalnie": AllegroLokalnieLimits.number_of_photos,
                                            "Sprzedajemy": SprzedajemyLimits.number_of_photos,
                                            "Vinted": VintedLimits.number_of_photos}
        self.sexes = GeneralLimits.sexes
        self.conditions = GeneralLimits.conditions
        self.package_sizes = GeneralLimits.package_sizes
        self.list_of_offers = self._get_list_of_offers()
        self.numbers_of_photos = self._get_numbers_of_photos()
        self.list_of_properties = self._get_list_of_properties()
        self.offers_properties = {offer: properties for offer, properties in zip(self.list_of_offers,
                                                                                 self.list_of_properties)}

    def _get_list_of_offers(self) -> List[str]:
        return [offer.path[offer.path.rfind("\\") + 1:] for offer in os.scandir(self.global_offers_path)
                if offer.is_dir()]

    def _get_numbers_of_photos(self) -> List[int]:
        return [len(os.listdir(f"{self.global_offers_path}/{offer_name}/{PHOTOS}"))
                for offer_name in self.list_of_offers]

    def _get_list_of_properties(self) -> List[Dict[str, Union[str, List[str], Dict[str, List[str]]]]]:
        properties = []
        for offer, number_of_photos in zip(self.list_of_offers, self.numbers_of_photos):
            with open(f"{self.global_offers_path}/{offer}/{PROPERTIES_JSON}", "r") as properties_file:
                properties_data = json.load(properties_file)
            properties_data["photos"] = number_of_photos
            properties.append(properties_data)
        return properties

    def check_title_lengths(self):
        for offer_title in self.offers_properties.keys():
            print('Offer "' + FC.GREEN + offer_title + FC.RESET + '" title properties:')
            title_length = len(offer_title)
            print("Title length: " + FC.BLUE + str(title_length) + FC.RESET)
            for site, limits in self.title_boundaries.items():
                print("For " + FC.YELLOW + site + FC.RESET + ": ", end="")
                if limits["min"] <= title_length <= limits["max"]:
                    print(f"In bounds (between {limits['min']} and {limits['max']} characters)")
                else:
                    print(FC.RED + "Not in bounds" + FC.RESET)
                    print(f"Bounds for {site} are: min - {limits['min']}, max - {limits['max']}")
            print("")

    def check_description_lengths(self):
        for offer_title, offer_properties in self.offers_properties.items():
            print('Offer "' + FC.GREEN + offer_title + FC.RESET + '" description properties:')
            description_length = len(offer_properties["description"])
            print("Description length: " + FC.BLUE + str(description_length) + FC.RESET)
            for site, limits in self.description_boundaries.items():
                print(FC.YELLOW + site + FC.RESET + ": ", end="")
                if limits["min"] <= description_length <= limits["max"]:
                    print(f"In bounds (between {limits['min']} and {limits['max']} characters)")
                else:
                    print(FC.RED + "Not in bounds" + FC.RESET)
                    print(f"Bounds for {site} are: min - {limits['min']}, max - {limits['max']}")
            print("")

    def check_number_of_photos(self):
        for offer_title, offer_properties in self.offers_properties.items():
            print('Offer "' + FC.GREEN + offer_title + FC.RESET + '" photos properties:')
            number_of_photos = offer_properties["photos"]
            print("Number of photos: " + FC.BLUE + str(number_of_photos) + FC.RESET)
            for site, limits in self.number_of_photos_boundaries.items():
                print(FC.YELLOW + site + FC.RESET + ": ", end="")
                if limits["min"] <= number_of_photos <= limits["max"]:
                    print(f"In bounds (between {limits['min']} and {limits['max']} photos)")
                else:
                    print(FC.RED + "Not in bounds" + FC.RESET)
                    print(f"Bounds for {site} are: min - {limits['min']}, max - {limits['max']}")
            print("")

    def check_sexes(self):
        for offer_title, offer_properties in self.offers_properties.items():
            print('Offer "' + FC.GREEN + offer_title + FC.RESET + '" sex: ' + FC.BLUE + offer_properties["sex"]
                  + FC.RESET)
            if offer_properties["sex"] not in self.sexes:
                print(FC.RED + f"Wrong sex of the item ({offer_properties['sex']})! Expected sexes: {self.sexes}!"
                      + FC.RESET)
            print("")

    def check_prices(self):
        for offer_title, offer_properties in self.offers_properties.items():
            print('Offer "' + FC.GREEN + offer_title + FC.RESET + '" price: ' + FC.BLUE +
                  f'{offer_properties["price"]} PLN' + FC.RESET)
            if offer_properties["price"] < 0:
                print(FC.RED + f"Wrong price of the item ({offer_properties['price']})! "
                               f"Price should be positive, or 0!" + FC.RESET)
            print("")

    def check_conditions(self):
        for offer_title, offer_properties in self.offers_properties.items():
            print('Offer "' + FC.GREEN + offer_title + FC.RESET + '" sex: ' + FC.BLUE + offer_properties["condition"]
                  + FC.RESET)
            if offer_properties["condition"] not in self.conditions:
                print(FC.RED + f"Wrong condition of the item! Expected conditions: {self.conditions}!" + FC.RESET)
            print("")

    def check_package_sizes(self):
        for offer_title, offer_properties in self.offers_properties.items():
            print('Offer "' + FC.GREEN + offer_title + FC.RESET + '" sex: ' + FC.BLUE + offer_properties["package size"]
                  + FC.RESET)
            if offer_properties["package size"] not in self.package_sizes:
                print(FC.RED + f"Wrong package size! Expected package sizes: {self.package_sizes}!" + FC.RESET)
