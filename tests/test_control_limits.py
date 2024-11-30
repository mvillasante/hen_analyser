from huevolizer.control_limits import set_eggs_by_hen
import pandas as pd


def test_set_data():
    data = pd.DataFrame({"Huevos": [1, 2, 3], "Gallinas": [1, 2, 3]})
    obtained = set_eggs_by_hen(data)
    expected_column = "eggs_by_hen"
    assert expected_column in obtained.columns
