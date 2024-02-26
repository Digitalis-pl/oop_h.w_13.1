import pytest
from class_category import Category
from function import open_json, create_instance


prod_list = open_json()
common_list = create_instance(prod_list)


def test_init_category():
    Category.all_category = 0
    Category.unique_product = 0
    o = Category("w", "e", [1, 2, 3, 7, 8])
    b = Category("f", "k", [4, 5, 6])
    assert o.name == "w"
    assert b.description == "k"
    assert Category.all_category == 2
    assert Category.unique_product == 8
    assert b.unique_product_in_category == 3
    assert o.unique_product_in_category == 5


def test_len_category():
    assert len(common_list[0][0]) == 3


def test_str_category():
    print((common_list[0][0]))
    assert True


