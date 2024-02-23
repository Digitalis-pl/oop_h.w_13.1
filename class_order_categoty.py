from abc import ABC, abstractmethod


class OrderCategory(ABC):

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def __str__(self):
        pass
