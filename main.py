import os
import json

OFFERS_FOLDER_NAME = "offers_to_post"
NAMES_OF_FILES_AND_FOLDERS = ["photos", "properties.json"]
MANDATORY_PROPERTIES = ["title", "description", "category", "condition", "size", "sex", "price", "brand", "colors", "package size"]
IMAGE_FORMATS = ["jpeg", "png"]

class PostOffer:
    def __init__(self):
        self.offers_folder_path = os.path.dirname(__file__) + "/"+ OFFERS_FOLDER_NAME + "/"
        self.json_data = {
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
        self.title_boundaries = {"OLX": {"min": 16, "max": 70}, "Allegro Lokalnie": {"min": 1, "max": 50}, "Sprzedajemy": {"min": 3, "max": 60}, "Vinted": {"min": 5, "max": 100}}
        self.description_boundaries = {"OLX": {"min": 80, "max": 9000}, "Allegro Lokalnie": {"min": 1, "max": 3000}, "Sprzedajemy": {"min": 1, "max": 6000}, "Vinted": {"min": 5, "max": 3000}}

    def add_offer_folders_with_photos_and_properties(self, offer_list: list):
        folder_path = os.path.dirname(__file__) + "/"+ OFFERS_FOLDER_NAME + "/"
        for offer in offer_list:
            os.mkdir(folder_path + offer + "/")
            os.mkdir(folder_path + offer + "/" + "photos/")
        self.add_properties_file_to_each_offer_folder()

    def add_properties_file_to_each_offer_folder(self):
        list_of_offers = [offer.path for offer in os.scandir(self.offers_folder_path) if offer.is_dir()]
        for offer_path in list_of_offers:
            if not os.path.exists(offer_path + "/properties.json"):
                with open(offer_path + "/properties.json", "w") as properties_file:
                    json.dump(self.json_data, properties_file)
    
    def print_bounds_for_title(self):
        print("Title bounds [characters]:")
        for key, value in self.title_boundaries.items():
            print(key + ": min - " + str(value["min"]) + ", max - " + str(value["max"]))
        print("")

    def print_bounds_for_description(self):
        print("Description bounds [characters]:")
        for key, value in self.description_boundaries.items():
            print(key + ": min - " + str(value["min"]) + ", max - " + str(value["max"]))
        print("")

    def check_title_lengths(self):
        list_of_offers = [offer.path for offer in os.scandir(self.offers_folder_path) if offer.is_dir()]
        for offer_path in list_of_offers:
            with open(offer_path + "/properties.json", "r") as properties_file:
                properties_data = json.load(properties_file)
            print("Offer \"" + offer_path[offer_path.rfind("/") + 1:] + "\" title properties:")
            print("Title length: " + str(len(properties_data["title"])))
            for key, value in self.title_boundaries.items():
                print(key, end="")
                if value["min"] < len(properties_data["title"]) < value["max"]:
                    print(": In bounds")
                else:
                    print(": Not in bounds")
                    print("Bounds for " + key + " are: min - " + str(value["min"]) + ", max - " + str(value["max"]))
            print("")

    def check_description_lengths(self):
        list_of_offers = [offer.path for offer in os.scandir(self.offers_folder_path) if offer.is_dir()]
        for offer_path in list_of_offers:
            with open(offer_path + "/properties.json", "r") as properties_file:
                properties_data = json.load(properties_file)
            print("Offer \"" + offer_path[offer_path.rfind("/") + 1:] + "\" description properties:")
            print("Description length: " + str(len(properties_data["description"])))
            for key, value in self.description_boundaries.items():
                print(key, end="")
                if value["min"] < len(properties_data["description"]) < value["max"]:
                    print(": In bounds")
                else:
                    print(": Not in bounds")
                    print("Bounds for " + key + " are: min - " + str(value["min"]) + ", max - " + str(value["max"]))
            print("")

if __name__ == "__main__":
    offer_poster = PostOffer()
    offer_poster.add_offer_folders_with_photos_and_properties(["Sample offer 1", "Sample offer 2"])
    # offer_poster.add_properties_file_to_each_offer_folder()
    offer_poster.print_bounds_for_title()
    offer_poster.print_bounds_for_description()
    offer_poster.check_title_lengths()
    offer_poster.check_description_lengths()