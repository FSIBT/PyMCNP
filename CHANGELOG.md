# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

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
