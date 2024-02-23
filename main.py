from class_category import Category
from class_product import Product
from class_smartphone import Smartphone
from class_grass import Grass
from mixin_repr import MixinRepr
from class_category_iteration import CategoryIteration


c = Category("w", "e", [1, 2, 3])
p = Product("a", "b", 20, 3)
s = Smartphone("s", "d", 22, 33, 55, 44, "c", "c")
g = Grass("n", "m", 66, 8, "v", 4, "b")
ca = CategoryIteration("Смартфоны")


print(repr(c))
print(repr(p))
print(repr(s))
print(repr(g))
print(repr(ca))