from class_item_equipment import ItemEquipment
from class_effect import Effect

# Default set (no armor)
default_head = ItemEquipment("No Helmet", "No Helmet", ("gold", 0), "helmet",  "head", (Effect("head_protection", 0),))

# Iron set
iron_helmet = ItemEquipment("Iron Helmet", "A regular iron helmet, gives small protection", ("gold", 100), "helmet", "head", (Effect("head_protection", 5),))
iron_chestplate = ItemEquipment("Iron Chestplate", "A regular iron chestplate, gives small protection", ("gold", 150), "chestplate", "body", (Effect("body_protection", 8),))

# Steel set
steel_helmet = ItemEquipment("Steel Helmet", "A regular steel helmet, gives moderate protection", ("gold", 200), "helmet", "head", (Effect("head_protection", 10),))
