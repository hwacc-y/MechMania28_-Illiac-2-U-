from enum import Enum
from game.stat_set import StatSet

class ItemModel():
    def __init__(self, stat_set, item_timer, cost) -> None:
        self.stat_set = stat_set
        self.item_timer = item_timer
        self.cost = cost

class Item(Enum):
    PROCRUSTEAN_IRON = ItemModel(StatSet(0, 0, 0, 0), 1, 8)
    HEAVY_BROADSWORD = ItemModel(StatSet(0, 0, 0, 0), -1, 8)
    MAGIC_STAFF = ItemModel(StatSet(0, 0, 0, 0), 0, 8)
    STEEL_TIPPED_ARROW = ItemModel(StatSet(0, 0, 0, 0), 0, 8)
    ANEMOI_WINGS = ItemModel(StatSet(0, 0, 2, 0), -1, 8)
    HUNTER_SCOPE = ItemModel(StatSet(0, 0, 0, 2), -1, 8)
<<<<<<< HEAD
    RALLY_BANNER = ItemModel(StatSet(0, 2, 0, 0), -1, 8) # DO NOT USE 
    SHIELD = ItemModel(StatSet(0, 0, 0, 0), -1, 8) # Interesting 
    STRENGTH_POTION = ItemModel(StatSet(0, 4, 0, 0), 1, 5) # Not that Good 
    SPEED_POTION = ItemModel(StatSet(0, 0, 2, 0), 1, 5) # Not that Good 
    DEXTERITY_POTION = ItemModel(StatSet(0, 0, 0, 2), 1, 5) # Not that Good 
    NONE = ItemModel(StatSet(0, 0, 0, 0), -1, 100)
=======
    RALLY_BANNER = ItemModel(StatSet(0, 2, 0, 0), -1, 8)
    SHIELD = ItemModel(StatSet(0, 0, 0, 0), -1, 8)
    STRENGTH_POTION = ItemModel(StatSet(0, 4, 0, 0), 1, 5)
    SPEED_POTION = ItemModel(StatSet(0, 0, 2, 0), 1, 5)
    DEXTERITY_POTION = ItemModel(StatSet(0, 0, 0, 2), 1, 5)
    NONE = ItemModel(StatSet(0, 0, 0, 0), -1, 100)

>>>>>>> slink_up
