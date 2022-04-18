import os
import json

OFFERS_FOLDER_NAME = "offers_to_post"
NAMES_OF_FILES_AND_FOLDERS = ["photos", "properties.json"]
MANDATORY_PROPERTIES = ["title", "description", "category", "condition", "size", "sex", "price", "brand", "colors", "package size"]
IMAGE_FORMATS = ["jpeg", "png"]

class PostOffer:
    def __init__(self):
        self.offers_folder_path = os.path.dirname(__file__) + "/"+ OFFERS_FOLDER_NAME + "/"

    def add_properties_file_to_each_offer_folder(self):
        list_of_offers = [offer.path for offer in os.scandir(self.offers_folder_path) if offer.is_dir()]
        json_data = {
                 "title": "Offer title. In case of OLX - title should be longer, than 16 characters.",
                 "description": "Description for an offer. In some cases (like OLX page), the description has to be longer, than 80 characters.",
                 "category": "Category, like Czapka zimowa/Koszule/Spodnie jeansowe etc.",
                 "condition": "fine/good/very good/new without a tag/new with a tag",
                 "size": "XS/S/M/L/XL/XXL/30/45 etc.",
                 "sex": "M/K/U (M - Man, K - Woman, U - Universal)",
                 "price": 10,
                 "brand": "Adidas/Champion/House Brand/None",
                 "colors": ["black", "white", "maximum of two colors in this list, with the most important as the first element"],
                 "package size": "S/M/L (S - small, M - medium, L - large)"
                }
        for offer_path in list_of_offers:
            with open(offer_path + "/properties.json", "w") as properties_file:
                json.dump(json_data, properties_file)

if __name__ == "__main__":
    offer_poster = PostOffer()
    offer_poster.add_properties_file_to_each_offer_folder()