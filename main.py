from classes import Product

d = Product.open_json()

d = Product("toster", "fry our bread", 6500.50, 20000)

print(d.change_price)
d.change_price = 3
print(d.change_price)