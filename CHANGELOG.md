# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- The `mplot` data card (`inp.card.data.Mplot`), e.g., `mplot tal 4 freq 1000`; its plot commands are kept as words, without expanding shorthands.

### Fixed
- A card whose name starts in columns 2-5, e.g., `  100 0 1`, failed to parse ("Expected Cell"). One to four blanks before a card name start a card, as in MCNP, and five or more mark a continuation line. Lines indented by one to four blanks that PyMCNP read as continuation lines, which MCNP reads as new cards, now start a card too.
- An `sp` or `sb` card with a built-in function and fewer than two parameters, e.g., `sp1 -21 1` or `sp1 -5`, failed to parse; its parameters are optional, as in MCNP. Probabilities may exceed 1, as MCNP normalizes them: `sp1 0 2 3` was read as function 0 with parameters 2 and 3. A function number must be negative.

## [1.0.0] - 2026-11-26

### Added
- `Outp.summary` (`outp.Summary`): version, histories, run time, termination, `keff`, warnings, fatal errors and the statistical checks of each tally. `outp.block.Tally.tally_number` (`int`); the `number` and `nps` columns of `Outp.to_dataframe` are `int`.
- `Outp.fatal_errors`, `Outp.activity(particle)` (print table 126 as a dataframe) and `Outp.tally(number)` with typed columns. `Outp.tallies()` and `Outp.activities()` return the parsed blocks.
- `Meshtal.iter_tallies` for meshtal files with several mesh tallies, which `from_file` silently truncated; `Meshtal.to_dataframe` with float columns; `Meshtal.tally_number` (`int`), `nps` (`int`), `particle_name` (`str`) and `names` (list of `str`).
- PTRAC streaming on the event-block parser: `Ptrac.stream`, `Ptrac.iter_histories` (yields `ptrac.block.History` or `ptrac.block.HistoryTruncated`), `Ptrac.tracks` (particle tracks linked to their parents and originating nuclide), `Ptrac.to_parquet` (chunked, with filters), `Ptrac.to_dataframe` with typed columns including `track` and `parent_zaid`, and `ptrac.Event`, `ptrac.Track`, `ptrac.EventType`, `ptrac.Particle`, `ptrac.Surface`. Event values such as the particle type, cell and material are found by the variable IDs of the PTRAC header, or, without a header, by the event block's field names. `PtracFilter.run` and `PtracProcessor.run` accept a path (see Changed).
- `Ptrac.from_file`, `iter_histories` and `stream` choose the form of each event block (`EventSource_1`, ..., `EventTermination_4`) from the variable IDs of the PTRAC header instead of by trial, which makes parsing about 3 times faster. A header that fits none of the forms (with an `abc.Warning`), or lines that do not fit the header, fall back to trial parsing, longest match first, as `History.from_mcnp`, which has no header, always does; the `ptrac.block` field names may then not follow the header, while `stream` and `to_dataframe` still do.
- A PTRAC file cut short, e.g., by a killed MCNP run, keeps its truncated last history with an `abc.Warning`; damage before the final event still raises. `Ptrac.from_file` leaves a truncated last history in the remainder, so use `stream` or `iter_histories` for such files. `ptrac.block.HistoryTruncated.from_mcnp` returns `(obj, remainder)`, like every other `from_mcnp`; the remainder is the lines of the event that was cut short.
- `abc.Warning`, the warning category of PyMCNP; warnings use Python's standard `warnings.showwarning`, and PyMCNP installs no global hook.
- Iterative parsing mixins (`abc.file.WithMcnpIter`, `abc.file.WithDataIter`) with `from_mcnp_iter`, `from_file_iter` and `to_dataframe_iter`. The iterators yield the parsed items, e.g., `meshtal.line.Row`, or for PTRAC one generator of `ptrac.block.Event`s per history, and return `(obj, remainder)`.
- `Inp.cell_cards`, `Inp.surface_cards` and `Inp.data_cards` filter cards by number, material, density or kind, e.g., `inp.surface_cards(99)[0]` and `inp.cell_cards(material=2)`.
- `scan` and `scan_with` on all nonterminals, e.g., `inp.scan(nps=[...], seed=[...])`, for independent copies in parameter scans. In `Inp` scan paths, the index into `cells` or `surfaces` is the card number, e.g., `inp.scan(**{'surfaces[99].r': [...]})` changes surface 99, and a number no card has raises `abc.Error`; the index into `data` is the list position, as in `inp.data[i]`, comment cards included. A `title` value, given to `scan`, `Inp(title=...)` or `inp.title = ...`, gets the title card's trailing newline if it has none.
- `Array.filter(*kinds, **fields)` selects the items of an array by type and field values, skipping items that lack the field.
- Field values and `abc.Array` items, set by index, slice, `append`, `insert`, `extend`, `+=` or a scan path such as `data[0].e[1]`, are converted to the field's or item's type as text, numbers (NumPy scalars included) or symbols, e.g., `card.e[1] = 2` stores `inp.literal.Real('2')`; invalid values, `None` included, and text that parses only in part, e.g., `so.r = '7 8'` or a title of two lines, raise `abc.Error`; whitespace around a text value is dropped, e.g., `so.r = '7\n'` stores 7, and a float for an integer field, e.g., `so.j = 10.0`, raises rather than being rounded. Array mutators and deep copies keep the spaces between items in step, so `to_mcnp` writes one space between new items, and an array emptied by `clear` or `[:] = []` writes a card that parses back, e.g., `E0`.
- `Outp`, `Meshtal` and `Ptrac` are `abc.File`s with the `abc.file.WithDataIter` mixin: `to_dataframe`, `to_dataframe_iter`, `to_file_csv` and `to_file_parquet`.
- `Run`: per-run directories, worker limit, run names (without `& | < > ^ % ! "`, which `cmd.exe` would read when it runs a `.bat` or `.cmd` MCNP command on Windows), `Result` objects with `fatal_errors`, `batch=False` and `Run.directory`.
- The FM tally multiplier card, and `M.from_formula` library suffixes.
- A `py.typed` marker (PEP 561), so that type checkers such as mypy and pyright use PyMCNP's annotations.
- `pymcnp.abc`, the base classes of the parse tree (`Nonterminal`, `Terminal`, `Array`, `File`, ...) and the `Visualization` shapes; `Inp.comment_cards()`; `outp.TallyCheck`; `ptrac.tracks`, `ptrac.to_dataframe` and `ptrac.ParquetWriter`.
- `SKILL.md`, which describes PyMCNP to AI coding agents, and examples 01 (PTRAC to parquet) and 02 (loop-built ground model with a flux plot).

