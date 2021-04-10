import pandas as pd
import matplotlib.pyplot as plt
from typing import List


def general_visualize(data: pd.DataFrame, name: str, countries: List[str]):
    """
    Creates a graph regarding the data of the countries that are provided.
    :param data: DataFrame to be plotted
    :param name: Name to be used in the title of the graph
    :param countries: Countries of the DataFrame to be plotted
    :return: None
    """
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.set_facecolor('black')
    ax.figure.set_facecolor('#121212')
    ax.ticklabel_format(useOffset=False, style='plain')
    ax.tick_params(axis='x', colors='white')
    ax.tick_params(axis='y', colors='white')
    ax.set_title(f'COVID-19 - Total {name}', color='white')
    for country in countries:
        data[country][0:].plot(label=country)
    fig.tight_layout()
    plt.legend(loc='upper left')
    plt.show()


def visualize_rate(rate: pd.DataFrame, name: str, country: str, freq='W', date=None):
    """
    Creates a bar chart regarding the rate of the country which is provided.
    :param rate: DataFrame with data regarding rates
    :param name: Name to be used in the title of the graph
    :param country: Name of the country
    :param freq: Frequency on which the graph is based, default is weekly
    :param date: Only data from that day and forward are used
    :return:
    """
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.set_facecolor('black')
    ax.figure.set_facecolor('#121212')
    ax.ticklabel_format(useOffset=False, style='plain')
    ax.tick_params(axis='x', colors='white')
    ax.tick_params(axis='y', colors='white')
    ax.set_title(f'COVID-19 - {name} [{country}]', color='white')
    rate = rate.resample(freq).sum()
    rate = rate[country][date if date else 0:]
    rate.index = rate.index.date
    rate.plot.bar()
    fig.tight_layout()
    plt.show()
