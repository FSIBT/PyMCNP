[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

# MCNP-tools
Python tools for MCNP.

# Development

For a local install and for development, use

  python -m pip install -e .

inside the top level of the git repository (where the pyproject.toml file is located)

Also install pre-commit via

1) python -m pip install pre-commit
2) pre-commit install

## Running tests
  Test can be run from the main directory using:

  python -m pytest --cov=mcnptools

# Related packages

- "Official" mcnptools from LANL. [github](https://github.com/lanl/mcnptools), [docs](https://www.osti.gov/biblio/1884737). This includes a C-implementation of a ptrac parser.
- Material library that can output MCNP code. [github](https://github.com/fusion-energy/neutronics_material_maker)
- A python based MCNP input file parser. [github](https://github.com/ENEA-Fusion-Neutronics/MCNP-Input-Reader)
- Merging and splitting input files. [github](https://github.com/MC-kit/mckit)
- Tools for several simulations packages including MCNP. [github](https://github.com/kbat/mc-tools/tree/master)
