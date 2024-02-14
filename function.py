import json
from classes import Category, Product, CateProd

def create_instance(category_list):
    category_instance_list = []
    product_list = []
    counter = -1
    for i in category_list:
        product_list.append([])
        counter += 1
        for x in i["products"]:
            product_list[counter].append(Product(x["name"], x["description"], x["price"], x["quantity"]))
        category_instance_list.append(Category(i["name"], i["description"], product_list[counter]))
    return [category_instance_list, product_list]

print(create_instance(CateProd.open_json())[0][0].product)