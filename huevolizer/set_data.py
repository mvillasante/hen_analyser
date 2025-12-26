import pandas as pd
from numpy import datetime_as_string


def fill_missing_dates(data):
    indexed_data = data.set_index("Fecha").copy()
    complete_dates = pd.date_range(indexed_data.index.min(), indexed_data.index.max(), freq="D")
    return indexed_data.reindex(datetime_as_string(complete_dates, unit="D")).ffill()


def join_daily_eggs_with_individual_counts(daily_eggs, individuals_count):
    return daily_eggs.set_index("Fecha").join(individuals_count.set_index("Fecha"), how="left")
