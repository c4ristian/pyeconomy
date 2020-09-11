"""
This module contains test cases for the module pyeconomy.simulator.
"""
# Imports
import pyeconomy.simulator as sim
import pyeconomy.population as pop


def test_simulate_n_rounds():
    """
    Test case for the method simulat_n_rounds.
    :return:
    """
    # Test a population without random elements
    population = pop.create_population(
        size=5, current_income=100,
        expected_rise_mean=0.01, expected_rise_sd=0.0,
        current_savings=0, saving_rate=0.1)

    assert len(population) == 5

    result_frame = sim.simulate_n_rounds(2, population)
    assert len(result_frame) == 15
    assert len(result_frame["citizen_id"].unique()) == 5
    assert list(result_frame["round"].unique()) == [0, 1, 2]
    assert result_frame["expected_rise_mean"].mean() == 0.01
    assert result_frame["expected_rise_sd"].mean() == 0.0

    final_results = result_frame[result_frame["final"]]

    assert len(final_results) == 5
    assert final_results["current_income"].mean() == 102.01

    # Test a population with random elements
    population = pop.create_population(
        size=1000, current_income=100,
        expected_rise_mean=0.01, expected_rise_sd=0.01,
        current_savings=0, saving_rate=0.1)

    assert len(population) == 1000

    result_frame = sim.simulate_n_rounds(30, population)
    assert len(result_frame) == 31000
    assert len(result_frame["citizen_id"].unique()) == 1000


def test_simulate_next_round():
    """
    Test case for the basic functionality of the method simulate_next_round.
    :return: None.
    """
    # Test a population without random elements
    population = pop.create_population(
        size=5, current_income=100,
        expected_rise_mean=0.01, expected_rise_sd=0.0,
        current_savings=0, saving_rate=0.1, interest_rate=0.05)

    assert len(population) == 5

    sim.simulate_next_round(population)

    for citizen in population:
        assert citizen.expected_rise_mean == 0.01
        assert citizen.expected_rise_sd == 0.0
        assert citizen.saving_rate == 0.1
        assert citizen.current_income == 101
        assert round(citizen.current_savings, 1) == 10.1

    # Test a population with random elements
    population = pop.create_population(
        size=5, current_income=100,
        expected_rise_mean=0.01, expected_rise_sd=0.01,
        current_savings=0, saving_rate=0.1)

    sim.simulate_next_round(population)

    for citizen in population:
        assert citizen.expected_rise_mean == 0.01
        assert citizen.expected_rise_sd == 0.01
        assert citizen.saving_rate == 0.1
        assert isinstance(citizen.current_income, float)
        assert isinstance(citizen.current_savings, float)


def test_savings_calculation():
    """
    This test case tests the calculation of savings and interest.
    :return: None.
    """
    population = pop.create_population(
        size=5, current_income=100,
        expected_rise_mean=0.01, expected_rise_sd=0.0,
        current_savings=10, saving_rate=0.1, interest_rate=0.05)

    sim.simulate_next_round(population)

    for citizen in population:
        assert citizen.expected_rise_mean == 0.01
        assert citizen.expected_rise_sd == 0.0
        assert citizen.saving_rate == 0.1
        assert citizen.current_income == 101
        assert round(citizen.current_savings, 1) == 20.6

    sim.simulate_next_round(population)

    for citizen in population:
        assert citizen.expected_rise_mean == 0.01
        assert citizen.expected_rise_sd == 0.0
        assert citizen.saving_rate == 0.1
        assert citizen.current_income == 102.01
        assert round(citizen.current_savings, 2) == 31.83
