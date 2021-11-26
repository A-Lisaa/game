"""
List of items inheriting from ItemMedicine
"""
from class_item_medicine import ItemMedicine, ItemMedicineEffect

# Food
bread = ItemMedicine("Bread", "Just a regular bread, heals 20 hp", ("gold", 5), (ItemMedicineEffect("health", 20, True),))
