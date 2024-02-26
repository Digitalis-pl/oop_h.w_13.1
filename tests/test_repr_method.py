from class_product import Product
from class_category import Category
from class_grass import Grass
from class_smartphone import Smartphone
from class_category_iteration import CategoryIteration


o = Category("w", "e", [1, 2, 3])
h = Product("a", "b", 20, 3)
s = Smartphone("s", "d", 22, 33, 55, 44, "c", "c")
g = Grass("n", "m", 66, 8, "v", 4, "b")
ca = CategoryIteration("Смартфоны")


def test_repr():
    assert repr(o) == "Category('w', 'e', [1, 2, 3], 3)"
    assert repr(h) == "Product('a', 'b', 20, 3, None)"
    assert repr(s) == "Smartphone('s', 'd', 22, 33, 'c', 55, 44, 'c')"
    assert repr(g) == "Grass('n', 'm', 66, 8, 'b', 'v', 4)"
    assert repr(ca) == "CategoryIteration(0, 'Смартфоны', [])"
