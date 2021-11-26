import attr

from class_item import Item, ItemData
from class_character import Character


@attr.s(hash=True)
class ItemMedicineEffectData:
    name: str = attr.ib()
    strength: float | bool = attr.ib()
    added: bool = attr.ib()


class ItemMedicineEffect(ItemMedicineEffectData):
    pass


@attr.s(hash=True)
class ItemMedicineData(ItemData):
    effects: tuple[ItemMedicineEffect] = attr.ib()


class ItemMedicine(Item, ItemMedicineData):
    def use(self, character: Character):
        for effect in self.effects:
            if effect.added:
                current_character_stat = getattr(character, effect.name)
                final_character_stat = current_character_stat + effect.strength
                try:
                    max_character_stat = getattr(character, f"{effect.name}_max")
                    final_character_stat = min(final_character_stat, max_character_stat)
                except AttributeError:
                    pass
                setattr(character, effect.name, final_character_stat)
            else:
                setattr(character, effect.name, effect.strength)