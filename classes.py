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
    product: str
    all_category = 0
    unique_product = 0

    def __init__(self, name, description, product):
        super().__init__(name, description)
        self.product = product
        Category.all_category += 1
        Category.unique_product += len(product)
        self.unique_product_in_category = len(product)


class Product(CateProd):
    name: str
    description: str
    prise: float
    count: int

    def __init__(self, name, description, prise, count):
        super().__init__(name, description)
        self.price = prise
        self.count = count
