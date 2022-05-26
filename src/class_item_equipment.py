import attr

from class_item import Item
from class_effect import Effect


@attr.s(hash=True)
class ItemEquipment(Item):
    armor_type: str = attr.ib()
    slot: str = attr.ib()
    buffs: tuple[Effect] = attr.ib()

    def context_menu(self):
        # Example:
        # 1 - Equip/Unequip
        # 2 - Info
        # 3 - Drop
        pass
