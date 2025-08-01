# Contributing

We welcome contributions to code, documentation, tests, and files, just create a [GitHub issue](https://github.com/FSIBT/PyMCNP/issues).

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
