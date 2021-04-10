def calc_new_cases(confirmed):
    """
    Calculates the daily number of new confirmed cases.
    :param confirmed: DataFrame of confirmed cases
    :return: DataFrame of new confirmed cases
    """
    return confirmed.diff()


def calc_active_cases(confirmed, deaths, recovered):
    """
    Calculates the number of active cases.
    :param confirmed: DataFrame of new confirmed cases
    :param deaths: DataFrame of deaths
    :param recovered: DataFrame of recoveries
    :return: DataFrame of daily active cases
    """
    return confirmed - deaths - recovered
