# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2026-11-25

### Added
- `Outp.summary` (`outp.Summary`): version, histories, run time, termination, `keff`, warnings, fatal errors and the statistical checks of each tally.
- `Outp.fatal_errors`, `Outp.activity(particle)` (print table 126 as a dataframe) and `Outp.tally(number)` with typed columns. `Outp.tallies()` and `Outp.activities()` return the parsed blocks.
- `Meshtal.iter_tallies` for meshtal files with several mesh tallies, which `from_file` silently truncated; `Meshtal.to_dataframe` with float columns; `Meshtal.tally_number` (`int`), `particle_name` (`str`) and `names` (list of `str`).
- PTRAC streaming on the event-block parser: `Ptrac.stream`, `Ptrac.iter_histories` (yields `ptrac.block.History` or `ptrac.block.HistoryTruncated`), `Ptrac.tracks` (particle tracks linked to their parents and originating nuclide), `Ptrac.to_parquet` (chunked, with filters), `Ptrac.to_dataframe` with typed columns including `track` and `parent_zaid`, and `ptrac.Event`, `ptrac.Track`, `ptrac.EventType`, `ptrac.Particle`, `ptrac.Surface`. Event values such as the particle type, cell and material are found by the variable IDs of the PTRAC header, or, without a header, by the event block's field names. `PtracFilter.run` and `PtracProcessor.run` accept a path.
- A PTRAC file cut short, e.g., by a killed MCNP run, keeps its truncated last history with an `abc.Warning`; damage before the final event still raises. `Ptrac.from_file` leaves a truncated last history in the remainder, so use `stream` or `iter_histories` for such files.
- `abc.Warning`, the warning category of PyMCNP; warnings use Python's standard `warnings.showwarning`, and PyMCNP installs no global hook.
- Iterative parsing mixins (`abc.file.WithMcnpIter`, `abc.file.WithDataIter`) with `from_mcnp_iter`, `from_file_iter` and `to_dataframe_iter`. The iterators yield the parsed items, e.g., `meshtal.line.Row`, or for PTRAC one generator of `ptrac.block.Event`s per history, and return `(obj, remainder)`.
- `Inp.cell_cards`, `Inp.surface_cards` and `Inp.data_cards` filter cards by number, material, density or kind, e.g., `inp.surface_cards(99)[0]` and `inp.cell_cards(material=2)`.
- `scan` and `scan_with` on all nonterminals, e.g., `inp.scan(nps=[...], seed=[...])`, for independent copies in parameter scans. In `Inp` scan paths, the index into `cells`, `surfaces` or `data` counts cards and skips comment cards: `inp.scan(**{'surfaces[0].r': [...]})` changes the first surface card, while `inp.surfaces[0]` may be a comment card. A scanned `title` value gets a trailing newline if it has none.
- `Array.filter(*kinds, **fields)` selects the items of an array by type and field values, skipping items that lack the field.
- Field values and `abc.Array` items, set by index, slice, `append`, `insert`, `extend`, `+=` or a scan path such as `data[0].e[1]`, are converted to the field's or item's type as text, numbers (NumPy scalars included) or symbols, e.g., `card.e[1] = 2` stores `inp.literal.Real('2')`; invalid values, `None` included, raise `abc.Error`. Array mutators and deep copies keep the spaces between items in step, so `to_mcnp` writes one space between new items.
- `Outp`, `Meshtal` and `Ptrac` are `abc.File`s with the `abc.file.WithDataIter` mixin: `to_dataframe`, `to_dataframe_iter`, `to_file_csv` and `to_file_parquet`.
- `Run`: per-run directories, worker limit, run names, `Result` objects with `fatal_errors`, `batch=False` and `Run.directory`.
- The FM tally multiplier card, and `M.from_formula` library suffixes.
- `SKILL.md`, which describes PyMCNP to AI coding agents, and examples 01 (PTRAC to parquet) and 02 (loop-built ground model with a flux plot).

