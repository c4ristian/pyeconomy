"""
This module provides classes and functions to setup and run the pyeconomy simulator.
"""

# Imports
import numpy as np
import pandas as pd


def simulate_n_rounds(number_of_rounds, population):
    """
    This method simulates several rounds for the population of a virtual economy.
    :param number_of_rounds: The number of rounds to simulate.
    :param population: The population to be modified.
    :return: A pandas data frame with results of every round.
    """
    result_frame = pd.DataFrame([vars(c) for c in population])
    result_frame["round"] = 0
    result_frame["final"] = False

    for r in range(1, number_of_rounds + 1):
        simulate_next_round(population)
        current_frame = pd.DataFrame([vars(c) for c in population])
        current_frame["round"] = r
        current_frame["final"] = r == number_of_rounds
        result_frame = result_frame.append(current_frame, ignore_index=True)

    return result_frame


def simulate_next_round(population):
    """
    This method simulates the next round for the population of a virtual economy.
    :param population: The list of Citizen objects to be modified.
    :return: None.
    """
    for citizen in population:
        current_income = citizen.current_income
        current_savings = citizen.current_savings
        saving_rate = citizen.saving_rate
        interest_rate = citizen.interest_rate

        expected_rise_mean = citizen.expected_rise_mean
        expected_rise_sd = citizen.expected_rise_sd

        income_rise = np.random.normal(expected_rise_mean, expected_rise_sd)
        next_income = current_income * (1 + income_rise)

        new_savings = next_income * saving_rate
        interest = current_savings * interest_rate

        citizen.current_income = next_income
        citizen.current_savings = current_savings + interest + new_savings


def execute_simulator(number_of_rounds=20, population_size=100):
    """
    This method runs the pyeconomy simulator and returns a pandas data frame
    with the results.
    :param number_of_rounds: The number of rounds to simulate.
    :param population_size: The number of citizens of the virtual economy.
    :return: A pandas data frame with the results.
    """
    return pd.DataFrame()
