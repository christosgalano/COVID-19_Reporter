from fetch import update_data, read_data
import cases
import rates
import common
import visualize


def main():
    # Example of usage
    update_data()
    data = read_data()

    active_cases = cases.calc_active_cases(data['confirmed'],
                                           data['deaths'],
                                           data['recovered'])

    overall_growth_rate = rates.calc_overall_growth_rate(data['confirmed'],
                                                         active_cases)

    visualize.visualize_rate(overall_growth_rate,
                             'Overall Growth Rate',
                             'China',
                             freq='W')


if __name__ == "__main__":
    main()
