import json


class CateProd:

    def __init__(self, name, description):
        self.name = name
        self.description = description

    @staticmethod
    def open_json():
        with open("products.json", "r", encoding="utf-8") as f:
            category_list = json.loads(f.read())
            return category_list


class Category(CateProd):
    name: str
    description: str
    product: list
    all_category = 0
    unique_product = 0

    def __init__(self, name, description, product):
        super().__init__(name, description)
        self.__product = product
        Category.all_category += 1
        Category.unique_product += len(product)
        self.unique_product_in_category = len(product)

    @property
    def show_product(self, name):
        for i in self.__product:
            if i["name"] == name:
                return f'{i["name"]}, {i["count"]} руб. Остаток: {i["quantity"]}'

    @property
    def add_product(self):
        return self.__product

    @add_product.setter
    def add_product(self, dictionary):
        self.__product.append(Product.create_product(dictionary))


class Product(CateProd):
    name: str
    description: str
    prise: float
    count: int

    def __init__(self, name, description, prise, count):
        super().__init__(name, description)
        self.price = prise
        self.count = count

    @property
    def change_price(self):
        return self.price

    @change_price.setter
    def change_price(self, price):
        if price <= 0:
            print("некорректная цена")
            exit()
        if 0 < price < self.price:
            answer = input("are you sure: y/n")
            if answer == "y":
                self.price = price
            else:
                self.price = self.price

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
