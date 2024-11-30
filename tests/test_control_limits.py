from huevolizer.control_limits import set_eggs_by_hen, calculate_average_per_sample

import pandas as pd


def test_set_data():
    data = pd.DataFrame({"Huevos": [1, 2, 3], "Gallinas": [1, 2, 1]})
    obtained = set_eggs_by_hen(data)
    expected_column = "eggs_by_hen"
    assert expected_column in obtained.columns
    assert (obtained.eggs_by_hen == [1, 1, 3]).all()


def test_calculate_average_per_sample():
    data = pd.DataFrame({"eggs_by_hen": [15, 5, 9, 11, 8, 12, 7, 13, 6, 14]})
    obtained = calculate_average_per_sample(data)
    assert len(obtained) == 5
