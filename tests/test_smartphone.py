from class_smartphone import Smartphone


b = Smartphone("Samsung",
               "200MP камера",
               210000,
               5,
               300,
               "Galaxy C23 Ultra",
               "256GB",
               "Серый")


def test_init_smartphone():
    assert b.name == "Samsung"
    assert b.description == "200MP камера"
    assert b.quantity == 5
    assert b.efficiency == 300
    assert b.model == "Galaxy C23 Ultra"
    assert b.internal_memory == "256GB"
    assert b.color == "Серый"
