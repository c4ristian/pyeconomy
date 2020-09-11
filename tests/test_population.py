"""
This module contains test cases for the module pyeconomy.population.
"""

# Imports
import pytest
import pyeconomy.population as pop


def test_create_population():
    """
    Test case for the method create_population.
    :return:
    """
    # Create a population with static attributes
    population = pop.create_population(
        current_income=100, expected_rise_mean=0.01,
        expected_rise_sd=0.005, saving_rate=0.05,
        interest_rate=0.03, size=2)

    assert population
    assert len(population) == 2

    for citizen_id, citizen in enumerate(population):
        assert citizen.citizen_id == citizen_id
        assert citizen.current_income == 100
        assert citizen.expected_rise_mean == 0.01
        assert citizen.expected_rise_sd == 0.005
        assert citizen.current_savings == 0
        assert citizen.saving_rate == 0.05
        assert citizen.interest_rate == 0.03

    # Create a population with various attributes
    population = pop.create_population(
        current_income=100, expected_rise_mean=[0.01, 0.02],
        expected_rise_sd=[0.01, 0.02], current_savings=50,
        saving_rate=0.05, interest_rate=[0.05, 0.06], size=2
    )

    assert population
    assert len(population) == 2

    for citizen_id, citizen in enumerate(population):
        assert citizen.citizen_id == citizen_id
        assert citizen.current_income == 100
        assert citizen.current_savings == 50
        assert citizen.saving_rate == 0.05

        if citizen_id == 0:
            assert citizen.expected_rise_mean == 0.01
            assert citizen.expected_rise_sd == 0.01
            assert citizen.interest_rate == 0.05
        else:
            assert citizen.expected_rise_mean == 0.02
            assert citizen.expected_rise_sd == 0.02
            assert citizen.interest_rate == 0.06

    # Create empty
    population = pop.create_population(size=-1)
    assert len(population) == 0

    # Create illegal population
    with pytest.raises(AssertionError):
        pop.create_population()
