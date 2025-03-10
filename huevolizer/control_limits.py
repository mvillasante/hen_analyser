import pandas as pd


class X_R_limits_calculator:
    def __init__(self, raw_data: pd.DataFrame):
        self.data = self.set_data(raw_data)
        self.x_s = calculate_average_per_sample(self.data)

    def set_data(self, data: pd.DataFrame):
        return set_eggs_by_hen(data)

    def get_X_limits(self):
        mean_X = self.x_s.mean()
        desviation_X = self.x_s.std()
        return {
            "average": mean_X,
            "one_sigma": mean_X + desviation_X,
            "two_sigma": mean_X + 2 * desviation_X,
            "three_sigma": mean_X + 3 * desviation_X,
            "minus_one_sigma": mean_X - desviation_X,
            "minus_two_sigma": mean_X - 2 * desviation_X,
            "minus_three_sigma": mean_X - 3 * desviation_X,
        }

    def get_R_limits(self):
        range_per_sample = calculate_range_per_sample(self.data)
        print(range_per_sample)
        mean_R = range_per_sample.mean()
        return {
            "average": mean_R,
        }


def calculate_range_per_sample(data):
    sample_size = 2
    range_of_sample = abs(
        data.eggs_by_hen.rolling(sample_size).max() - data.eggs_by_hen.rolling(sample_size).min()
    )
    return range_of_sample[1::sample_size]


def calculate_average_per_sample(data):
    sample_size = 2
    mean_of_two_values = data.eggs_by_hen.rolling(sample_size).mean()
    return mean_of_two_values[1::sample_size]


def set_eggs_by_hen(raw_data):
    raw_data["eggs_by_hen"] = raw_data.Huevos / raw_data.Gallinas
    return raw_data
