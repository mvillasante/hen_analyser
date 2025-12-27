from huevolizer.control_limits import (
    calculate_average_per_sample,
    calculate_range_per_sample,
    X_R_limits_calculator,
)

import pandas as pd


def test_x_r_chart_limits_calculator():
    raw_data = pd.DataFrame(
        {
            "Fecha": [
                "2021-01-01",
                "2021-01-02",
                "2021-01-03",
                "2021-01-04",
            ],
            "Huevos": [1, 2, 6, 2],
        }
    )

    individual_data = pd.DataFrame(
        {
            "Fecha": [
                "2021-01-01",
                "2021-01-02",
                "2021-01-03",
                "2021-01-04",
            ],
            "Gallinas": [1, 2, 3, 1],
            "Gallos": [2, 2, 2, 3],
            "Pollos": [8, 7, 8, 7],
        }
    )
    chart_limits_calculator = X_R_limits_calculator(raw_data, individual_data)
    obtained = chart_limits_calculator.data
    assert "eggs_by_hen" in obtained.columns
    obtained = chart_limits_calculator.get_X_limits()
    assert obtained["average"] == 1.5
    assert obtained["one_sigma"] > obtained["average"]
    assert obtained["two_sigma"] > obtained["one_sigma"]
    assert obtained["three_sigma"] > obtained["two_sigma"]
    assert obtained["minus_one_sigma"] < obtained["average"]
    assert obtained["minus_two_sigma"] < obtained["minus_one_sigma"]
    assert obtained["minus_three_sigma"] < obtained["minus_two_sigma"]
    raw_data = pd.DataFrame(
        {
            "Fecha": [
                "2021-01-01",
                "2021-01-02",
                "2021-01-03",
                "2021-01-04",
                "2021-01-05",
                "2021-01-06",
                "2021-01-07",
                "2021-01-08",
            ],
            "Huevos": [6, 1, 6, 1, 4, 8, 7, 1],
        }
    )
    individual_data = pd.DataFrame(
        {
            "Fecha": [
                "2021-01-01",
            ],
            "Gallinas": [11],
            "Gallos": [2],
            "Pollos": [8],
        }
    )
    chart_limits_calculator = X_R_limits_calculator(raw_data, individual_data)
    obtained = chart_limits_calculator.get_R_limits()
    assert obtained["average"] == 0.3766233766233765
    assert obtained["one_sigma"] > obtained["average"]
    assert obtained["two_sigma"] > obtained["one_sigma"]
    assert obtained["three_sigma"] > obtained["two_sigma"]
    assert obtained["minus_one_sigma"] < obtained["average"]
    assert obtained["minus_two_sigma"] < obtained["minus_one_sigma"]
    assert obtained["minus_three_sigma"] < obtained["minus_two_sigma"]


def test_set_data():
    data = pd.DataFrame({"Fecha": ["2021-01-01", "2021-01-02", "2021-01-03"], "Huevos": [1, 2, 3]})
    individual_data = pd.DataFrame(
        {
            "Fecha": ["2021-01-01", "2021-01-02", "2021-01-03"],
            "Gallinas": [1, 2, 1],
            "Gallos": [2, 1, 0],
            "Pollos": [8, 7, 6],
        }
    )
    chart_limits_calculator = X_R_limits_calculator(data, individual_data)
    expected_column = "eggs_by_hen"
    assert expected_column in chart_limits_calculator.data.columns
    assert (chart_limits_calculator.data.eggs_by_hen == [1, 1, 3]).all()


sorted_data = pd.DataFrame({"eggs_by_hen": [15, 5, 9, 11, 8, 12, 7, 13, 6, 14]})


def test_calculate_average_per_sample():
    obtained = calculate_average_per_sample(sorted_data)
    assert len(obtained) == 9
    assert obtained.iloc[0] == 10


def test_calculate_range_per_sample():
    obtained = calculate_range_per_sample(sorted_data)
    assert len(obtained) == 9
    assert obtained.iloc[0] == 10
