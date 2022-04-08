import os
import json
import pytest
import shutil

OFFERS_FOLDER_NAME = "offers_to_post"
NAMES_OF_FILES_AND_FOLDERS = ["photos", "properties.json"]
MANDATORY_PROPERTIES = ["title", "description", "size", "price", "brand", "colors"]
IMAGE_FORMATS = ["jpeg", "png"]


def test_all_subfolders_and_files():
    folder_path = os.path.dirname(os.path.dirname(__file__)) + "/"+ OFFERS_FOLDER_NAME + "/"
    assert os.path.isdir(folder_path)
    ############################################################################
    sample_offer_path = folder_path + "example/"
    os.mkdir(sample_offer_path)
    photos_path = sample_offer_path + "photos/"
    os.mkdir(photos_path)
    with open(OFFERS_FOLDER_NAME + "/example/photos/sample_photo_1.png", "w") as photo_1, open(OFFERS_FOLDER_NAME + "/example/photos/sample_photo_2.jpeg", "w") as photo_2:
        pass
    json_data = {
                 "title": "Sample Title",
                 "description": "Description",
                 "size": "M",
                 "price": 10,
                 "brand": "None",
                 "colors": ["black", "white"]
                }
    with open(sample_offer_path + "properties.json", "w") as properties_file:
        json.dump(json_data, properties_file)
    ############################################################################
    list_of_offers = os.listdir(folder_path)
    assert len(list_of_offers) > 0
    for offer in list_of_offers:
        current_offer_path = folder_path + offer + "/"
        files_in_current_offer = os.listdir(current_offer_path)
        assert len(files_in_current_offer) == len(NAMES_OF_FILES_AND_FOLDERS)
        for name in NAMES_OF_FILES_AND_FOLDERS:
            assert name in files_in_current_offer
        photos_path = current_offer_path + NAMES_OF_FILES_AND_FOLDERS[0] + "/"
        files_in_photo_directory = [file for file in os.listdir(photos_path) if file.endswith("." + IMAGE_FORMATS[0]) or file.endswith("." + IMAGE_FORMATS[1])]
        number_of_photos = len(files_in_photo_directory)
        assert number_of_photos > 0 and number_of_photos < 9
        with open(current_offer_path + NAMES_OF_FILES_AND_FOLDERS[1], "r") as json_file:
            try:
                json_data = json.load(json_file)
            except json.JSONDecodeError:
                assert False
        assert len(json_data) == len(MANDATORY_PROPERTIES)
        for iterable, (key, value) in enumerate(json_data.items()):
            assert key in MANDATORY_PROPERTIES
        # assert len(json_data[MANDATORY_PROPERTIES[0]]) > 16
        # assert len(json_data[MANDATORY_PROPERTIES[1]]) > 80
        ############################################################################
        shutil.rmtree(sample_offer_path)
        ############################################################################