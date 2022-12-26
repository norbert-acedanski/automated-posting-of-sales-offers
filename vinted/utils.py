import json
from typing import Dict, List, Union


def _open_json_file(file_name: str) -> Union[List[int], Dict[str, Union[str, Dict[str, dict]]]]:
    with open(file_name, "r") as file:
        data = json.load(file)
    return data


def choose_categories() -> None:
    categories = _open_json_file("./vinted_categories.json")
    current_categories = list(categories.keys())
    children = categories
    tree_of_categories = []

    def _print_current_categories(_current_categories: List[str]) -> None:
        for category_index, category in enumerate(_current_categories, 1):
            print(f"{category_index}. {category}")
    while children is not None:
        print("\nCurrent categories:")
        _print_current_categories(current_categories)
        chosen_category_index = int(input("Select category number: ")) - 1
        chosen_category = current_categories[chosen_category_index]
        tree_of_categories.append(chosen_category)
        children = children[chosen_category]
        current_categories = list(children.keys()) if children is not None else None
    print("\nTree of categories:")
    _print_current_categories(tree_of_categories)
    print(tree_of_categories)


def print_vinted_colors() -> None:
    colors = _open_json_file("./vinted_colors.json")
    print("Vinted colors list:")
    for color in colors:
        print(color)
    print()


if __name__ == "__main__":
    print_vinted_colors()
    choose_categories()
