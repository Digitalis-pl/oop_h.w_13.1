class MixinRepr:
    def __init__(self):
        self.__repr__()

    def __repr__(self):
        print(f"{self.__class__.__name__}{tuple(self.__dict__.values())}")
        return f"{self.__class__.__name__}{tuple(self.__dict__.values())}"
