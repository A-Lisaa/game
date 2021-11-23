from class_character import Character


if __name__ == "__main__":
    sammy = Character("Samantha", (0, 165, 255), "../images/characters/", (0, 0))
    print(sammy)
    sammy.money.gold += 1000
    print(sammy)
    sammy.money.platinum = 500
    print(sammy)
    sammy.money.convert("gold", "silver", 250, 3)
    print(sammy)
