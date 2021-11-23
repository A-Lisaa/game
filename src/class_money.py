import attr


@attr.s
class MoneyData:
    silver: int = attr.ib(default=0)
    gold: int = attr.ib(default=0)
    platinum: int = attr.ib(default=0)

class Money(MoneyData):
    def convert(self, input_currency: str, output_currency: str, amount: int, exchange_rate: float):
        setattr(self, input_currency, getattr(self, input_currency)-amount)
        setattr(self, output_currency, getattr(self, output_currency) + amount*exchange_rate)
