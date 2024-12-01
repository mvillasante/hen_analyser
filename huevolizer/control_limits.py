def calculate_range_per_sample(data):
    sample_size = 2
    range_of_sample = abs(data.rolling(sample_size).max() - data.rolling(sample_size).min())
    return range_of_sample.iloc[1::sample_size, :]


def calculate_average_per_sample(data):
    sample_size = 2
    mean_of_two_values = data.rolling(sample_size).mean()
    return mean_of_two_values.iloc[1::sample_size, :]


def set_eggs_by_hen(raw_data):
    raw_data["eggs_by_hen"] = raw_data.Huevos / raw_data.Gallinas
    return raw_data
