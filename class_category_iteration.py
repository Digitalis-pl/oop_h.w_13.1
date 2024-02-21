from function import create_instance, open_json


class CategoryIteration:
    index_counter = -1

    def __init__(self, category_name):
        self.category_name = category_name

    def __iter__(self):
        for i in create_instance(open_json())[0]:
            print(i)
            if i.name == self.category_name:
                self.iter_object = i.product
                print(self.iter_object)
        return self

    def __next__(self):
        CategoryIteration.index_counter += 1
        print(self.iter_object[CategoryIteration.index_counter])
        return self.iter_object[CategoryIteration.index_counter]
