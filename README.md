# PyMCNP

PyMCNP enables research with Monte Carlo N-Particle (MCNP) simulations. It parses MCNP files, creates MCNP geometry visualization, and runs MCNP in parallel. PyMCNP provides a Python API for MCNP input and output files and a command line interface for interacting with MCNP and MCNP files.

Find more information on [ReadTheDocs](https://github.com/mauricioAyllon/PyMCNP).

## Installation

To download PyMCNP, (1) clone PyMCNP from [Github](https://github.com/mauricioAyllon/PyMCNP) by running the following `git` command, and (2) run the following `pip` command inside a clone of the pymcnp repository:

```
git clone https://github.com/mauricioAyllon/PyMCNP
cd PyMCNP
pip install -e .
```

## Testings

To run the PyMCNP testing suite, after clone the PyMCNP GitHub repository, use the following commands to install Hypothesis ([ReadTheDocs](https://hypothesis.readthedocs.io/en/latest/quickstart.html#installing])) and Pytest ([Docs](https://docs.pytest.org/en/stable/)) inside the PyMCNP directory:

```
cd PyMCNP
pip install pytest hypothesis
```

After instaling `pytest` and `hypothesis`, test the `pymcnp` package by calling the following commands inside the PyMCNP directory:

```
cd PyMCNP
pytest --verbose
```

## Copyright and License

For copyright and license infromation, see the `COPYRIGHT` and `LICENSE` files in the top level directory.
