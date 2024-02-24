from class_product import Product
from class_smartphone import Smartphone
from class_grass import Grass
from mixin_repr import MixinRepr


class Category(MixinRepr):
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
        super().__repr__()

    def __len__(self):
        return len(self.product)

    def __str__(self):
        return f"{self.name}, Остаток: {len(self.__product)}"

    @property
    def product(self):
        p_list = []
        for i in self.__product:
            if isinstance(i, (Product, Grass, Smartphone)):
                p_list.append(str(i))
            else:
                raise TypeError
        return p_list

    @product.setter
    def product(self, object_product):
        if isinstance(object_product, (Product, Grass, Smartphone)):
            self.__product.append(object_product)
            Category.unique_product += 1
        else:
            raise TypeError
