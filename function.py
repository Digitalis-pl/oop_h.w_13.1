from class_product import Product
from class_category import Category
import json


def open_json():
    with open("products.json", "r", encoding="utf-8") as f:
        category_list = json.loads(f.read())
        return category_list


def create_instance(category_list):
    category_instance_list = []
    product_list = []
    all_product_list = []
    counter = -1

    for i in category_list:
        product_list.append([])
        counter += 1
        for x in i["products"]:
            product_list[counter].append(Product(x["name"], x["description"], x["price"], x["quantity"]))
            all_product_list.append(Product(x["name"], x["description"], x["price"], x["quantity"]))
        category_instance_list.append(Category(i["name"], i["description"], product_list[counter]))
    return [category_instance_list, product_list, all_product_list]
