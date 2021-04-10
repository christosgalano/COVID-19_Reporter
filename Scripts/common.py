import pandas as pd


def calc_deaths_per_month(deaths, country=None):
    """
    Calculates the monthly number of deaths in a certain country if specified.
    :param deaths: DataFrame of deaths
    :param country: Name of the country
    :return: DataFrame or Series based on if a country was provided
    """
    deaths_per_month = deaths.diff().resample('M').sum()
    if country:
        deaths_per_month = deaths_per_month[country]
    return deaths_per_month.astype(int)


def general_info(confirmed, deaths, recovered, country=None):
    """
    Provides general information regarding the confirmed cases,recoveries,deaths,death rate
    and still active cases.
    :param confirmed: DataFrame of confirmed cases
    :param deaths: DataFrame of deaths
    :param recovered: DataFrame of recoveries
    :param country: Name of the country
    :return: DataFrame of general information
    """
    values = [confirmed.iloc[len(confirmed) - 1],
              recovered.iloc[len(recovered) - 1],
              deaths.iloc[len(deaths) - 1]]
    df = pd.DataFrame(values, index=['confirmed cases', 'recovered', 'deaths'])
    df.loc['active cases'] = values[0] - values[1] - values[2]
    df.loc['death rate'] = (values[2] / values[0]) * 100
    df = df.T
    df = df.astype({'confirmed cases': int, 'recovered': int, 'deaths': int,
                    'active cases': int, 'death rate': float})
    if country:
        df = df.loc[country]
    return df
