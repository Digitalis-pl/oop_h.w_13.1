from function import create_instance, open_json


class Order:
    order_id: int

    def __init__(self, product_name, product_quantity):
        self.product_name = product_name
        self.product_quantity = product_quantity
        self.total = 0
        self.chosen = None
        super().__repr__()

    def choose_product(self):
        for i in create_instance(open_json())[2]:
            if self.product_name == i.name:
                self.chosen = i
                return self.chosen

    def count_total_sum(self):
        self.total = self.product_quantity * self.chosen.price
        return self.total

    def __str__(self):
        return f"ваш заказ: {self.product_name}, кол-во: {self.product_quantity}, итог: {self.total}"
