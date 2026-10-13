from huevolizer.app_helpers import append_to_csv

import pandas as pd


def test_append_to_csv_creates_file_when_new():
    df = pd.DataFrame({"col1": [1, 2], "col2": ["a", "b"]})
    path = "tests/out.csv"
    append_to_csv(df, path)
    result = pd.read_csv(path)
