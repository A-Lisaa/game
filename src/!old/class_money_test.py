import unittest

from class_character import Character


class MoneyTests(unittest.TestCase):
    def test_set_money(self):
        sammy = Character("Samantha", (0, 165, 255), "../images/characters/test_character")

        sammy.money.set_money("gold", 1488)

        self.assertEqual(sammy.money.cash["gold"], 1488)

    def test_add_money(self):
        sammy = Character("Samantha", (0, 165, 255), "../images/characters/test_character")

        sammy.money.add_money("gold", 1000)

        self.assertEqual(sammy.money.cash["gold"], 1000)

    def test_remove_money(self):
        sammy = Character("Samantha", (0, 165, 255), "../images/characters/test_character")

        sammy.money.set_money("gold", 500)
        sammy.money.remove_money("gold", 1000)

        self.assertEqual(sammy.money.cash["gold"], 0)

if __name__ == "__main__":
    unittest.main()
