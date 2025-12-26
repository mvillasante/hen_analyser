from huevolizer.set_data import fill_missing_dates

import pandas as pd
from numpy import datetime_as_string


def test_fill_missing_date():
    data = pd.DataFrame(
        {
            "Fecha": ["2021-04-30", "2021-05-30"],
            "Gallinas": [16, 15],
            "Gallos": [2, 2],
            "Pollos": [8, 7],
        }
    )
    obtained = fill_missing_dates(data)
    assert datetime_as_string(obtained.index[0], unit="D") == "2021-04-30"
    assert len(obtained) >= 30
