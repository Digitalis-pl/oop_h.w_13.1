from class_category import Category
from class_product import Product
from class_smartphone import Smartphone
from class_grass import Grass
from mixin_repr import MixinRepr
from class_category_iteration import CategoryIteration
from class_order import Order

order = Order("Samsung Galaxy C23 Ultra", 2)
order.choose_product()
order.count_total_sum()
print(order)
