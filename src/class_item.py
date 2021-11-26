from abc import ABC, abstractmethod

import attr


@attr.s(hash=True)
class ItemData:
    name: str = attr.ib()
    info: str = attr.ib()
    cost: tuple[str, int] | list[str, int] = attr.ib()


class Item(ABC):
    @abstractmethod
    def use(self):
        raise NotImplementedError
