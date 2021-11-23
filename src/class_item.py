from abc import ABC, abstractmethod

import attr

from class_character import Character


@attr.s(hash=True)
class ItemData:
    name: str = attr.ib()
    cost: tuple[str, int] | list[str, int] = attr.ib()


@attr.s(hash=True)
class ItemMedicineEffectData:
    name: str = attr.ib()
    strength: float | bool | int | str = attr.ib()
    added: bool = attr.ib()


class ItemMedicineEffect(ItemMedicineEffectData):
    pass


@attr.s(hash=True)
class ItemMedicineData(ItemData):
    effects: tuple[ItemMedicineEffect] | list[ItemMedicineEffect] = attr.ib()


class Item(ABC):
    @abstractmethod
    def use(self):
        raise NotImplementedError


class ItemMedicine(Item, ItemMedicineData):
    def use(self, character: Character):
        for effect in self.effects:
            if effect.added:
                # TODO: Still doesn't work
                final_character_effect_value = getattr(character, effect.name) + effect.strength
                # try:
                #     effect_max = getattr(character, f"{effect.name}_max")
                #     setattr(character, effect.name, effect_max % final_character_effect_value)
                # except AttributeError:
                setattr(character, effect.name, final_character_effect_value)
            else:
                setattr(character, effect.name, effect.strength)
