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
            p_list.append(f'{i.name}, {i.price} руб. Остаток: {i.count}')
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
    count: int

    def __init__(self, name, description, prise, count):
        self.name = name
        self.description = description
        self.price = prise
        self.count = count

    @property
    def product_price(self):
        return self.price

    @product_price.setter
    def product_price(self, price):
        if price <= 0:
            print("некорректная цена")
        if 0 < price < self.price:
            answer = input("are you sure: y/n")
            if answer == "y":
                self.price = price

    @classmethod
    def create_product(cls, dictionary, list_p):
        obj = list(dictionary.values())
        new = cls(name=obj[0], description=obj[1], prise=obj[2], count=obj[3])
        for i in list_p:
            if new.name == i.name:
                new.count += i.count
                if new.price < i.price:
                    new.price = i.price
        return new
