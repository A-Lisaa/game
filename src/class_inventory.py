import attr
from logger import get_logger


@attr.s
class InventoryData:
    items: dict[object, int] = attr.ib(default={})


class Inventory(InventoryData):
    def __init__(self):
        super().__init__()
        self.log = get_logger(__file__)

    def add_item(self, item: object, amount: int):
        if item not in self.items:
            self.items[item] = amount
        else:
            self.items[item] += amount

        self.log.debug("Added %i of %s. Total amount: %i", amount, item, self.items[item])

    def remove_item(self, item: object, amount: int):
        if item in self.items:
            # TODO: Doesn't work correctly, same problem as in ItemMedicine, goes to negative numbers
            self.items[item] -= amount
        else:
            print(f"No item {item.name} in inventory")
            return 0

        self.log.debug("Removed %i of %s. Total amount: %i", amount, item, self.items[item])

        if self.items[item] == 0:
            self.items.pop(item)

    def show(self):
        print(self.items)

    def use_item(self, target: object, item: object, amount: int):
        for _ in range(amount):
            item.use(target)
        self.log.debug("Used %i of %s on %s", amount, item, target)
        self.remove_item(item, amount)
