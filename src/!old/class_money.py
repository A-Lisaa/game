import attr
from logger import get_logger

@attr.s
class MoneyData:
    cash: dict[str, float] = attr.ib(factory=dict)

class Money(MoneyData):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.log = get_logger(__file__)

    def set_money(self, currency: str, amount: float):
        if amount < 0:
            raise ValueError("Money can't be set below 0")
        self.cash[currency] = amount

    # TODO: Just one function for addition and subtraction, maybe also for setting
    def change_money(self, currency: str, amount: float):
        if currency not in self.cash:
            self.cash[currency] = amount
        else:
            self.cash[currency] += amount

        

    def add_money(self, currency: str, amount: float):
        if amount < 0:
            self.remove_money(currency, abs(amount))
            return
        if currency not in self.cash:
            self.cash[currency] = amount
        else:
            self.cash[currency] += amount

        self.log.debug("Added %i of %s. Total amount: %i", amount, currency, self.cash[currency])

    def remove_money(self, currency: str, amount: float):
        if amount < 0:
            self.add_money(currency, abs(amount))
            return
        if currency in self.cash:
            self.cash[currency] -= min(amount, self.cash[currency])
        else:
            print(f"No currency {currency} in Storage")
            return

        self.log.debug("Removed %i of %s. Total amount: %i", amount, currency, self.cash[currency])

    def convert(self, input_currency: str, output_currency: str, amount: int, exchange_rate: float):
        setattr(self, input_currency, getattr(self, input_currency) - amount)
        setattr(self, output_currency, getattr(self, output_currency) + amount*exchange_rate)
