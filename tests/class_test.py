import pytest
from class_product import Product
from class_category import Category
from function import create_instance, open_json
from class_grass import Grass
from class_smartphone import Smartphone


category_list = [
  {
    "name": "Смартфоны",
    "description": "Смартфоны, как средство не только коммуникации, но и получение дополнительных"
                   " функций для удобства жизни",
    "products": [
      {
        "name": "Samsung Galaxy C23 Ultra",
        "description": "256GB, Серый цвет, 200MP камера",
        "price": 180000.0,
        "quantity": 5
      },
      {
        "name": "Iphone 15",
        "description": "512GB, Gray space",
        "price": 210000.0,
        "quantity": 8
      },
      {
        "name": "Xiaomi Redmi Note 11",
        "description": "1024GB, Синий",
        "price": 31000.0,
        "quantity": 14
      }
    ]
  },
  {
    "name": "Телевизоры",
    "description": "Современный телевизор, который позволяет наслаждаться просмотром,"
                   " станет вашим другом и помощником",
    "products": [
      {
        "name": "55\" QLED 4K",
        "description": "Фоновая подсветка",
        "price": 123000.0,
        "quantity": 7
      }
    ]
  }
]


@pytest.fixture
def product_toster():
    return Product("toster", "fry our bread", 6500.50, 20000)


def test_init(product_toster):
    assert product_toster.name == "toster"
    assert product_toster.description == "fry our bread"
    assert product_toster.price == 6500.50
    assert product_toster.quantity == 20000


@pytest.fixture()
def device_category():
    return [Category("devices", "electronic", [
      {
        "name": "Samsung Galaxy C23 Ultra",
        "description": "256GB, Серый цвет, 200MP камера",
        "price": 180000.0,
        "quantity": 5
      },
      {
        "name": "Iphone 15",
        "description": "512GB, Gray space",
        "price": 210000.0,
        "quantity": 8
      },
      {
        "name": "Xiaomi Redmi Note 11",
        "description": "1024GB, Синий",
        "price": 31000.0,
        "quantity": 14
      }
    ]), Category("tv", "tv", [

      {
        "name": "55\" QLED 4K",
        "description": "Фоновая подсветка",
        "price": 123000.0,
        "quantity": 7
      }
    ])]


def test_init_category(device_category):
    assert device_category[0].name == "devices"
    assert device_category[0].description == "electronic"
    assert Category.all_category == 2
    assert Category.unique_product == 4
    assert device_category[0].unique_product_in_category == 3
    assert device_category[1].unique_product_in_category == 1


prod_list = open_json()


def test_create_instance():
  assert create_instance(prod_list)[1][0][0].name == "Samsung Galaxy C23 Ultra"


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
  assert Product.create_product(d, create_instance(prod_list)[1][0])
  assert Product.create_product(d, create_instance(prod_list)[1][0]).description == "Фоновая подсветка"
  assert Product.create_product(d, create_instance(prod_list)[1][0]).quantity == 7
  assert Product.create_product(d, create_instance(prod_list)[1][0]).price == 123000.0
  assert Product.create_product(d, create_instance(prod_list)[1][0]).name == "55\" QLED 4K"
  assert Product.create_product(m, create_instance(prod_list)[1][0])
  assert Product.create_product(m, create_instance(prod_list)[1][0]).quantity == 28
  assert Product.create_product(m, create_instance(prod_list)[1][0]).name == "Xiaomi Redmi Note 11"
  assert Product.create_product(m, create_instance(prod_list)[1][0]).price == 31000.0
  assert Product.create_product(m, create_instance(prod_list)[1][0]).description == "1024GB, Синий"
  assert Product.create_product(m_p, create_instance(prod_list)[1][0])
  assert Product.create_product(m_p, create_instance(prod_list)[1][0]).quantity == 28
  assert Product.create_product(m_p, create_instance(prod_list)[1][0]).name == "Xiaomi Redmi Note 11"
  assert Product.create_product(m_p, create_instance(prod_list)[1][0]).price == 31100.0
  assert Product.create_product(m_p, create_instance(prod_list)[1][0]).description == "1024GB, Синий"


def test_show_product():
    assert create_instance(open_json())[0][0].product == ["Samsung Galaxy C23 Ultra, 180000.0 руб. Остаток: 5",
                                                               "Iphone 15, 210000.0 руб. Остаток: 8",
                                                               "Xiaomi Redmi Note 11, 31000.0 руб. Остаток: 14"]


def test_len_category():
    assert len(create_instance(open_json())[0][0]) == 3


def test_str_category():
    print((create_instance(open_json())[0][0]))
    assert True


def test_str_product():
    print((create_instance(open_json())[1][0][0]))
    assert True


def test_add_product():
    assert create_instance(open_json())[1][0][0] + create_instance(open_json())[1][0][1] == 2580000.0
    with pytest.raises(TypeError):
       print(create_instance(open_json())[1][0][0] + create_instance(open_json())[0][0])


a = Grass("sphagnum", "green green", 3000, 5, "Sweden", "2 month",  "green")


def test_init_grass():
    assert a.name == "sphagnum"
    assert a.description == "green green"
    assert a.price == 3000
    assert a.quantity == 5
    assert a.country == "Sweden"
    assert a.color == "green"


b = Smartphone("Samsung", "200MP камера", 210000, 5, 300, "Galaxy C23 Ultra", "256GB", "Серый")


def test_init_smartphone():
    assert b.name == "Samsung"
    assert b.description == "200MP камера"
    assert b.price == 210000
    assert b.quantity == 5
    assert b.efficiency == 300
    assert b.model == "Galaxy C23 Ultra"
    assert b.internal_memory == "256GB"
    assert b.color == "Серый"
