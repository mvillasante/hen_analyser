import huevolizer as dt
import pandas as pd


def test_set_data():
    data = pd.DataFrame({"Huevos": [1, 2, 3], "Gallinas": [1, 2, 3]})
    obtained = dt.set_eggs_by_hen(data)
    expected_column = "huevos_by_hen"
    assert expected_column in obtained.columns


def test_add_offset():
    augend = 1
    addend = 2
    expected = augend + addend
    obtained = dt.add_offset(augend, addend)
    assert expected == obtained
