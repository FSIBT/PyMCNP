[![Documentation Status](https://readthedocs.org/projects/pymcnp/badge/?version=latest)](https://pymcnp.readthedocs.io/en/latest/?badge=latest)
[![PyPI version](https://badge.fury.io/py/pymcnp.svg)](https://badge.fury.io/py/pymcnp)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)

# PyMCNP

PyMCNP supports running [Monte Carlo N-Particle (MCNP) simulations](https://mcnp.lanl.gov/). It parses MCNP files, enabling automation such as parameter scans, creates MCNP geometry visualization using [pyvista](https://pyvista.org). PyMCNP provides a Python API for MCNP input and output files and a command line interface for interacting with MCNP and MCNP files.

Find more information on [ReadTheDocs](https://pymcnp.readthedocs.io).

## Installation

PyMCNP is available on [PyPI](https://pypi.org/project/pymcnp/) and can be "pip installed":

    pip install pymcnp

PyMCNP supports Python 3.11 to 3.14. As of 2026-10-14, Python 3.15 does not work yet because a dependency, `vtk` (through `pyvista`), does not publish wheels for it.

## Contributing

Contributions are welcome: issues, pull requests, and in particular MCNP input files that PyMCNP fails to parse or visualize. See [CONTRIBUTING.md](CONTRIBUTING.md) for how to report bugs, set up a development environment, run the tests, and build the documentation.

## Copyright and License

For copyright and license information, see the `COPYRIGHT` and `LICENSE` files in the top level directory.
