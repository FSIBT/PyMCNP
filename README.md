[![Documentation Status](https://readthedocs.org/projects/pymcnp/badge/?version=latest)](https://pymcnp.readthedocs.io/en/latest/?badge=latest)
[![PyPI version](https://badge.fury.io/py/pymcnp.svg)](https://badge.fury.io/py/pymcnp)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)

# PyMCNP

PyMCNP supports running [Monte Carlo N-Particle (MCNP) simulations](https://mcnp.lanl.gov/). It parses MCNP files, enabling automation such as parameter scans, creates MCNP geometry visualization using [pyvista](https://pyvista.org). PyMCNP provides a Python API for MCNP input and output files and a command line interface for interacting with MCNP and MCNP files.

Find more information on [ReadTheDocs](https://pymcnp.readthedocs.io).

## Installation

PyMCNP is available on [PyPI](https://pypi.org/project/pymcnp/) and can be "pip installed":

    pip install pymcnp

## Contributing

PyMCNP source code is accessable for contributions, suggestions, and bug reports on [GitHub](https://github.com/FSIBT/PyMCNP):

    # Installing
    git clone https://github.com/FSIBT/PyMCNP
    cd PyMCNP
    pip install -e .

    # Running
    pymcnp

To contribute, use [pre-commit](https://pre-commit.com) and [ruff](https://docs.astral.sh/ruff/):

    # Installing
    pip install pre-commit ruff
    cd PyMCNP
    pre-commit install

    # Running
    pre-commit

## Testing

To run the PyMCNP test suite, after cloning the PyMCNP GitHub repository, use the following commands to install [pytest](https://docs.pytest.org/en/stable/) with [pytest-cov](https://pytest-cov.readthedocs.io/en/latest/) inside the PyMCNP directory:

    # Installing
    pip install pytest-cov
    cd PyMCNP
    python -m pytest

    # Running
    pytest --cov --cov-report term-missing:skip-covered

## Documenting

To rebuild the documentation using [Sphinx](https://www.sphinx-doc.org/en/master/) and [Napolean](https://www.sphinx-doc.org/en/master/usage/extensions/napoleon.html):

    # Installing
    pip install sphinx

    # Running
    cd docs
    make html

## Copyright and License

For copyright and license information, see the `COPYRIGHT` and `LICENSE` files in the top level directory.
