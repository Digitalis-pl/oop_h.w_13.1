from class_product import Product
from class_all_product import AllProductClass
from mixin_repr import MixinRepr


class Smartphone(Product, AllProductClass, MixinRepr):
    efficiency: float
    model: str
    internal_memory: float
    colour: str

    def __init__(self, name, description, price, quantity,  efficiency, model, internal_memory, color):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.internal_memory = internal_memory
        self.color = color
        super().__repr__()

    def __str__(self):
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity}"

    def __add__(self, other):
        if not isinstance(other, Smartphone):
            raise ValueError('Складывать можно только объекты Product и дочерние от них.')
        if type(self) == type(other):
            self.total_sum = self.quantity * self.price
            other.total_sum = other.quantity * other.price
            return self.total_sum + other.total_sum
        else:
            raise TypeError

    @property
    def price(self):
        return self.price

    @price.setter
    def price(self, price):
        if price <= 0:
            print("некорректная цена")
        if 0 < price < self.price:
            answer = input("are you sure: y/n")
            if answer == "y":
                self.price = price

    @classmethod
    def create_product(cls, dictionary, list_p):
        new = cls(**dictionary)
        for i in list_p:
            if new.name == i.name:
                new.quantity += i.quantity
                if new.price < i.price:
                    new.price = i.price
        return new

    def __len__(self):
        return len(Product.all_product)
