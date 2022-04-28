import os
import json

OFFERS_FOLDER_NAME = "offers_to_post"
NAMES_OF_FILES_AND_FOLDERS = ["photos", "properties.json"]
MANDATORY_PROPERTIES = ["title", "description", "category", "condition", "size", "sex", "price", "brand", "colors", "package size"]
IMAGE_EXTENSIONS = ["jpeg", "png"]
SEXES = ["M", "K", "U"]
RED_COLOR = '\033[91m'
ENDC = '\033[0m'

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
        self.number_of_photos_boundaries = {"OLX": {"min": 1, "max": 8}, "Allegro Lokalnie": {"min": 1, "max": 15}, "Sprzedajemy": {"min": 1, "max": 12}, "Vinted": {"min": 1, "max": 20}}
    
    def add_offer_folders_with_photos(self, offer_list: list):
        folder_path = os.path.dirname(__file__) + "/"+ OFFERS_FOLDER_NAME + "/"
        os.mkdir(folder_path)
        for offer in offer_list:
            os.mkdir(folder_path + offer + "/")
            os.mkdir(folder_path + offer + "/" + "photos/")

    def add_properties_file_to_each_offer_folder(self):
        list_of_offers = [offer.path for offer in os.scandir(self.offers_folder_path) if offer.is_dir()]
        for offer_path in list_of_offers:
            if not os.path.exists(offer_path + "/properties.json"):
                with open(offer_path + "/properties.json", "w") as properties_file:
                    json.dump(self.json_data, properties_file)
    
    def print_bounds_for_title(self):
        print("Title limits [characters]:")
        for key, value in self.title_boundaries.items():
            print(f"{key}: min - " + str(value["min"]) + ", max - " + str(value["max"]))
        print("")

    def print_bounds_for_description(self):
        print("Description limits [characters]:")
        for key, value in self.description_boundaries.items():
            print(f"{key}: min - " + str(value["min"]) + ", max - " + str(value["max"]))
        print("")
    
    def print_photos_restrictions(self):
        print("Number of photos limits:")
        for key, value in self.number_of_photos_boundaries.items():
            print(f"{key}: min - " + str(value["min"]) + ", max - " + str(value["max"]))
        print("")
        print("Acceptable photos extensions:")
        for extension in IMAGE_EXTENSIONS:
            print(f"* {extension}")
        print("")

    def print_sexes_restrictions(self):
        print("Acceptable sexes marks:")
        for sex in SEXES:
            print(f"* {sex}")
        print("")

    def check_title_lengths(self):
        list_of_offers = [offer.path for offer in os.scandir(self.offers_folder_path) if offer.is_dir()]
        for offer_path in list_of_offers:
            with open(offer_path + "/properties.json", "r") as properties_file:
                properties_data = json.load(properties_file)
            print("Offer \"" + offer_path[offer_path.rfind("/") + 1:] + "\" title properties:")
            print("Title length: " + str(len(properties_data["title"])))
            for key, value in self.title_boundaries.items():
                print(key + ": ", end="")
                if value["min"] <= len(properties_data["title"]) <= value["max"]:
                    print("In bounds")
                else:
                    print(RED_COLOR + "Not in bounds" + ENDC)
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
                print(key + ": ", end="")
                if value["min"] <= len(properties_data["description"]) <= value["max"]:
                    print("In bounds")
                else:
                    print(RED_COLOR + "Not in bounds" + ENDC)
                    print("Bounds for " + key + " are: min - " + str(value["min"]) + ", max - " + str(value["max"]))
            print("")
    
    def check_number_of_photos_and_extension(self):
        list_of_offers = [offer.path for offer in os.scandir(self.offers_folder_path) if offer.is_dir()]
        for offer_path in list_of_offers:
            found_photos = os.listdir(offer_path + "/photos/")
            print("Offer \"" + offer_path[offer_path.rfind("/") + 1:] + "\" photos properties:")
            print("Number of photos: " + str(len(found_photos)))
            for key, value in self.number_of_photos_boundaries.items():
                print(key + ": ", end="")
                if value["min"] <= len(found_photos) <= value["max"]:
                    print("In bounds")
                else:
                    print(RED_COLOR + "Not in bounds" + ENDC)
                    print("Bounds for " + key + " are: min - " + str(value["min"]) + ", max - " + str(value["max"]))
            if any([not photo.endswith("." + IMAGE_EXTENSIONS[0]) or not photo.endswith("." + IMAGE_EXTENSIONS[0]) for photo in found_photos]):
                print(RED_COLOR + "Wrong extension of some of the photos! Check available photos extensions!" + ENDC)
            print("")

    def check_sex(self):
        list_of_offers = [offer.path for offer in os.scandir(self.offers_folder_path) if offer.is_dir()]
        for offer_path in list_of_offers:
            with open(offer_path + "/properties.json", "r") as properties_file:
                properties_data = json.load(properties_file)
            print("Offer \"" + offer_path[offer_path.rfind("/") + 1:] + "\" sex properties:")
            print("Sex of the item: " + properties_data["sex"])
            if properties_data["sex"] not in SEXES:
                print(RED_COLOR + "Wrong sex of the item!" + ENDC)
            print("")

    def check_price(self):
        list_of_offers = [offer.path for offer in os.scandir(self.offers_folder_path) if offer.is_dir()]
        for offer_path in list_of_offers:
            with open(offer_path + "/properties.json", "r") as properties_file:
                properties_data = json.load(properties_file)
            print("Offer \"" + offer_path[offer_path.rfind("/") + 1:] + "\" price properties:")
            print("Price of the item: " + str(properties_data["price"]))
            if properties_data["price"] < 0:
                print(RED_COLOR + "Wrong price of the item!" + ENDC)
            print("")

    def print_all_limitations(self):
        self.print_bounds_for_title()
        self.print_bounds_for_description()
        self.print_photos_restrictions()
        self.print_sexes_restrictions()

    def check_all_properties(self):
        self.check_title_lengths()
        self.check_description_lengths()
        self.check_number_of_photos_and_extension()
        self.check_sex()
        self.check_price()

if __name__ == "__main__":
    offer_poster = PostOffer()
    offer_poster.add_offer_folders_with_photos(["Sample offer 1", "Sample offer 2"])
    offer_poster.add_properties_file_to_each_offer_folder()
    offer_poster.print_all_limitations()
    offer_poster.check_all_properties()