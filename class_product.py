class Product:
    name: str
    description: str
    prise: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

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
