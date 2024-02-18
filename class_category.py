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

    def show_product(self):
        p_list = []
        for i in self.__product:
            p_list.append(f'{i.name}, {i.price} руб. Остаток: {i.quantity}')
        return p_list

    @property
    def __product(self):
        return self.__product

    @__product.setter
    def __product(self, object_product):
        self.__product.append(object_product)
