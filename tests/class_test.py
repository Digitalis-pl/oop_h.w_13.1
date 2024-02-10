import pytest
from classes import Product, Category

@pytest.fixture
def product_toster():
    return Product("toster", "fry our bread", 6500.50, 20000)

def test_init(product_toster):
    assert product_toster.name == "toster"
    assert product_toster.description == "fry our bread"
    assert product_toster.price == 6500.50
    assert product_toster.count == 20000

@pytest.fixture()
def device_category():
    return Category("devices", "electronic", "tosters")

def test_init_category(device_category):
    assert device_category.name == "devices"
    assert device_category.description == "electronic"
    assert device_category.product == "tosters"

category_list = [
  {
    "name": "Смартфоны",
    "description": "Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни",
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
    "description": "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником",
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

def test_all_category():
    all_category(category_list) == 2
