# pyeconomy: Python economic simulator

## What is it?
This Python library simulates a virtual economy with the aim of 
studying the inequality of income and wealth in societies.

## Main Features
The library provides two modules:
- [population](pyeconomy/population.py) - classes and functions to model the population of the virtual economy
- [simulator](pyeconomy/simulator.py) - methods to setup and execute the simulator

The project furthermore offers [jupyter notebooks](notebooks) for running the simulator and
studying the results. The notebooks are stored as [markdown](https://en.wikipedia.org/wiki/Markdown) 
files to support efficient versioning in git. The synchronization between markdown files and ipynb files 
is handled by the framework [jupytext](https://github.com/mwouts/jupytext) 
(for further instructions see below).

## Where to get it
The source code is currently hosted on GitHub at:
https://github.com/c4ristian/pyeconomy

## Setup
```sh
conda env create -f environment.yml

conda activate pyeconomy
```

## Run Tests
```sh
pytest
```

## Code Coverage
```sh
pytest --cov
```

## Code Quality
```sh
pylint FILENAME.py
```

## Jupyter
### Sync Notebooks
```sh
jupytext --sync notebooks/*.md
```

### Pair Notebook
```sh
jupytext --set-formats ipynb,md notebooks/NOTEBOOK.ipynb
```

### Install Kernel 
```sh
python -m ipykernel install --user --name=pyeconomy
```

### Run Notebooks
```sh
jupyter notebook --notebook-dir="./notebooks"
```

## License
[Apache 2.0](LICENSE.txt)
