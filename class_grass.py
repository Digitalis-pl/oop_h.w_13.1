from class_product import Product


class Grass(Product):
    country: str
    term: int
    colour: str

    def __init__(self, name, description, price, quantity,  country, term, color):
        super().__init__(name, description, price, quantity, color)
        self.country = country
        self.term = term
