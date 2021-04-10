import pandas as pd
import requests


def update_data():
    """
    Downloads the data. The data get updated daily.
    :return: None
    """
    def download_data(url, filename):
        req = requests.get(url)
        with open(filename, 'wb') as f:
            f.write(req.content)

    confirmed_url = "https://data.humdata.org/hxlproxy/api/data-preview.csv?" \
                    "url=https%3A%2F%2Fraw.githubusercontent.com%2FCSSEGISandData%2FCOVID-19%" \
                    "2Fmaster%2Fcsse_covid_19_data%2Fcsse_covid_19_time_series%" \
                    "2Ftime_series_covid19_confirmed_global.csv&filename=time_series_covid19_confirmed_global.csv"

    deaths_url = "https://data.humdata.org/hxlproxy/api/data-preview.csv?url=https%3A%2F%" \
                 "2Fraw.githubusercontent.com%2FCSSEGISandData%2FCOVID-19%2Fmaster%" \
                 "2Fcsse_covid_19_data%2Fcsse_covid_19_time_series%2Ftime_series_covid19_deaths_global.csv&" \
                 "filename=time_series_covid19_deaths_global.csv"

    recovered_url = "https://data.humdata.org/hxlproxy/api/data-preview.csv?" \
                    "url=https%3A%2F%2Fraw.githubusercontent.com%2FCSSEGISandData%2FCOVID-19%" \
                    "2Fmaster%2Fcsse_covid_19_data%2Fcsse_covid_19_time_series%" \
                    "2Ftime_series_covid19_recovered_global.csv&filename=time_series_covid19_recovered_global.csv"

    download_data(confirmed_url, "../Datasets/covid19_confirmed_global.csv")
    download_data(deaths_url, "../Datasets/covid19_deaths_global.csv")
    download_data(recovered_url, "../Datasets/covid19_recovered_global.csv")


def read_data():
    """
    Reads the data and adjusts them.
    :return: Dictionary of the data
    """
    def adjust(data):
        data = data.drop(['Province/State', 'Lat', 'Long'], axis=1)
        data = data.groupby(data['Country/Region']).aggregate('sum')
        data = data.T
        data.index = pd.to_datetime(data.index)
        return data

    confirmed = pd.read_csv("../Datasets/covid19_confirmed_global.csv")
    deaths = pd.read_csv("../Datasets/covid19_deaths_global.csv")
    recovered = pd.read_csv("../Datasets/covid19_recovered_global.csv")

    confirmed = adjust(confirmed)
    deaths = adjust(deaths)
    recovered = adjust(recovered)
    return {'confirmed': confirmed, 'deaths': deaths, 'recovered': recovered}
