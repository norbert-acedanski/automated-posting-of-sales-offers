import json
import os
from typing import List, Dict, Union

from common.common import OFFERS_FOLDER_NAME, PHOTOS, PROPERTIES_JSON


class OffersDataCollector:
    def __init__(self):
        self.global_offers_path = os.path.join(os.path.split(os.path.dirname(__file__))[0], OFFERS_FOLDER_NAME)

    def get_offers_names(self) -> List[str]:
        return [offer.name for offer in os.scandir(self.global_offers_path) if offer.is_dir()]

    def get_offer_properties(self, offer_name: str) -> Dict[str,
                                                            Union[List[str], str, int, float, Dict[str, List[str]]]]:
        offer_path = os.path.join(self.global_offers_path, offer_name)
        photos_path = os.path.join(offer_path, PHOTOS)
        offer_properties = {"title": offer_name,
                            "photos": [os.path.join(photos_path, photo.name) for photo in os.scandir(photos_path)
                                       if not photo.is_dir()]}
        with open(os.path.join(offer_path, PROPERTIES_JSON), "r", encoding="utf-8") as properties_file:
            properties_data = json.load(properties_file)
        offer_properties.update(properties_data)
        return offer_properties
