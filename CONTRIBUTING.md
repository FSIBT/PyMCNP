# Contributing to PyMCNP

We are happy when people submit issues and pull requests, and we welcome
contributions of code, tests, documentation, and example files. Please follow the
[Code of Conduct](CODE_OF_CONDUCT.md).

## MCNP input files that don't work

We especially welcome MCNP input files that PyMCNP can't handle, whether it fails
to parse them or fails to visualize them. MCNP has a very large number of options,
and PyMCNP does not cover all of them yet. We are happy to improve coverage, and to
provide extra support if you need a particular feature to make use of PyMCNP. Just
tell us what you are trying to do.

Inputs that MCNP rejects after a PyMCNP round trip are also very useful.

## Reporting bugs and requesting features

Report issues on [GitHub](https://github.com/FSIBT/PyMCNP/issues) with a small,
working example that reproduces the problem. Trim your input down to the few cards
that trigger it where you can. Please include:

- the PyMCNP version and Python version (`pip show pymcnp`, `python --version`),
- the MCNP version that produced or consumes the file (we mostly test MCNP 6.1, and have started testing 6.3),
- the full traceback or the unexpected output.

Please remove anything export-controlled or otherwise sensitive before attaching a file.

## Setting up

We recommend [uv](https://docs.astral.sh/uv/); the pip equivalents work too.

    git clone https://github.com/FSIBT/PyMCNP
    cd PyMCNP
    uv venv
    source .venv/bin/activate
    uv pip install -e .[dev,test,docs]
    pre-commit install

Code must work on the minimum Python version PyMCNP supports (`requires-python` in
`pyproject.toml`, currently 3.11), so don't use syntax or standard-library features
that are newer. CI tests Python 3.11 to 3.14.

## Making a change

1. Open an issue first for anything larger than a small fix, so we can agree on the approach.
2. Create a branch from `main`.
3. Keep commits small and focused, one logical change each, with a message that says why.
4. Add or update tests and docs along with the code.
5. Add an entry to [CHANGELOG.md](CHANGELOG.md) (under an `Unreleased` heading) for user-visible changes.
6. Open a pull request against `main` and describe what changed and how you checked it.

## Code style

Pull requests must pass [ruff](https://docs.astral.sh/ruff/) with the same rules we use.
The ruff version is pinned and the rules are configured in `pyproject.toml` (single
quotes, 200-column lines), so local and CI results agree. Installing the `dev` extra and
running `pre-commit install` applies them automatically.

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
