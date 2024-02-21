from function import create_instance, open_json


class CategoryIteration:
    def __init__(self, category_name):
        self.category_name = category_name

    def __iter__(self):
        for i in create_instance(open_json())[0]:
           if i.name == self.category_name:
               self.iter_object = i.product
        return self.iter_object

    def __next__(self):
        index_counter = -1
        index_counter += 1
        return self.iter_object[index_counter]
