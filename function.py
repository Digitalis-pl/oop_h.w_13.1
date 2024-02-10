import json
from classes import Category, Product
def open_json():
    with open("products.json", "r", encoding="utf-8") as f:
        category_list = json.loads(f.read())
        return category_list

def create_instance(category_list):
    category_instance_list = []
    product_list = []
    for i in category_list:
        category_instance_list.append(Category(i["name"], i["description"], i["products"]))
        for x in i["products"]:
            product_list.append(Product(x["name"], x["description"], x["price"], x["quantity"]))
    return [category_instance_list, product_list]
print(create_instance(open_json()))

