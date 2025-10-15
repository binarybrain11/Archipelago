from BaseClasses import ItemClassification
from .data.items import all_item_names, major_item_names


class ItemData:
    name: str
    classification: ItemClassification
    id: int

    def __init__(self, name: str, classification: ItemClassification, id: int):
        self.name = name
        self.classification = classification
        self.id = id

    def __repr__(self):
        return self.name

item_table: dict[str, ItemData] = dict()

for index, item in enumerate(all_item_names):
    classification = ItemClassification.progression if item in major_item_names else ItemClassification.filler
    item_table[item] = ItemData(item, classification, index + 1)

valid_item_names = [*all_item_names, "Zodiac Stones"]