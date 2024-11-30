from bootstrapping_tools import resample_data


def calculate_average_per_sample(data):
    samples_of_two = resample_data(data, None, 2)
    return samples_of_two.iloc[0:5]


def set_eggs_by_hen(raw_data):
    raw_data["eggs_by_hen"] = raw_data.Huevos / raw_data.Gallinas
    return raw_data
