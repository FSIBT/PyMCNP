# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- `Outp.summary` (`outp.Summary`): version, histories, run time, termination, `keff`, warnings, fatal errors and the statistical checks of each tally.
- `Outp.fatal_errors`, `Outp.activity(particle)` (print table 126 as a dataframe), `Outp.tallies()` and `Outp.tally(number)` with typed columns.
- `Meshtal.iter_tallies` for meshtal files with several mesh tallies, which `from_file` silently truncated; `Meshtal.to_dataframe` with float columns.
- PTRAC streaming: `Ptrac.stream`, `Ptrac.iter_histories`, `Ptrac.tracks` (particle tracks linked to their parents and originating nuclide), `Ptrac.to_parquet` (chunked, with filters), and `ptrac.Event`, `ptrac.Track`, `ptrac.EventType`, `ptrac.Particle`, `ptrac.Surface`.
- `Inp.cell`, `surface`, `material` and `tally` lookups by number, and `Inp.cells_with_material`.
- `scan` and `scan_with` on all nonterminals, e.g., `inp.scan(nps=[...], seed=[...])`, for independent copies in parameter scans.
- `Outp`, `Meshtal` and `Ptrac` are `abc.DataFile`s with `to_dataframe`, `to_dataframe_iter`, `to_file_csv` and `to_file_parquet`.
- `Run`: per-run directories, worker limit, run names, `Result` objects with `fatal_errors`, `batch=False` and `Run.directory`.
- The FM tally multiplier card, and `M.from_formula` library suffixes.
- `SKILL.md`, which describes PyMCNP to AI coding agents, and examples 01 (PTRAC to parquet) and 02 (loop-built ground model with a flux plot).

### Changed
- **Breaking:** `Outp.to_dataframe` returns one dataframe with a `number` column instead of a dictionary of dataframes.
- **Breaking:** removed `Convert`; use `to_file_csv` and `to_file_parquet`. `pymcnp convert` is now `pymcnp convert outp|ptrac|meshtal (--csv | --parquet) <file>` and converts the whole file.
- **Breaking:** the PTRAC `I`, `J`, `N` and `P` lines are replaced by `ptrac.block.History` fields and event blocks named after the MCNP manual's variables (`EventSource_1`, ..., `EventTermination_4`), picked by the event type announced on the previous line.
- **Breaking:** OUTP blocks are now `Header`, `Footer`, `Activity` (`NeutronActivity`, `PhotonActivity`), and `Tally` (`TallySurface`, `TallyAngle`, `TallyCell`); the `Tally_0` to `Tally_7` blocks are gone.
- **Breaking:** `PtracProcessor.run` returns the results of the `process_*` methods; a `Run` result without an output file is not `ok`.
- Depends on `pyarrow` instead of `fastparquet`, and on `docopt-ng` instead of `docopt`.
- Parsing time is linear in file size; it was quadratic, which made large OUTP, MESHTAL and PTRAC files very slow.

### Fixed
- `&` and `|` on surfaces and geometries were swapped.
- OUTP files whose footer was written to `runtpe`, ends with a newline, or is missing (runs that stopped early) did not parse.
- MESHTAL files: tally bin boundaries are required and data rows are parsed.
- PTRAC: every history is parsed, event types 2010, 2020 and 2030 are accepted, and macrobody facets work in the `SURFACE` option.
- `nI` and `nILOG` entries expand to the values between the endpoints.
- Input files with library keywords between substances, unindented continuation lines after `&`, thermal scattering names such as `h-zr.20t`, trailing spaces or comments at the ends of cards, or no final newline failed to parse.
- `Array.append` added a space before the first item, and deep copies lost or duplicated array spaces.
- Tests no longer write files into the repository.

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
