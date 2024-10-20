[![Documentation Status](https://readthedocs.org/projects/pymcnp/badge/?version=latest)](https://pymcnp.readthedocs.io/en/latest/?badge=latest)
[![PyPI version](https://badge.fury.io/py/pymcnp.svg)](https://badge.fury.io/py/pymcnp)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)

# PyMCNP

PyMCNP supports running [Monte Carlo N-Particle (MCNP) simulations](https://mcnp.lanl.gov/). It parses MCNP files, enabling automation such as parameter scans, creates MCNP geometry visualization using [cadquery](https://cadquery.readthedocs.io/en/latest/), and can run MCNP in parallel across multiple machines (including support for clusters). PyMCNP provides a Python API for MCNP input and output files and a command line interface for interacting with MCNP and MCNP files.

Find more information on [ReadTheDocs](https://pymcnp.readthedocs.io).

## Installation

PyMCNP is available on [PyPI](https://pypi.org/project/pymcnp/) and can be `pip installed`.

    pip install pymcnp

## Contributing

PyMCNP source code is accessable for contributions, suggestions, and bug reports on [GitHub](https://github.com/FSIBT/PyMCNP). The following command downloads PyMCNP source code and installs `pymcnp` and its dependencies in editable mode:

    git clone https://github.com/FSIBT/PyMCNP
    cd PyMCNP
    pip install -e .


If you plan to contribute, you should also enable `pre-commit`

    pip install pre-commit
    # cd into repo
    pre-commit install

from within the top level directory in the git repository.

## Testings

To run the PyMCNP test suite, after clone the PyMCNP GitHub repository, use the following commands to install Pytest ([Docs](https://docs.pytest.org/en/stable/)) inside the PyMCNP directory:

    pip install pytest

After instaling `pytest`, test the `pymcnp` package by calling the following commands inside the PyMCNP directory:

    cd PyMCNP
    python -m pytest

## Copyright and License

For copyright and license infromation, see the `COPYRIGHT` and `LICENSE` files in the top level directory.
