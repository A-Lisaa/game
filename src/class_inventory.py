import attr
from logger import get_logger

from class_storage import Storage


class Inventory(Storage):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.log = get_logger(__file__)

    def use_item(self, target: object, item: object, amount: int = 1):
        """
        Uses amount of Item on target

        Args:
            target (object): object to use an Item on
            item (object): Item to use
            amount (int): amount of Item to use, Defaults to 1
        """
        if item not in self.items:
            print(f"No item {item}")
            return
        for i in range(amount):
            if self.items[item] >= 1:
                item.use(target)
            else:
                break
        self.log.debug("Used %i of %s on %s", i+1, item, target)
        self.remove_item(item, amount)

    def show(self):
        print(self.items)
