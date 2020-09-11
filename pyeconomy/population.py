"""
This module provides classes and functions to model the population the virtual economy.
"""


class Citizen:
    """
    This class models a citizen of the virtual economy.
    """
    def __init__(self, citizen_id: float, current_income: float, expected_rise_mean: float,
                 expected_rise_sd: float, current_savings: float, saving_rate: float,
                 interest_rate: float):
        """
        Create a new Citizen object.
        :param citizen_id: Unique identifier of the citizen in the population.
        :param current_income: The current income in currency units.
        :param expected_rise_mean: The mean of the expected rise of income in percent.
        :param expected_rise_sd: The standard deviation of the expected rise in percent.
        :param current_savings: The current savings of the Citizen in currency units.
        :param saving_rate: The savings rate in percent.
        :param interest_rate: The interest rate paid on savings in percent.
        """
        self.citizen_id = citizen_id
        self.current_income = current_income
        self.expected_rise_mean = expected_rise_mean
        self.expected_rise_sd = expected_rise_sd
        self.current_savings = current_savings
        self.saving_rate = saving_rate
        self.interest_rate = interest_rate


def create_population(
        current_income=100, expected_rise_mean=0.01,
        expected_rise_sd=0.01, current_savings=0,
        saving_rate=0.05, interest_rate=0.01, size=None):
    """
    This function creates a list of Citizen objects. The attributes of the citizens
    can either be specified as list or single values. If a list is provided, the
    length must equal the population size. If a single value is provided all
    citizens share the same attribute value.

    :param size: The size of the population.
    :param current_income: The current income in currency units as float or list.
    :param expected_rise_mean: The expected rise of income in percent as float or list.
    :param expected_rise_sd: The volatility of the rise in percent as float or list.
    :param current_savings: The current savings in currency units as float or list.
    :param saving_rate: The savings rate in percent as float or list.
    :param interest_rate: The interest rate paid on savings in percent as float or list.
    :return: The list of Citizen objects.
    """
    current_income_list = _as_list(current_income, size)
    expected_rise_mean_list = _as_list(expected_rise_mean, size)
    expected_rise_sd_list = _as_list(expected_rise_sd, size)
    current_savings_list = _as_list(current_savings, size)
    saving_rate_list = _as_list(saving_rate, size)
    interest_rate_list = _as_list(interest_rate, size)

    population = []

    for i in range(0, size):
        population.append(Citizen(
            i, current_income_list[i],
            expected_rise_mean_list[i],
            expected_rise_sd_list[i],
            current_savings_list[i],
            saving_rate_list[i],
            interest_rate_list[i]
        ))

    return population


def _as_list(variable, length: int):
    """
    Helper function that returns a list with instances of certain variable.
    If the variable is a list already the variable is returned.
    :param variable: The variable.
    :param length: The length of the list.
    :return:
    """
    assert isinstance(length, int), "Attribute length must be an integer"

    if isinstance(variable, list):
        result = variable
    else:
        result = [variable] * length

    return result
