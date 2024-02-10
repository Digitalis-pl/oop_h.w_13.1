class Category:
    name: str
    description: str
    product: str
    all_category: int
    unicue_product: int

    def __init__(self, name, description, product):
        self.name = name
        self.description = description
        self.product = product


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