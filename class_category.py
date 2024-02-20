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

    def __len__(self):
        return len(self.product)

    def __str__(self):
        return f"{self.name}, Остаток: {len(self.__product)}"

    @property
    def product(self):
        p_list = []
        for i in self.__product:
            p_list.append(str(i))
        return p_list

    @product.setter
    def product(self, object_product):
        self.__product.append(object_product)
