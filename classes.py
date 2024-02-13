

class Category:
    name: str
    description: str
    product: str
    all_category = 0
    unicue_product = 0

    def __init__(self, name, description, product):
        self.name = name
        self.description = description
        self.product = product
        Category.all_category += 1
        Category.unicue_product += len(product)
        self.unicue_product_in_category = len((product))


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