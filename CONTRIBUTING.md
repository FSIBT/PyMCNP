# Contributing to PyMCNP

Thanks for your interest in PyMCNP. Contributions of code, tests, documentation,
and example files are welcome. Please follow the [Code of Conduct](CODE_OF_CONDUCT.md).

## Reporting bugs and requesting features

Open a [GitHub issue](https://github.com/FSIBT/PyMCNP/issues). For bugs, please include:

- the PyMCNP version and Python version (`pip show pymcnp`, `python --version`),
- the MCNP version that produced or consumes the file (we mostly test MCNP 6.1, and have started testing 6.3),
- a minimal input, output, or PTRAC snippet that reproduces the problem,
- the full traceback or the unexpected output.

Input files that PyMCNP fails to parse, or that MCNP rejects after a PyMCNP
round trip, are especially useful. Please remove anything export-controlled or
otherwise sensitive before attaching a file.

## Setting up

We recommend [uv](https://docs.astral.sh/uv/); the pip equivalents work too.

    git clone https://github.com/FSIBT/PyMCNP
    cd PyMCNP
    uv venv
    source .venv/bin/activate
    uv pip install -e .[dev,test,docs]
    pre-commit install

PyMCNP supports Python 3.11 to 3.14.

## Making a change

1. Open an issue first for anything larger than a small fix, so we can agree on the approach.
2. Create a branch from `main`.
3. Keep commits small and focused, one logical change each, with a message that says why.
4. Add or update tests and docs along with the code.
5. Add an entry to [CHANGELOG.md](CHANGELOG.md) (under an `Unreleased` heading) for user-visible changes.
6. Open a pull request against `main` and describe what changed and how you checked it.

## Code style

Style is enforced by [ruff](https://docs.astral.sh/ruff/), pinned to the version in
`pyproject.toml` so that local and CI results agree. Configuration lives in `pyproject.toml`
(single quotes, 200-column lines).

    ruff check .
    ruff format .
    pre-commit run --all-files

CI runs `ruff check` and `ruff format --check`, so run them before pushing.

Other conventions:

- Write comments only for non-obvious reasons, not to restate the code.
- Raise the exceptions from `pymcnp.errors` for parse and validation failures rather than bare `ValueError`.
- Input cards, options and types follow the existing `Field` descriptor pattern. Look at a neighbouring card before adding a new one.

## Testing

    python -m pytest

By default pytest runs with coverage and [testmon](https://github.com/tarpas/pytest-testmon),
which only reruns tests affected by your changes. Use `python -m pytest -o addopts=""` for a
plain full run. Tests live under `tests/test_pymcnp/` and mirror the layout of `src/pymcnp/`.

- New parsing or writing code needs tests for both `from_mcnp` and `to_mcnp`, including a round trip.
- Tests that write files must use pytest's `tmp_path`, never the working directory.
- Example inputs in tests, docs, and `examples/` should be valid MCNP, since people copy them.
- Fix bugs with a test that fails before the fix.

## Documentation

Docs are built with Sphinx from `docs/`:

    uv pip install -e .[docs]
    cd docs
    make html

Please document public classes and functions with docstrings. Keep claims in the docs
modest, and say which MCNP versions a feature was checked against.

## Licence

By contributing you agree that your contribution is licensed under the project's
[licence](LICENSE).
