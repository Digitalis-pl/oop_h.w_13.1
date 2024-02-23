from class_product import Product


class Smartphone(Product):
    efficiency: float
    model: str
    internal_memory: float
    colour: str

    def __init__(self, name, description, price, quantity,  efficiency, model, internal_memory, color):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.internal_memory = internal_memory
        self.color = color
