from huevolizer.set_data import fill_missing_dates, join_daily_eggs_with_individual_counts

import pandas as pd
from numpy import datetime_as_string


individual_data = pd.DataFrame(
    {
        "Fecha": ["2021-04-30", "2021-05-30"],
        "Gallinas": [16, 15],
        "Gallos": [2, 2],
        "Pollos": [8, 7],
    }
)


def test_fill_missing_date():
    obtained = fill_missing_dates(individual_data)
    print(obtained)
    assert obtained.index.values[0] == "2021-04-30"
    assert len(obtained) >= 30
    assert obtained.Gallinas.iloc[1] == 16


def test_join_daily_eggs_with_individual_counts():
    daily_eggs_data = pd.DataFrame(
        {
            "Fecha": ["2021-04-30", "2021-04-31", "2021-05-30"],
            "Huevos": [5, 8, 7],
        }
    )
    obtained = join_daily_eggs_with_individual_counts(daily_eggs_data, individual_data)
    is_without_na = not obtained.Gallinas.isna().any()
    assert is_without_na
