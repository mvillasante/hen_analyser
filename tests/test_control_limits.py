from huevolizer.control_limits import (
    set_eggs_by_hen,
    calculate_average_per_sample,
    calculate_range_per_sample,
)

import pandas as pd


def test_set_data():
    data = pd.DataFrame({"Huevos": [1, 2, 3], "Gallinas": [1, 2, 1]})
    obtained = set_eggs_by_hen(data)
    expected_column = "eggs_by_hen"
    assert expected_column in obtained.columns
    assert (obtained.eggs_by_hen == [1, 1, 3]).all()


sorted_data = pd.DataFrame({"eggs_by_hen": [15, 5, 9, 11, 8, 12, 7, 13, 6, 14]})


def test_calculate_average_per_sample():
    obtained = calculate_average_per_sample(sorted_data)
    assert len(obtained) == 5
    assert obtained.iloc[0].values == 10


def test_calculate_range_per_sample():
    obtained = calculate_range_per_sample(sorted_data)
    assert len(obtained) == 5
    assert obtained.iloc[0].values == 10
