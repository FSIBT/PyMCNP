# Contributing

We welcome contributions to code, documentation, tests, and files,
just create a [GitHub issue](https://github.com/FSIBT/PyMCNP/issues).

## Contributing

PyMCNP source code is accessible for contributions, suggestions, and
bug reports on [GitHub](https://github.com/FSIBT/PyMCNP):

    # Installing
    git clone https://github.com/FSIBT/PyMCNP
    cd PyMCNP
    pip install -e .[dev]

    # Running
    pymcnp

To contribute, use [pre-commit](https://pre-commit.com) and
[ruff](https://docs.astral.sh/ruff/). These will be automatically
included when using the optional _dev_ dependency.

    # Installing
    cd PyMCNP
    pre-commit install

## Testing

To run the PyMCNP test suite, after cloning the PyMCNP GitHub
repository, use the following commands to install
[pytest](https://docs.pytest.org/en/stable/) with
[pytest-cov](https://pytest-cov.readthedocs.io/en/latest/) inside the
PyMCNP directory. This can be done automatically using the _test_
dependency. By default coverage and testmon will be used with pytest.

    # Installing
    cd PyMCNP
    pip install -e .[test]
    python -m pytest

    # Running
    pytest --cov --cov-report term-missing:skip-covered

## Documenting

To rebuild the documentation using
[Sphinx](https://www.sphinx-doc.org/en/master/) and
[Napolean](https://www.sphinx-doc.org/en/master/usage/extensions/napoleon.html). This
can be done automatically using the _doc_ dependency. 

    # Installing
    pip install -e .[doc]

    # Running
    cd docs
    make html
