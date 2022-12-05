import json
import os
from typing import List, Dict, Union

OFFERS_FOLDER_PATH = "\\offers_to_post"


class OffersDataHandler:
    def __init__(self):
        self.global_offers_path = os.path.dirname(__file__).replace("\\offers_data_handling", "") + OFFERS_FOLDER_PATH

    def get_offers_names(self) -> List[str]:
        return [offer.name for offer in os.scandir(self.global_offers_path) if offer.is_dir()]

    def get_global_photos_paths_from_single_offer_path(self) -> List[str]:
        pass

    def get_offer_properties(self, offer_name: str) -> Dict[str, Union[List[str], str, Dict[str, str]]]:
        offer_path = f"{self.global_offers_path}\\{offer_name}"
        photos_path = f"{offer_path}\\photos"
        offer_properties = {"title": offer_name,
                            "photos": [f"\\photos\\{photo.name}" for photo in os.scandir(photos_path)
                                       if not photo.is_dir()]}
        with open(f"{offer_path}\\properties.json", "r") as properties_file:
            properties_data = json.load(properties_file)
        offer_properties.update(properties_data)
        return offer_properties