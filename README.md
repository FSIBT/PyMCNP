[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

# MCNP-tools
Python tools for MCNP

# Development

For a local install and for development, use

  pip install -e .

inside the top level of the git repository (where the setup.py file is located)

Also install pre-commit via

1) pip install pre-commit
2) pre-commit install

## Running tests
  Test can be run from the main directory using:

  python -m pytest --cov=mcnptools

