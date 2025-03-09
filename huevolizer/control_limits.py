import pandas as pd


class X_R_limits_calculator:
    def __init__(self, raw_data: pd.DataFrame):
        self.data = self.set_data(raw_data)

    def set_data(self, data: pd.DataFrame):
        return set_eggs_by_hen(data)

    def get_sigmas(self):
        average_per_sample = calculate_average_per_sample(self.data)
        return {
            "average": average_per_sample.mean(),
            "one_sigma": average_per_sample.std(),
            "two_sigma": 2 * average_per_sample.std(),
        }


def calculate_range_per_sample(data):
    sample_size = 2
    range_of_sample = abs(data.rolling(sample_size).max() - data.rolling(sample_size).min())
    return range_of_sample.eggs_by_hen[1::sample_size]


def calculate_average_per_sample(data):
    sample_size = 2
    mean_of_two_values = data.rolling(sample_size).mean()
    return mean_of_two_values.eggs_by_hen[1::sample_size]


def set_eggs_by_hen(raw_data):
    raw_data["eggs_by_hen"] = raw_data.Huevos / raw_data.Gallinas
    return raw_data
