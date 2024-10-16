[![Documentation Status](https://readthedocs.org/projects/pymcnp/badge/?version=latest)](https://pymcnp.readthedocs.io/en/latest/?badge=latest)

# PyMCNP

PyMCNP enables research with Monte Carlo N-Particle (MCNP) simulations. It parses MCNP files, creates MCNP geometry visualization, and runs MCNP in parallel. PyMCNP provides a Python API for MCNP input and output files and a command line interface for interacting with MCNP and MCNP files.

Find more information on [ReadTheDocs](https://pymcnp.readthedocs.io).

## Installation

PyMCNP requires [Python](https://www.python.org>) (≥ 3.10) and [Numpy](https://numpy.org>) (≥ 2.0).

PyMCNP is distributed through the [Python Package Index](https://pypi.org/project/pymcnp/>) (PyPi) with the ``pip`` command. The following command installs both ``pymcnp`` and its depenencies:

```
pip install numpy pymcnp
```

PyMCNP source code is accessable for contributions, suggestions, and bug reports on [GitHub](https://github.com/FSIBT/PyMCNP) with the ``git`` command. The following command downloads PyMCNP source code and installs ``pymcnp`` and its dependencies in editable mode:

```
git clone https://github.com/FSIBT/PyMCNP
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