### Changed
- **Breaking:** `Visualize` and `Plot` take their data in the call: `pymcnp.Visualize().to_show_surfaces(inp)` instead of `pymcnp.Visualize(inp).to_show_surfaces()`, and `pymcnp.Plot().to_pdf(outp, '1', path)` instead of `pymcnp.Plot(outp).to_pdf('1', path)`. The cell and surface visualizations take the input first, then the numbers as arguments: `Visualize().to_show_cell(inp, 1, 2)` instead of `Visualize(inp).to_show_cell(('1', '2'))`, and `Visualize().to_pdf_cell(inp, path, 1)` instead of `Visualize(inp).to_pdf_cell('1', path)`: `to_pdf_cell` and `to_pdf_surface` had the number before the path. Tally, cell and surface numbers may be given as `int` or `str`.
- **Breaking:** `Inp`, `Outp`, `Meshtal` and `Ptrac` `from_mcnp` and `from_file` return `(obj, remainder)` instead of the object; check that the remainder is empty.
- **Breaking:** `Run(inps=...)` is `Run(files=...)`; `Run.run` returns a list of `Result` instead of the batch directory (now in `Run.directory`), and `posthook_file(path, index)` is `posthook_file(result)`.
- **Breaking:** the INP card classes moved from `pymcnp.inp` (`inp.Cell`, `inp.Arb`, `inp.Nps`, ...) to `pymcnp.inp.card` (`card.Cell`, `card.surface.Arb`, `card.data.Nps`, ...), and their options to `pymcnp.inp.option`.
- **Breaking:** removed `pymcnp.errors` (`CliError`, `InpError`, ...); PyMCNP raises `pymcnp.abc.Error`. Removed `pymcnp.types`; the literals are in `pymcnp.inp.literal`.
- **Breaking:** removed `MeshtalFilter` and `MeshtalProcessor`.
- **Breaking:** assigning an attribute that is not a field of a card or other nonterminal, e.g., `rpp.r = 5` on a box or the misspelt `rpp.x_min = 1`, raises `AttributeError` naming the fields, instead of being stored and ignored. Fields, `spaces`, settable properties such as `Inp.nps`, and names starting with `_` may be set.
- **Breaking:** every `pymcnp` command exits with the same codes, listed in `pymcnp help` and the CLI documentation: 0 success; 1 the input or output has problems or the command failed; 2 a usage error, or a file that does not exist, is a directory or is not a text file; 3 PyMCNP cannot parse all of a file. A file gets the same code from every command that reads it; an OUTP tally PyMCNP cannot parse yet is only a warning, unless it is the tally `plot` is asked for, or nothing is left to convert. 0.10's codes depended on the kind of error raised inside PyMCNP. Changes: an unknown option or command exits 2 (was 1); a run of MCNP that fails, e.g., with a non-zero exit code or no output file, exits 1 (was 0); an input that is not valid, e.g., two cells with one number, given to `run` or `visualize`, and a file of another kind given to `convert` or `plot`, exit 3 (were 1); an OUTP file whose tallies do not parse exits 3 from `convert` (was a traceback, exit 1) and from `plot` (was 2); a file PyMCNP parses only in part exits 3 from `run`, `visualize`, `convert` and `plot` (was 0), and `run` runs nothing; `check --fix` that cannot shorten a line exits 1 (was 0). The cases 0.10 got wrong, an MCNP command that is not found and a file that is not text or may not be read, are under Fixed. Unchanged: a file that does not exist or is a directory, and a cell or surface that is not in the file, exit 2; a card PyMCNP cannot parse exits 3 from `check`. Scripts that test exit codes must be checked.
- **Breaking:** `Check(path)` raises `abc.Error` ("File not found") for a file that does not exist, instead of `check()` and `problems()` raising `CliError` ("Bad path."). The `Problem.message` of a wide line reads "Line exceeds 80 characters maximum length (103 columns)." instead of "Line is 103 columns wide, MCNP reads at most 80.".
- **Breaking:** `Outp.to_dataframe` returns one dataframe with a `number` column instead of a dictionary of dataframes.
- **Breaking:** removed `Convert`; use `to_file_csv` and `to_file_parquet`. `pymcnp convert` is now `pymcnp convert outp|ptrac|meshtal (--csv | --parquet) <file>` and converts the whole file; for meshtal files every mesh tally, with a `number` column for the tally number, as in `Outp.to_dataframe`. It writes the file name plus `.csv` or `.parquet`, e.g., `run.outp.csv` and `run.ptrac.csv`, so that the OUTP and PTRAC files of one run do not write the same file, and writes nothing if there is nothing to convert.
- **Breaking:** the PTRAC `I`, `J`, `N` and `P` lines are replaced by `ptrac.block.History` fields and event blocks named after the MCNP manual's variables (`EventSource_1`, ..., `EventTermination_4`), picked by the event type announced on the previous line.
- **Breaking:** the OUTP classes were rebuilt. Removed: `outp.Mcnp`, `outp.ProblemSummary`, `outp.Tally_1A`, `Tally_1B`, `Tally_2`, `Tally_4`, `Tally_8A`, `Tally_8B` and the `outp.tally` package (`Subtally_1`, `Subtally_2`, `Subtally_4`, `Line`). `outp.NeutronActivity`, `PhotonActivity`, `AnalysisTallyFluctuation`, `StartingMcrun` and `UnnormedTallyDensity` moved to `outp.block`, where the tally blocks are `Tally` (`TallySurface`, `TallyAngle`, `TallyCell`); `outp.Header` stays and `outp.Footer` is new, and `Outp(header, blocks, footer)` has a `footer`.
- **Breaking:** `Meshtal` holds one mesh tally, as flat fields (`header`, `title`, `number`, `particle`, `bins`, `labels`, `rows`, ...), instead of `Meshtal(header, tallies)` with `.tallies`; `meshtal.Header` and `meshtal.Tally` are gone, `meshtal.block` and `meshtal.line` replace them, and `Meshtal.iter_tallies` reads files with several mesh tallies.
- **Breaking:** the PTRAC package was rebuilt: `ptrac.Header`, `ptrac.History`, `ptrac.Keyword`, `ptrac.header` and `ptrac.history` are now `ptrac.block.Header`, `ptrac.block.History` and the event blocks; `ptrac.Keyword` is removed. `Ptrac(header, histories)` keeps its two fields, but the histories are `ptrac.block.History`.
- **Breaking:** `PtracFilter()(file)` and `PtracProcessor()(file)` are `PtracFilter().run(file)` and `PtracProcessor().run(file)`; instances are no longer callable. The `check_*` and `process_*` hooks are instance methods taking a `ptrac.Event` (they were static methods taking a `ptrac.history.event.j.EventType`), e.g., `def check_collision(self, event): return event.cell == 4`.
- **Breaking:** the `value` of the PTRAC card's `EVENT` option (`inp.option.data.ptrac.Event`) is an `abc.Array` of event types instead of an `abc.Terminal` string, so that `EVENT=SRC,COL,BNK` keeps every value; use `[str(v) for v in option.value]` or `option.value.to_mcnp()`.
- **Breaking:** `PtracProcessor.run` returns the results of the `process_*` methods; a `Run` result without an output file is not `ok`.
- `Inp.to_mcnp` wraps card lines longer than 80 columns again.
- The test suite is much faster (sentinels, truncated PTRAC fixtures, a coarse visualization resolution), runs in temporary directories, and the rendering tests are marked `render`, which macOS and Windows CI skip.
- PyMCNP is tested on Windows as well as Linux and macOS (CI on `windows-latest`, Python 3.11 to 3.15). Files with Windows (CRLF) line ends are tested to read as their LF originals, for every fixture.
- The `pymcnp` command prints Python warnings, e.g., "Tally not parsed." or "Line exceeds 80 characters maximum length", as warning panels, like its own messages, instead of Python's format with the source line; `pymcnp check` and `Check` report each wide line once, with its line number, and `check --fix` only the lines it cannot shorten.
- `pymcnp run`, `visualize`, `convert` and `plot` ignored the part of a file PyMCNP cannot parse, e.g., a card and every card after it. They now warn, naming the line where parsing stopped, and exit with 3, as `pymcnp check` does; `run` runs nothing, and the others draw, write or plot what was parsed before that part.
- `pymcnp check --fix` exits with 1 and reports each line it cannot shorten, e.g., a full-line or `$` comment over 80 columns, instead of printing "Done!" and exiting with 0; `Check.fix` returns the problems left in the fixed file.
- Depends on `pyarrow` instead of `fastparquet`, and on `docopt-ng` instead of `docopt`.
- Python 3.15 is supported, now that `vtk` has wheels for it.
- Parsing time is linear in file size; it was quadratic, which made large OUTP, MESHTAL and PTRAC files very slow. E.g., `Ptrac.from_file` of a 1.1 MB file takes 0.1 s instead of 3.6 s, and `Meshtal.from_file` of a 3.3 MB file 0.5 s instead of 2.7 s. `Ptrac.to_dataframe` builds one dataframe for all histories; reading the same file and converting it with `to_dataframe` takes 0.15 s instead of 5.1 s.

