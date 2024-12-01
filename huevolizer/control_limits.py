from bootstrapping_tools import resample_data


def calculate_average_per_sample(data):
    mean_of_two_values = data.rolling(2, step=1, closed="right").mean()
    return mean_of_two_values.iloc[1::2, :]


def set_eggs_by_hen(raw_data):
    raw_data["eggs_by_hen"] = raw_data.Huevos / raw_data.Gallinas
    return raw_data
