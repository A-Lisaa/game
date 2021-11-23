from class_character import Character
from class_item import ItemMedicine, ItemMedicineEffect


if __name__ == "__main__":
    sammy = Character("Samantha", (0, 165, 255), "../images/characters/", (0, 0))
    print(sammy)
    bread = ItemMedicine("Bread", ("gold", 20),
                        (ItemMedicineEffect("health", 50, True),
                        ItemMedicineEffect("poison", 0, 0)))
    print(bread)
    sammy.health -= 20
    sammy.poison = True
    print(sammy)
    bread.use(sammy)
    print(sammy)
