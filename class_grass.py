from class_product import Product
from class_all_product import AllProductClass


class Grass(AllProductClass, Product):
    country: str
    term: int
    colour: str

    def __init__(self, name, description, price, quantity,  country, term, color):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.term = term
        self.color = color
