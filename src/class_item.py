from abc import ABC, abstractmethod

import attr


@attr.s(hash=True)
class Item(ABC):
    name: str = attr.ib()
    info: str = attr.ib()
    cost: tuple[str, int] = attr.ib()

    # @property
    # def info(self):
    #     return f"{self._info}. Cost is {self.cost[1]} {self.cost[0]}."

    # @info.setter
    # def info(self, value: str):
    #     self._info = value

    @abstractmethod
    def context_menu(self):
        raise NotImplementedError
