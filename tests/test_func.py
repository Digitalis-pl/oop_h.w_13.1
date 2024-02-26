from function import create_instance, open_json


prod_list = open_json()
common_list = create_instance(prod_list)


def test_create_instance():
    assert common_list[1][0][0].name == "Samsung Galaxy C23 Ultra"
