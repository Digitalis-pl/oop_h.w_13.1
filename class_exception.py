class ScriptError(Exception):

    def __init__(self, *args, **kwargs):
        self.message = args[0] if args else "товар с нулевым количеством не может быть добавлен."

    def __str__(self):
        return self.message


class CheckQuantityException(ScriptError):
    def __init__(self, *args):
        self.quantity = args[0]
        try:
            if self.quantity == 0:
                raise ScriptError
        except ScriptError:
            print("Необходимо выбрать количество")
        else:
            print("Товар успешно добавлен")
        finally:
            print("Обработка товара завершена")
