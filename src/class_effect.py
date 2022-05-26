import attr


@attr.s(hash=True)
class Effect:
    stat: str = attr.ib()
    strength: float | bool = attr.ib()
    added: bool = attr.ib(default=True)
