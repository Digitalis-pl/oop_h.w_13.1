class Category:
    name: str
    description: str
    product: str

    def __init__(self, name, description, product, all_category, unicue_product):
        self.name = name
        self.description = description
        self.product = product
        self.all_category = all_category
        self.unicue_product = unicue_product


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