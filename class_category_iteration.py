from function import create_instance, open_json
from mixin_repr import MixinRepr


class CategoryIteration(MixinRepr):
    def __init__(self, category_name):
        self.index_counter = 0
        self.category_name = category_name
        self.iter_object = []
        super().__repr__()


    def __iter__(self):
        for i in create_instance(open_json())[0]:
            print(i)
            if i.name == self.category_name:
                self.iter_object = i.product
                break
        return self

    def __next__(self):
        if self.index_counter < len(self.iter_object):
            result = self.iter_object[self.index_counter]
            self.index_counter += 1
            return result
        else:
            raise StopIteration
