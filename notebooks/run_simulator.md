---
jupyter:
  jupytext:
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.2'
      jupytext_version: 1.6.0
  kernelspec:
    display_name: pyeconomy
    language: python
    name: pyeconomy
---

<!-- #region pycharm={"name": "#%% md\n"} -->
## pyEconomy
<!-- #endregion -->

```python pycharm={"name": "#%%\n"}
"""
This experimental notebook executes a single simulation of a virtual economy and
visualizes the results.
"""

# Imports
import matplotlib.pyplot as plt
import numpy as np
import quantecon as qe
from pyeconomy import simulator as sim
from pyeconomy import population as pop

# Configuration
DATA_PATH = "../data/"
CSV_PATH = DATA_PATH + "simulation.csv"
EXPORT_RESULTS = True

POPULATION_SIZE=1000
NUMBER_OF_ROUNDS=50

CURRENT_INCOME=100.0
EXPECTED_RISE_MEAN=0.01
EXPECTED_RISE_SD=0.2
CURRENT_SAVINGS=0.0
SAVING_RATE=0.05
INTEREST_RATE=0.05

# Create population
population = pop.create_population(
    current_income=CURRENT_INCOME,
    expected_rise_mean=EXPECTED_RISE_MEAN,
    expected_rise_sd=EXPECTED_RISE_SD,
    current_savings=CURRENT_SAVINGS,
    saving_rate=SAVING_RATE,
    interest_rate=INTEREST_RATE,
    size=POPULATION_SIZE
)

# Execute simulation
result_frame = sim.simulate_n_rounds(NUMBER_OF_ROUNDS, population)

# Print configuration
print("Population size:", POPULATION_SIZE, " Number of Rounds:", NUMBER_OF_ROUNDS, "\n")
```

<!-- #region pycharm={"name": "#%% md\n"} -->
## Development
<!-- #endregion -->

```python pycharm={"name": "#%%\n"}
population_mean = result_frame.groupby(by=["round"]).mean()

# Population income
plt.figure()
plt.title("Income avg")
plt.plot(population_mean["current_income"])

# Population income
plt.figure()
plt.title("Savings avg")
plt.plot(population_mean["current_savings"])

plt.show()
```

## Income distribution

```python pycharm={"name": "#%%\n"}
result_frame_final = result_frame[result_frame["final"]]
income_array = np.array(result_frame_final["current_income"])

# Plot Lorenz curve
f_vals, l_vals = qe.lorenz_curve(income_array)

fig, ax = plt.subplots()
ax.plot(f_vals, l_vals, label='Income')
ax.plot(f_vals, f_vals)
ax.legend()

# Plot histogram
plt.figure()
plt.title("Income distribution")
plt.hist(result_frame_final["current_income"])

plt.show()

# Print Statistics
print("Gini:", qe.gini_coefficient(income_array), "\n")
print("Mean:", result_frame_final["current_income"].mean())
print("Median:", result_frame_final["current_income"].median())
print("Min:", result_frame_final["current_income"].min())
print("Max:", result_frame_final["current_income"].max())
```

## Savings distribution

```python pycharm={"name": "#%%\n"}
savings_array = np.array(result_frame_final["current_savings"])

# Plot Lorenz curve
f_vals, l_vals = qe.lorenz_curve(savings_array)

fig, ax = plt.subplots()
ax.plot(f_vals, l_vals, label='Savings')
ax.plot(f_vals, f_vals)
ax.legend()

# Plot histogram
plt.figure()
plt.title("Savings distribution")
plt.hist(result_frame_final["current_savings"])

plt.show()

print("Gini:", qe.gini_coefficient(savings_array), "\n")
print("Mean:", result_frame_final["current_savings"].mean())
print("Median:", result_frame_final["current_savings"].median())
print("Min:", result_frame_final["current_savings"].min())
print("Max:", result_frame_final["current_savings"].max())
```

## Rich vs poor

```python pycharm={"name": "#%%\n"}
# Get max and min income
max_income_index = result_frame_final["current_income"].idxmax()

max_income_id = int(result_frame_final[
    result_frame_final.index == max_income_index]["citizen_id"])

max_income_series = result_frame[
    result_frame["citizen_id"] == max_income_id]["current_income"]

min_income_index = result_frame_final["current_income"].idxmin()

min_income_id = int(result_frame_final[
    result_frame_final.index == min_income_index]["citizen_id"])

min_income_series = result_frame[
    result_frame["citizen_id"] == min_income_id]["current_income"]

# Get max and min savings
max_savings_index = result_frame_final["current_savings"].idxmax()

max_savings_id = int(result_frame_final[
    result_frame_final.index == max_savings_index]["citizen_id"])

max_savings_series = result_frame[
    result_frame["citizen_id"] == max_savings_id]["current_savings"]

min_savings_index = result_frame_final["current_savings"].idxmin()

min_savings_id = int(result_frame_final[
    result_frame_final.index == min_savings_index]["citizen_id"])

min_savings_series = result_frame[
    result_frame["citizen_id"] == min_savings_id]["current_savings"]

# Plot income
plt.figure()
plt.title("Income max vs. min")
plt.plot(max_income_series, label="max income")
plt.plot(min_income_series, label="min income")
plt.legend()

# Plot savings
plt.figure()
plt.title("Savings max vs. min")
plt.plot(max_savings_series, label="max savings")
plt.plot(min_savings_series, label="min savings")
plt.legend()

plt.show()

```

```python pycharm={"name": "#%%\n"}
# Export results
if EXPORT_RESULTS:
    result_frame.to_csv(CSV_PATH, index=False)
```
