from class_category import Category


class CategoryIteration:
    def __init__(self, category_name):
        self.category_name = category_name

    def __iter__(self):
        if Category.name == self.category_name:
            return Category.product

    def __next__(self):
        index_counter = -1
        index_counter += 1
        return Category.product[index_counter]
