from abc import ABC, abstractmethod


class IUsable(ABC):
    @abstractmethod
    def use(self):
        raise NotImplementedError