### Fixed
- `pymcnp check`, and `Check.problems`, blamed the first card PyMCNP cannot parse even when the error came from before it, e.g., two cells with one number; they now report that error, for the file. `Plot.to_show` and `Plot.to_pdf` raise `abc.Error` "Tally not parsed." for a tally in a layout PyMCNP cannot parse yet, and "Tally not found." for a tally that is not in the file.
- `pymcnp help <unknown command>` printed "Unknown command" and exited 0; it now names the commands and exits 2.
- The `message:` block at the start of an input file, e.g., `message: outp=run.o` followed by a blank line, failed to parse. It ends at its first blank line, as in MCNP, is `Inp.message` (None without one), and is written back as it is. A message set as text, e.g., `inp.message = 'outp=run.o'`, gets the `message:` keyword if it has none and its blank line; one that holds a blank line raises `abc.Error`. 0.10 read only a one-line block followed directly by the title, which MCNP reads as part of the message, and wrote it without the `=` signs.
- Every command given a file that is not a text file, e.g., a binary PTRAC file, or a file that it may not read, ended in a Python traceback; it now prints an error, e.g., "not a text file (a NUL byte at byte offset 7)" (`convert ptrac` adds how to have MCNP write a text PTRAC file) or "cannot read the file: Permission denied.", and exits 2. `pymcnp visualize -c abc` says that it expects numbers instead of "no such cell: abc", and a directory is "not a file" instead of "Bad path.".
- `pymcnp visualize` of a surface PyMCNP cannot draw yet, e.g., GQ, ended in a Python traceback; it now prints "PyMCNP cannot visualize this geometry yet" with the surface type and exits 1. `Surface.to_show` raises `NotImplementedError` with the type's name.
- `pymcnp` messages lost text in square brackets, e.g., `[1 0 0]` of a card, which `rich` read as markup.
- `pymcnp run -c mcnp7` reported "Bad parameter." for a command that is not found, and exited 0; the error is now "MCNP command not found: mcnp7", with exit 1, and `Run(command=...)` raises `abc.Error` with that message.
- `pymcnp help convert` and the CLI manual page showed reST double backticks.
- `Inp.from_mcnp` and `Inp.from_file` raised `abc.Error` ("Expected Inp.blank_2") for a data card that parses only in part, e.g., `f4:n 1 [1]` or `df4 iu=1 ic=10`; that card and every card after it are now the remainder, as for any other data card PyMCNP cannot parse.
- `pymcnp check` and `Check.problems` reported the wrong line for a card PyMCNP cannot parse when comment cards came first, e.g., line 2, the first comment, for every example input; and they passed a card that parsed only in part, or whose shorthands were not expanded. Comment cards are now skipped, and each card is parsed to its end with its shorthands expanded.
- `pymcnp visualize --pdf` names cell and surface PDFs `<input>-cell_100.pdf` (not `cell_['100']`) and prints where it wrote each PDF.
- `pymcnp convert`, `plot --pdf` and `visualize --pdf` crashed on a file name without an extension, e.g., MCNP's default `outp`, and wrote next to the directory for a dot only in a directory name, e.g., `run.csv` for `run.d/meshtal`; they now write, e.g., `outp.csv` and `run.d/meshtal.csv`.
- The hexagonal prism visualization mask, and the shape masks of `Visualize` (vectorized, with the sign convention of MCNP).
- `Visualize` drew a general plane `P A B C D` with `A`, `B` and `C` all non-zero centred at (0, 0, D), off the plane unless C is 1.
- `examples/`: `do_run.py`, `do_parameter_scan.py`, `do_check.py`, `read_ptrac.py`, the tally examples, and `script_example_01_ptrac_to_parquet.py` (which ignored its `path` argument) use the current API, and `tests/test_examples.py` runs them. `do_run.py` and `do_parameter_scan.py` use `where` instead of `echo` on Windows, which has no `echo` program.
- `&` and `|` on surfaces and geometries were swapped.
- OUTP files whose footer was written to `runtpe`, ends with a newline, or is missing (runs that stopped early) did not parse.
- OUTP tally blocks in a layout PyMCNP cannot parse yet (e.g., F8, and some F1/F2/F4/F5 layouts) were dropped silently while the remainder stayed empty; `Outp.from_file` now issues an `abc.Warning` naming the file and each such tally's number and type, on every call, and `Outp.tally(number)` raises "Tally not parsed." for it instead of "Tally not found.".
- MESHTAL files: tally bin boundaries are required and data rows are parsed.
- PTRAC: every history is parsed, event types 2010, 2020 and 2030 are accepted, and macrobody facets work in the `SURFACE` option.
- The PTRAC card's `EVENT`, `CELL` and `SURFACE` options take several values separated by commas or spaces, e.g., `PTRAC EVENT=SRC,COL,BNK FILE=ASC`; they kept only the first value.
- `nI` and `nILOG` entries expand to the values between the endpoints, and `xM` entries (the previous entry times `x`, e.g., `e1 1 2m 3`) are read; they failed to parse.
- The shorthands `nR`, `nI`, `nJ` and `nLOG` were expanded in the title, comment cards, `$` comments and the text after the data block too, e.g., `c phys:n 50000 5j 4 100` became `c phys:n 50000 j j j j j 4 100`; that text is now kept as written.
- Input files with library keywords between substances, unindented continuation lines after `&`, thermal scattering names such as `h-zr.20t`, trailing spaces or comments at the ends of cards, or no final newline failed to parse.
- Subclasses of `Inp`, `Outp`, `Meshtal`, `Ptrac`, `ptrac.block.History` and the card classes are parsed as the subclass, e.g., `MyInp.from_file` returned an `Inp` for `class MyInp(pymcnp.Inp)`; they inherit the parent's fields, and a subclass that adds a field, or a class attribute or method named like an inherited field, now raises `abc.Error` (0.10 ignored it).
- Vertical data format (`#`) blocks lost cards: two blocks in a row dropped the cards after the second block and moved it after the data block, and rows indented with spaces shifted every value one column left. Rows may now be indented, hold one column, or start with a sign, a decimal point or `J`; a block whose rows do not have one entry per card name, carry a `$` comment, or hold a shorthand such as `2j` (a jump over two cards), is left in the remainder instead of being read wrong. A comment card between rows ends the block: the rows before it are read, and the rows after it are the remainder.
- `Check.fix` rewrote a file PyMCNP could parse only in part, dropping the unparsed card and every card after it, and then reported the shortened file as clean. It now raises `abc.Error`, naming the first line PyMCNP cannot parse, and leaves the file as it is, as `pymcnp check --fix` does.
- `Inp.to_mcnp` and `pymcnp check --fix` wrapped a long comment card indented in columns 2-5 with `&`, so its second half became a continuation line, and dropped the `&` at the end of a long line, so the line after it became a new card. Comment cards in columns 1-5 are written as they are, and a wrapped line keeps its `&`.
- `prdmp` with fewer than five entries or with jumps, e.g., `prdmp 2j 1` or `prdmp j j -1`, did not parse, so it and every data card after it were left in the remainder; every entry may now be a jump or left out. `tropt genxs nreact atten` read `nreact` as the `genxs` file name.
- The `AREA` card was checked against the number of cells instead of the number of surfaces, so a valid card raised `abc.Error`.
- `from_mcnp` and `from_mcnp_iter` failed on text with Windows (`\r\n`) line ends, which `from_file` reads; they now translate line ends as `from_file` does.
- Windows: PyMCNP read and wrote files in the locale's encoding, e.g., cp1252, so a UTF-8 file with a character outside ASCII was read wrong, and `to_file` wrote such characters as cp1252 or failed. Every file is now written as UTF-8, with the line ends of the OS (CRLF on Windows), and read as UTF-8 on every OS, as on Linux and macOS before; a UTF-8 byte order mark, as Windows Notepad may write, is skipped. A file that is not UTF-8, e.g., saved as cp1252 ("ANSI") on Windows, or Latin-1 text, which 0.10 failed to read on Linux and macOS, is read as Latin-1 with an `abc.Warning` naming its first line that is not UTF-8, once per read or `pymcnp` command (`Check.fix` and `pymcnp check --fix` write such a file as UTF-8); save such files as UTF-8 to read them as written. A file with a NUL byte, e.g., binary PTRAC, raises `UnicodeDecodeError`, as does a UTF-16 file with a byte order mark (Notepad's "Unicode"), whose error says "UTF-16; save the file as UTF-8"; `pymcnp` exits 2 for both.
- Windows: `Run` and `pymcnp run` found an MCNP command such as `mcnp6.bat` or `mcnp6.cmd` on `PATH` but could not start it; they now start the executable that `PATH` and `PATHEXT` give, as the shell would, also for a path without its extension, e.g., `C:\MCNP\mcnp6` for `mcnp6.exe`, which Python 3.11 does not look up.
- `Run(command=...)` with a relative path, e.g., `./mcnp6` or `bin/mcnp6`, was looked for in each run's own directory and not found; it is now relative to the working directory.
- Windows: `pymcnp` ended in a traceback when its output went to a file or pipe (cp1252) and a message held a character cp1252 lacks, e.g., in a file name; such characters are now printed as `\u` escapes.
- A `$` comment after a continuation `&`, e.g., `1 1 -2.7 -1 & $ geometry`, made the card fail to parse.
- `Inp.to_mcnp` moved a long continuation line indented by fewer than 5 spaces, e.g., `    lat=1 fill= ...` in a cell card, to column 1 when wrapping it, so the output no longer parsed. A wrapped line keeps an indent of 1-4 spaces; one indented by 5 or more starts at column 6, as before.
- `from_mcnp` of a single card did not expand the shorthands `nR`, `nI`, `nJ`, `nLOG` and `xM`, so it stopped at the first one, e.g., `data.E.from_mcnp('E14 0.1 100i 10')` returned `E14 0.1 100` and the remainder `'i 10'`. Cards now expand them as `Inp` does.
- `Inp` and `Check` expanded shorthand-like words in the free text of `fc` and `sc` cards, e.g., `sc1 source 2r here` became `sc1 source source source here`; the text of these cards and their continuation lines is now kept as written.
- The docstrings of `data.F_0`, `F_1` and `F_2` and of `Cell_0`, `Cell_1` and `Cell_2` say which MCNP form each is, e.g., `F_1` is the F5 point detector and `Cell_1` a void cell, and `F_0` lists its `t` field. They also say what does not parse yet: a point detector without `ND`, e.g., `F5:p 0 0 0 1`, parses as `F_0` with its coordinates read as cells, and `+F6 1` (without a particle) does not parse.
- `from pymcnp import *` imported the private `_cli` and `_show` modules, and `pymcnp.importlib` was a public name.
- `Plot` and `pymcnp plot` drew each tally value centred on its energy bin, half a bin too low; OUTP bins are upper bin edges, so each value is now drawn from the previous edge up to its own, the first from 0 (for negative bins, e.g., cosines, from one bin width below), with its error bar at the centre of its bin.
- Tests no longer write files into the repository.
- The docstrings of `PtracFilter` (every `check_*` returns `True` unless overridden) and `data.M.from_formula` (isotopes below `cutoff`, default 0.01, are dropped; pass `cutoff=0` to keep them all) say what the code does, as `SKILL.md` and the documentation do.
- `README.md` links are absolute, so that they work on PyPI.

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