### Changed
- **Breaking:** `Visualize` and `Plot` take their data in the call: `pymcnp.Visualize().to_show_surfaces(inp)` instead of `pymcnp.Visualize(inp).to_show_surfaces()`, and `pymcnp.Plot().to_pdf(outp, '1', path)` instead of `pymcnp.Plot(outp).to_pdf('1', path)`. Tally, cell and surface numbers may be given as `int` or `str`.
- **Breaking:** `Inp`, `Outp`, `Meshtal` and `Ptrac` `from_mcnp` and `from_file` return `(obj, remainder)` instead of the object; check that the remainder is empty.
- **Breaking:** `Run(inps=...)` is `Run(files=...)`; `Run.run` returns a list of `Result` instead of the batch directory (now in `Run.directory`), and `posthook_file(path, index)` is `posthook_file(result)`.
- **Breaking:** the INP card classes moved from `pymcnp.inp` (`inp.Cell`, `inp.Arb`, `inp.Nps`, ...) to `pymcnp.inp.card` (`card.Cell`, `card.surface.Arb`, `card.data.Nps`, ...), and their options to `pymcnp.inp.option`.
- **Breaking:** removed `pymcnp.errors` (`CliError`, `InpError`, ...); PyMCNP raises `pymcnp.abc.Error`. Removed `pymcnp.types`; the literals are in `pymcnp.inp.literal`.
- **Breaking:** removed `MeshtalFilter` and `MeshtalProcessor`.
- `Inp.to_mcnp` wraps card lines longer than 80 columns again.
- The test suite is much faster (sentinels, truncated PTRAC fixtures, a coarse visualization resolution), runs in temporary directories, and the rendering tests are marked `render`, which macOS CI skips.
- **Breaking:** `Outp.to_dataframe` returns one dataframe with a `number` column instead of a dictionary of dataframes.
- **Breaking:** removed `Convert`; use `to_file_csv` and `to_file_parquet`. `pymcnp convert` is now `pymcnp convert outp|ptrac|meshtal (--csv | --parquet) <file>` and converts the whole file; for meshtal files every mesh tally, with a `number` column for the tally number, as in `Outp.to_dataframe`.
- **Breaking:** the PTRAC `I`, `J`, `N` and `P` lines are replaced by `ptrac.block.History` fields and event blocks named after the MCNP manual's variables (`EventSource_1`, ..., `EventTermination_4`), picked by the event type announced on the previous line.
- **Breaking:** OUTP blocks are now `Header`, `Footer`, `Activity` (`NeutronActivity`, `PhotonActivity`), and `Tally` (`TallySurface`, `TallyAngle`, `TallyCell`); the `Tally_0` to `Tally_7` blocks are gone.
- **Breaking:** the `value` of the PTRAC card's `EVENT` option (`inp.option.data.ptrac.Event`) is an `abc.Array` of event types instead of an `abc.Terminal` string, so that `EVENT=SRC,COL,BNK` keeps every value; use `[str(v) for v in option.value]` or `option.value.to_mcnp()`.
- **Breaking:** `PtracProcessor.run` returns the results of the `process_*` methods; a `Run` result without an output file is not `ok`.
- The `pymcnp` command prints Python warnings, e.g., "Tally not parsed." or "Line exceeds 80 characters maximum length", as warning panels, like its own messages, instead of Python's format with the source line; `pymcnp check` and `Check` report each wide line once, with its line number, and `check --fix` only the lines it cannot shorten.
- `pymcnp run`, `visualize`, `convert` and `plot` ignored the part of a file PyMCNP cannot parse, e.g., a card and every card after it. They now warn, naming the line where parsing stopped, and exit with 3, as `pymcnp check` does; `run` runs nothing, and the others draw, write or plot what was parsed before that part.
- `pymcnp check --fix` exits with 1 and reports each line it cannot shorten, e.g., a full-line or `$` comment over 80 columns, instead of printing "Done!" and exiting with 0; `Check.fix` returns the problems left in the fixed file.
- Depends on `pyarrow` instead of `fastparquet`, and on `docopt-ng` instead of `docopt`.
- Python 3.15 is supported, now that `vtk` has wheels for it.
- Parsing time is linear in file size; it was quadratic, which made large OUTP, MESHTAL and PTRAC files very slow. E.g., `Ptrac.from_file` of a 1.1 MB file takes 0.3 s instead of 3.6 s, and `Meshtal.from_file` of a 3.3 MB file 0.5 s instead of 2.7 s. `Ptrac.to_dataframe` builds one dataframe for all histories; reading the same file and converting it with `to_dataframe` takes 0.35 s instead of 5.1 s.

### Fixed
- `pymcnp check` and `Check.problems` reported the wrong line for a card PyMCNP cannot parse when comment cards came first, e.g., line 2, the first comment, for every example input; and they passed a card that parsed only in part, or whose shorthands were not expanded. Comment cards are now skipped, and each card is parsed to its end with its shorthands expanded.
- `pymcnp visualize --pdf` names cell and surface PDFs `<input>-cell_100.pdf` (not `cell_['100']`) and prints where it wrote each PDF.
- `pymcnp convert`, `plot --pdf` and `visualize --pdf` crashed on a file name without an extension, e.g., MCNP's default `outp`, and wrote next to the directory for a dot only in a directory name, e.g., `run.csv` for `run.d/meshtal`; they now write, e.g., `outp.csv` and `run.d/meshtal.csv`.
- The hexagonal prism visualization mask, and the shape masks of `Visualize` (vectorized, with the sign convention of MCNP).
- `Visualize` drew a general plane `P A B C D` with `A`, `B` and `C` all non-zero centred at (0, 0, D), off the plane unless C is 1.
- `examples/`: `do_run.py`, `do_parameter_scan.py`, `do_check.py`, `read_ptrac.py`, the tally examples, and `script_example_01_ptrac_to_parquet.py` (which ignored its `path` argument) use the current API, and `tests/test_examples.py` runs them.
- `&` and `|` on surfaces and geometries were swapped.
- OUTP files whose footer was written to `runtpe`, ends with a newline, or is missing (runs that stopped early) did not parse.
- OUTP tally blocks in a layout PyMCNP cannot parse yet (e.g., F8, and some F1/F2/F4/F5 layouts) were dropped silently while the remainder stayed empty; `Outp.from_file` now issues an `abc.Warning` naming the file and each such tally's number and type, on every call, and `Outp.tally(number)` raises "Tally not parsed." for it instead of "Tally not found.".
- MESHTAL files: tally bin boundaries are required and data rows are parsed.
- PTRAC: every history is parsed, event types 2010, 2020 and 2030 are accepted, and macrobody facets work in the `SURFACE` option.
- The PTRAC card's `EVENT`, `CELL` and `SURFACE` options take several values separated by commas or spaces, e.g., `PTRAC EVENT=SRC,COL,BNK FILE=ASC`; they kept only the first value.
- `nI` and `nILOG` entries expand to the values between the endpoints, and `xM` entries (the previous entry times `x`, e.g., `e1 1 2m 3`) are read; they failed to parse.
- The shorthands `nR`, `nI`, `nJ` and `nLOG` were expanded in the title, comment cards, `$` comments and the text after the data block too, e.g., `c phys:n 50000 5j 4 100` became `c phys:n 50000 j j j j j 4 100`; that text is now kept as written.
- Input files with library keywords between substances, unindented continuation lines after `&`, thermal scattering names such as `h-zr.20t`, trailing spaces or comments at the ends of cards, or no final newline failed to parse.
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
