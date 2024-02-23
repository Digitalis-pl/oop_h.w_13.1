from function import create_instance, open_json
from class_category_iteration import CategoryIteration


some = create_instance(open_json())[1]


def show():
    index = -1
    index += 1
    return some[index]


a = CategoryIteration("Смартфоны")
for x in a:
    print(x)
