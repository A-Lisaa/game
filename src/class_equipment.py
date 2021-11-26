import attr


@attr.s
class EquipmentData:
    helmet: object = attr.ib(default=None) # TODO: Make a class for equipment, default should be an equipment of Equipment instance with no buffs, maybe


class Equipment(EquipmentData):
    pass
