import attr

from class_item import Item
from class_character import Character
from class_effect import Effect
from IUsable import IUsable


@attr.s(hash=True)
class ItemMedicine(Item, IUsable):
    effects: tuple[Effect] = attr.ib()

    def context_menu(self):
        # Example:
        # 1 - Use item
        # 2 - Info
        # 3 - Drop
        pass

    def use(self, character: Character):
        for effect in self.effects:
            if effect.added:
                current_character_stat = getattr(character, effect.stat)
                final_character_stat = current_character_stat + effect.strength
                try:
                    max_character_stat = getattr(character, f"{effect.stat}_max")
                    final_character_stat = min(final_character_stat, max_character_stat)
                except AttributeError:
                    pass
                setattr(character, effect.stat, final_character_stat)
            else:
                setattr(character, effect.stat, effect.strength)