import unittest

from class_character import Character
from list_item_medicine import *


class InventoryTests(unittest.TestCase):
    def test_add_item(self):
        sammy = Character("Samantha", (0, 165, 255), "../images/characters/test_character")

        sammy.inventory.add_item(bread, 10)

        self.assertEqual(sammy.inventory.items[bread], 10)

    def test_remove_item(self):
        sammy = Character("Samantha", (0, 165, 255), "../images/characters/test_character")

        sammy.inventory.add_item(bread, 5)
        sammy.inventory.remove_item(bread, 10)

        self.assertNotIn(bread, sammy.inventory.items)

    def test_show_info(self):
        sammy = Character("Samantha", (0, 165, 255), "../images/characters/test_character")

        sammy.inventory.add_item(bread, 15)
        self.assertEqual(bread.info, "Just a regular bread, heals 20 hp.")

if __name__ == "__main__":
    unittest.main()
