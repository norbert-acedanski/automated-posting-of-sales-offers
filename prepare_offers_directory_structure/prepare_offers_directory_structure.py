import json
import os
import random
import string

from common.common import OFFERS_FOLDER_PATH, PHOTOS, PROPERTIES_JSON


class PrepareOffersDirectoryStructure:
    def __init__(self):
        self.global_offers_path = os.path.dirname(__file__)[:os.path.dirname(__file__).rfind("\\")] + OFFERS_FOLDER_PATH
        self.json_data = {
            "description": "Description for an offer. In some cases (like OLX page), "
                           "the description has to be longer, than 80 characters.",
            "category": {"vinted": ["Correct", "category", "path", "for", "vinted"],
                         "olx": ["Correct", "category", "path", "for", "olx"]},
            "condition": "fine/good/very good/new without a tag/new with a tag",
            "size": "XS/S/M/L/XL/XXL/30/45 etc.",
            "sex": "M/K/U (M - Man, K - Woman, U - Universal)",
            "price": 10,
            "brand": "Adidas/Champion/House Brand/None",
            "colors": ["Czarny", "Biały", "maximum of two colors in this list, "
                                          "with the most important as the first element - should be in polish"],
            "material": "Bawełna/Akryl etc. - in polish",
            "package size": "S/M/L (S - small, M - medium, L - large)"
        }

    def add_offers_directories_with_photos_folders(self, number_of_offers: int):
        try:
            os.mkdir(self.global_offers_path)
        except FileExistsError:
            print("No need to create 'offers_to_post' directory, skipping...")
        random_string = "".join(random.choices(string.ascii_letters + string.digits, k=10))
        for offer_number in range(1, number_of_offers + 1):
            os.mkdir(self.global_offers_path + f"/Offer {random_string} {offer_number}/")
            os.mkdir(self.global_offers_path + f"/Offer {random_string} {offer_number}/{PHOTOS}/")

    def add_properties_file_to_each_offer_directory(self):
        list_of_offers = [offer.path for offer in os.scandir(self.global_offers_path) if offer.is_dir()]
        for offer_path in list_of_offers:
            if not os.path.exists(offer_path + f"/{PROPERTIES_JSON}"):
                with open(offer_path + f"/{PROPERTIES_JSON}", "w") as properties_file:
                    json.dump(self.json_data, properties_file, indent=4)
