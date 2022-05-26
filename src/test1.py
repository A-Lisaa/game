class IUsable:
    pass

class BaseClass:
    pass

class Usable(BaseClass, IUsable):
    pass


u = Usable()
print(bool(isinstance(u, IUsable)))