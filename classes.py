import json


def open_json():
    with open("products.json", "r", encoding="utf-8") as f:
        category_list = json.loads(f.read())
        return category_list


class Category:
    name: str
    description: str
    product: list
    all_category = 0
    unique_product = 0

    def __init__(self, name, description, product):
        self.name = name
        self.description = description
        self.__product = product
        Category.all_category += 1
        Category.unique_product += len(product)
        self.unique_product_in_category = len(product)

    @property
    def show_product(self):
        p_list = []
        for i in self.__product:
            p_list.append(f'{i.name}, {i._Product__price} руб. Остаток: {i.quantity}')
        return "[%s]" % ",\n ".join(map(str, p_list))

    @property
    def add_product(self):
        return self.__product

    @add_product.setter
    def add_product(self, object_product):
        self.__product.append(object_product)


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
       # obj = list(dictionary.values())
        new = cls(**dictionary)
        for i in list_p:
            if new.name == i.name:
                new.quantity += i.quantity
                if new.__price < i.__price:
                    new.__price = i.__price
        return new
