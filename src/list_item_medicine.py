"""
List of items inheriting from ItemMedicine
"""
from class_item_medicine import ItemMedicine
from class_effect import Effect


# Food
bread = ItemMedicine("Bread", "Just a regular bread, heals 20 hp.", ("gold", 5), (Effect("health", 20),))
