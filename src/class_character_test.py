import unittest

from class_character import Character
from list_item_medicine import *


class CharacterTests(unittest.TestCase):
    def test_create_character(self):
        characters = []
        sammy = Character("Sammy", (0, 0, 0), "../images/characters/test_character/")
        semen = Character("Semen", (255, 255, 255), "../images/characters/test_character/")

        characters.append(sammy)
        sammy.inventory.add_item(bread, 1488)
        characters.append(semen)
        semen.inventory.add_item(bread, 666)

        self.assertIn(sammy, characters)
        self.assertIn(semen, characters)

if __name__ == "__main__":
    unittest.main()
