class MixinRepr:
    def __repr__(self):
        return f"{self.__class__.__name__}{tuple(self.__dict__.values())}"
