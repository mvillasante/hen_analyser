import pandas as pd


class X_R_limits_calculator:
    def __init__(self, raw_data: pd.DataFrame):
        self.data = self.set_data(raw_data)
        print(self.data.dtypes)
        self.x_s = calculate_average_per_sample(self.data)
        self.r_s = calculate_range_per_sample(self.data)

    def save_x_r(self, output_path: str):
        pd.DataFrame({"Fecha": self.data.Fecha.loc[1:], "X": self.x_s, "R": self.r_s}).set_index(
            "Fecha"
        ).to_csv(output_path)

    def set_data(self, raw_data: pd.DataFrame):
        return self.set_eggs_by_hen(raw_data)

    def set_eggs_by_hen(self, raw_data):
        raw_data["eggs_by_hen"] = raw_data.Huevos / raw_data.Gallinas
        return raw_data

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
        mean_R = self.r_s.mean()
        desviation_R = self.r_s.std()
        return {
            "average": mean_R,
            "one_sigma": mean_R + desviation_R,
            "two_sigma": mean_R + 2 * desviation_R,
            "three_sigma": mean_R + 3 * desviation_R,
            "minus_one_sigma": mean_R - desviation_R,
            "minus_two_sigma": mean_R - 2 * desviation_R,
            "minus_three_sigma": mean_R - 3 * desviation_R,
        }


def calculate_range_per_sample(data):
    sample_size = 2
    range_of_sample = abs(
        data.eggs_by_hen.rolling(sample_size).max() - data.eggs_by_hen.rolling(sample_size).min()
    )
    return range_of_sample[1:]


def calculate_average_per_sample(data):
    sample_size = 2
    mean_of_two_values = data.eggs_by_hen.rolling(sample_size).mean()
    return mean_of_two_values[1:]
