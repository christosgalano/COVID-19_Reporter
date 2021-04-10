def calc_growth_rate(confirmed, new_cases):
    """
    Calculates the daily growth rate in confirmed cases.
    Note: rate = ((new - old) / new) * 100, but the difference new - old is already stored in new_cases
    :param confirmed: DataFrame of confirmed cases
    :param new_cases: DataFrame of new cases
    :return: DataFrame of daily growth_rate
    """
    growth_rate = confirmed.copy()
    for day in range(1, len(confirmed)):
        growth_rate.iloc[day] = (new_cases.iloc[day] / confirmed.iloc[day - 1]) * 100
    growth_rate = growth_rate.fillna(0.0)   # some days may have 0 confirmed cases
    return growth_rate


def calc_overall_growth_rate(confirmed, active_cases):
    """
    Calculates the daily growth rate in active cases.
    :param confirmed: DataFrame of confirmed cases
    :param active_cases: DataFrame of active cases
    :return: DataFrame of daily overall growth rate
    """
    overall_growth_rate = confirmed.copy()
    for day in range(1, len(confirmed)):
        overall_growth_rate.iloc[day] = ((active_cases.iloc[day] - active_cases.iloc[day - 1]) /
                                         active_cases.iloc[day - 1]) * 100
    overall_growth_rate = overall_growth_rate.fillna(0.0)
    return overall_growth_rate


def calc_death_rate(confirmed, deaths):
    """
    Calculates the daily death rate in confirmed cases.
    :param confirmed: DataFrame of confirmed cases
    :param deaths: DataFrame of deaths
    :return: DataFrame of daily death rate
    """
    death_rate = (deaths / confirmed) * 100
    death_rate = death_rate.fillna(0.0)
    return death_rate
