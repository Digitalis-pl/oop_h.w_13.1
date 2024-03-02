from class_order import Order


class Exceptions:
    def __init__(self):
        try:
            name = input()
            number = input()
            Order(product_name=name, product_quantity=number)
        except ValueError:
            print("Необходимо выбрать количество")
        else:
            print("Товар успешно добавлен")
        finally:
            print("Обработка товара завершена")
