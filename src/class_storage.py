import attr
from logger import get_logger


@attr.s()
class StorageData:
    items: dict[object, int] = attr.ib(factory=dict)


class Storage(StorageData):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.log = get_logger(__file__)

    def set_item(self, item: object, amount: int = 1):
        self.items[item] = amount

    def add_item(self, item: object, amount: int = 1):
        """
        Adds an Item to a Storage

        Args:
            item (object): Item to add
            amount (int): amount of Item to add
        """
        if item not in self.items:
            self.items[item] = amount
        else:
            self.items[item] += amount

        self.log.debug("Added %i of %s. Total amount: %i", amount, item, self.items[item])

    def remove_item(self, item: object, amount: int = 1):
        """
        Removes an Item from a Storage

        Args:
            item (object): Item to remove
            amount (int): amount of Item to remove
        """
        if item in self.items:
            self.items[item] -= min(amount, self.items[item])
        else:
            print(f"No item {item.name} in Storage")
            return

        self.log.debug("Removed %i of %s. Total amount: %i", amount, item, self.items[item])

        if self.items[item] == 0:
            self.items.pop(item)
