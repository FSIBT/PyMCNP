# Contributing

We welcome contributions. Either in code, documentation, or input
files that do not currenlty work with PyMCNP.

The best way to connect with us is to create a github issue.


## Installing

PyMCNP source code is accessable for contributions, suggestions, and bug reports on [GitHub](https://github.com/FSIBT/PyMCNP). The following command downloads PyMCNP source code and installs `pymcnp` and its dependencies in editable mode:

    git clone https://github.com/FSIBT/PyMCNP
    cd PyMCNP
    pip install -e .

## Code formatting, pre-commit, etc.

If you plan to contribute, you should also enable `pre-commit`

    pip install pre-commit
    # cd into repo
    pre-commit install

from within the top level directory in the git repository. Pre-commit will ensure that the code is formatted using ruff and that it will match the coding style in our repository.

We are happy to receive pull requests on github.

## Testings

To run the PyMCNP test suite, after clone the PyMCNP GitHub repository, use the following commands to install Pytest ([Docs](https://docs.pytest.org/en/stable/)) inside the PyMCNP directory:

    pip install pytest

After instaling `pytest`, test the `pymcnp` package by calling the following commands inside the PyMCNP directory:

    cd PyMCNP
    python -m pytest


