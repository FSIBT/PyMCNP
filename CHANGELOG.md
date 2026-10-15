# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.10.0] - 2026-10-15

### Added
- `pymcnp check` reports lines wider than 80 columns as errors and the first card PyMCNP cannot parse as a warning, with line numbers. Checking stops at that card, so rerun it after fixing.
- `pymcnp check --diff` shows the changes `--fix` would make.
- `pymcnp visualize --cells-skip` and `--surfaces-skip` also work with `--pdf`.
- `CONTRIBUTING.md`, now also used for the documentation's contributing page.
- Roundtrip tests for the example inputs, including a run through MCNP when `mcnp6` is installed.
- Continuous integration builds the package (with `twine check`) and the documentation.

### Changed
- **Breaking:** `pymcnp check` exit codes: lines over 80 columns exit 1, files PyMCNP cannot parse exit 3, and a bad path exits 2. `--fix` no longer rewrites a file PyMCNP cannot parse.
- **Breaking:** `Integer` fields reject non-integral values such as `2.5` instead of truncating them.
- **Breaking:** removed the unused `Tally_8` block, superseded by `Tally_8A` and `Tally_8B`.
- Written cards wrap at 80 columns with `&` continuation and a 5-space indent.
- Surface tally facets (`F1:p 2.1`), the F5 ring radius, and the PTRAC `NSF` field are read as reals.
- `INP`, `OUTP`, `PTRAC` and `MESHTAL` attributes are `Field` descriptors, and shared behaviour moved into base classes.
- Geometry and surface operators follow MCNP semantics, and `BOX` vectors are checked for orthogonality.
- `pymcnp check`, `plot`, `run`, `convert` and `visualize` usage lines put options first.
- Python 3.11 to 3.14 are supported. Python 3.15 is not yet, because `vtk` (through `pyvista`) has no wheels for it.
- Ruff is pinned to 0.17.0 with an explicit rule list, and the example inputs are valid MCNP.
- Documentation recommends `uv`, and the active-development warnings were removed.

### Fixed
- Cell and material options were silently dropped when parsing `INP`.
- Vertical-data rows whose length differed from the header were accepted.
- `pymcnp visualize` had ambiguous short options, did not validate cell and surface numbers, and wrote the cell PDF for `--surface --pdf`.
- Previews of the Plane, Ellipsoid, unbounded cylinder, torus, truncated cone, wedge and hexagonal cylinder shapes were wrong or inverted.
- The MCNP torus card parameters were mapped to the wrong axes.
- Material cards with library keywords such as `plib` between substances failed to parse (#7).

## [0.9.0]  - 2025-12-01

### Fixed
- Fixed `INP` importance card, `imp`, validation.
- Fixed `OUTP` `1tally8` table parsing.

### Changed
- Refactored `INP` parser.
- Refactored `OUTP` parser.
- Refactored `PTRAC` parser.
- Refactored `utils` subpackage.
- Refactored `cli` subpackage.
- Updated documentation.
- Updated examples.

### Added
- Added `MESHTAL` parser.
- Added `pyvstia` surface visualizations.
- Added `pyvstia` cell visualizations.
- Added `MCNP` files for testing.
- Added full-coverage unit tests.

### Removed
- Removed `cadquery` surface visualizations.
- Removed `INP` card block classes.
- Removed `modify` function.

## [0.2.0]  - 2024-10-27

### Fixed
- Fixed `from_mcnp` and `to_mcnp` for several classes.
- Fixed pre-commit.
- Fixed CI.

### Added
- Added `INP` parsing tests.
- Added examples.
- Added `material.from_formula`.
- Added `modify` function to change `INP` objects.

### Changed
- Updated documentation.
- Updated `cli` subpackage.
- Imporved `__str__` and `__repr__` for several classes.

## [0.1.2]  - 2024-10-19

### Fixed
- Fixed automated release on `PyPI`.

## [0.1.1]  - 2024-10-19

Initial release. Not everything is working yet ;)
