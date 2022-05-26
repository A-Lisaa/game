import attr
from constants import INDOORS_LOCATIONS


@attr.define
class Location:
    name: str
    _type: str

    def is_indoors(self):
        if self._type in INDOORS_LOCATIONS:
            return True
        return False
