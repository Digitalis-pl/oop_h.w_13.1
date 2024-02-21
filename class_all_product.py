from abc import ABC, abstractmethod


class AllProductClass(ABC):

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def create_product(self):
        pass

    @abstractmethod
    def price(self):
        pass

    @abstractmethod
    def __add__(self):
        pass

    @abstractmethod
    def __str__(self):
        pass
