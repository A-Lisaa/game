import unittest

from class_character import Character
from list_item_equipment import *


class EquipmentTest(unittest.TestCase):
    def test_equip(self):
        sammy = Character("Samantha", (0, 165, 255), "../images/characters/test_character")

        sammy.equip(iron_helmet)

        self.assertEqual(sammy.equipment["head"], iron_helmet)

    def test_unequip(self):
        sammy = Character("Samantha", (0, 165, 255), "../images/characters/test_character")

        sammy.equip(iron_helmet)
        sammy.equip(iron_chestplate)
        sammy.unequip(iron_helmet)

        self.assertEqual(sammy.equipment["head"], default_head)

if __name__ == "__main__":
    unittest.main()
