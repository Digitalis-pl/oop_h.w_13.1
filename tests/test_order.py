from class_order import Order

order = Order("Samsung Galaxy C23 Ultra", 2)


def test_init_order():
    order.choose_product()
    order.count_total_sum()
    assert order.product_quantity == 2
    assert order.product_name == "Samsung Galaxy C23 Ultra"
    assert order.total == 360000.0
    print(order)
