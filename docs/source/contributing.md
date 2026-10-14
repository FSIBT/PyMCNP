# Contributing

We welcome contributions to code, documentation, tests, and files,
just create a [GitHub issue](https://github.com/FSIBT/PyMCNP/issues).
Input files that PyMCNP fails to parse, or that MCNP rejects after a PyMCNP
round trip, are especially useful.

We recommend [uv](https://docs.astral.sh/uv/) for development. The pip
equivalents are given alongside.

## Contributing

PyMCNP source code is accessible for contributions, suggestions, and
bug reports on [GitHub](https://github.com/FSIBT/PyMCNP):

    # Installing
    git clone https://github.com/FSIBT/PyMCNP
    cd PyMCNP
    uv venv
    source .venv/bin/activate
    uv pip install -e .[dev]

    # Running
    pymcnp

With pip, replace `uv pip install` with `pip install` (after creating and
activating a virtual environment with `python -m venv .venv`).

To contribute, use [pre-commit](https://pre-commit.com) and
[ruff](https://docs.astral.sh/ruff/). These will be automatically
included when using the optional _dev_ dependency.

    # Installing
    cd PyMCNP
    pre-commit install

    # Running
    pre-commit run --all-files

## Testing

To run the PyMCNP test suite, after cloning the PyMCNP GitHub
repository, install [pytest](https://docs.pytest.org/en/stable/) and its
plugins inside the PyMCNP directory. This can be done automatically using the
_test_ dependency. By default coverage and testmon will be used with pytest,
and matplotlib uses the non-interactive `Agg` backend.

    # Installing
    cd PyMCNP
    uv pip install -e .[test]

    # Running
    python -m pytest

    # Running with a coverage report
    python -m pytest --cov --cov-report term-missing:skip-covered

## Documenting

To rebuild the documentation using
[Sphinx](https://www.sphinx-doc.org/en/master/) and
[Napoleon](https://www.sphinx-doc.org/en/master/usage/extensions/napoleon.html).
This can be done automatically using the _docs_ dependency.

    # Installing
    uv pip install -e .[docs]

    # Running
    cd docs
    make html
