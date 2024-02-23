from class_product import Product
from class_all_product import AllProductClass
from mixin_repr import MixinRepr


class Grass(Product, AllProductClass, MixinRepr):
    country: str
    term: int
    colour: str

    def __init__(self, name, description, price, quantity,  country, term, color):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.term = term
        self.color = color

    def __str__(self):
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity}"

    def __add__(self, other):
        if not isinstance(other, Grass):
            raise ValueError('Складывать можно только объекты Product и дочерние от них.')
        if type(self) == type(other):
            self.total_sum = self.quantity * self.__price
            other.total_sum = other.quantity * other.__price
            return self.total_sum + other.total_sum
        else:
            raise TypeError

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        if price <= 0:
            print("некорректная цена")
        if 0 < price < self.__price:
            answer = input("are you sure: y/n")
            if answer == "y":
                self.__price = price

    @classmethod
    def create_product(cls, dictionary, list_p):
        new = cls(**dictionary)
        for i in list_p:
            if new.name == i.name:
                new.quantity += i.quantity
                if new.__price < i.__price:
                    new.__price = i.__price
        return new

    def __len__(self):
        return len(Product.all_product)
