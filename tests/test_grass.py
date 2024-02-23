from class_grass import Grass


a = Grass("sphagnum",
          "green green",
          3000,
          5,
          "Sweden",
          "2 month",
          "green")


def test_init_grass():
    assert a.name == "sphagnum"
    assert a.description == "green green"
    assert a.quantity == 5
    assert a.country == "Sweden"
    assert a.color == "green"
