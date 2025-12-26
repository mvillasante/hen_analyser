import pandas as pd


def fill_missing_dates(data):
    indexed_data = data.set_index("Fecha", drop=True).copy()
    complete_dates = pd.date_range(indexed_data.index.min(), indexed_data.index.max(), freq="D")
    return indexed_data.reindex(complete_dates)
