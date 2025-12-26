def fill_missing_dates(data):
    return data.set_index("Fecha", drop=True)
