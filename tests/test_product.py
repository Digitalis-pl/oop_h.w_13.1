import pytest
from function import open_json, create_instance
from class_product import Product
from class_category import Category


prod_list = open_json()
common_list = create_instance(prod_list)


@pytest.fixture
def product_toster():
    return Product("toster", "fry our bread", 6500.50, 20000)


def test_init(product_toster):
    assert product_toster.name == "toster"
    assert product_toster.description == "fry our bread"
    assert product_toster.price == 6500.50
    assert product_toster.quantity == 20000


d = {
        "name": "55\" QLED 4K",
        "description": "Фоновая подсветка",
        "price": 123000.0,
        "quantity": 7
      }

m = {
        "name": "Xiaomi Redmi Note 11",
        "description": "1024GB, Синий",
        "price": 31000.0,
        "quantity": 14
      }

m_p = {
        "name": "Xiaomi Redmi Note 11",
        "description": "1024GB, Синий",
        "price": 31100.0,
        "quantity": 14
      }


def test_create_product():
    assert Product.create_product(d, common_list[1][0])
    assert Product.create_product(d, common_list[1][0]).description == "Фоновая подсветка"
    assert Product.create_product(d, common_list[1][0]).quantity == 7
    assert Product.create_product(d, common_list[1][0]).price == 123000.0
    assert Product.create_product(d, common_list[1][0]).name == "55\" QLED 4K"
    assert Product.create_product(m, common_list[1][0])
    assert Product.create_product(m, common_list[1][0]).quantity == 28
    assert Product.create_product(m, common_list[1][0]).name == "Xiaomi Redmi Note 11"
    assert Product.create_product(m, common_list[1][0]).price == 31000.0
    assert Product.create_product(m, common_list[1][0]).description == "1024GB, Синий"
    assert Product.create_product(m_p, common_list[1][0])
    assert Product.create_product(m_p, common_list[1][0]).quantity == 28
    assert Product.create_product(m_p, common_list[1][0]).name == "Xiaomi Redmi Note 11"
    assert Product.create_product(m_p, common_list[1][0]).price == 31100.0
    assert Product.create_product(m_p, common_list[1][0]).description == "1024GB, Синий"


def test_show_product():
    assert common_list[0][0].product == ["Samsung Galaxy C23 Ultra, 180000.0 руб. Остаток: 5",
                                         "Iphone 15, 210000.0 руб. Остаток: 8",
                                         "Xiaomi Redmi Note 11, 31000.0 руб. Остаток: 14"]


def test_str_product():
    print((common_list[1][0][0]))
    assert True


def test_add_product():
    assert common_list[1][0][0] + common_list[1][0][1] == 2580000.0
    with pytest.raises(ValueError):
        print(common_list[1][0][0] + common_list[0][0])


p = Product("z", "v", 3, 4)
c = Category("c_p", "d_p", [])


def test_add_product_in_category():
    c.product = p
    print(c.product)
    assert c.product
    with pytest.raises(TypeError):
        c.product = c
