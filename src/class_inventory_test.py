from class_character import Character
from class_inventory import Inventory
from class_item import ItemMedicine, ItemMedicineEffect

if __name__ == "__main__":
    sammy = Character("Samantha", (0, 165, 255), "../images/characters/", (0, 0))
    sammy.health -= 90
    print(sammy)
    bread = ItemMedicine("Bread", ("gold", 10), (ItemMedicineEffect("health", 20, True),))
    sammy.inventory = Inventory()
    print(sammy.inventory)
    sammy.inventory.add_item(bread, 10)
    print(sammy.inventory)
    sammy.inventory.show()
    sammy.inventory.remove_item(bread, 3)
    sammy.inventory.show()
    sammy.inventory.remove_item(bread, 7)
    sammy.inventory.show()
    print(sammy.inventory)
    sammy.inventory.add_item(bread, 2)
    sammy.inventory.show()
    sammy.inventory.use_item(sammy, bread, 1)
    print(sammy)
    sammy.inventory.show()
