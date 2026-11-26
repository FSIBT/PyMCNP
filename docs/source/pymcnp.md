# PyMCNP Library

PyMCNP provides the backend for the CLI and useful tools for programmatically interfacing with
MCNP. This package supports INP, OUTP, PTRAC, and MESHTAL parsing using subpackages.

## Table of Contents

```{eval-rst}
.. toctree::
   :maxdepth: 1

   pymcnp/abc
   pymcnp/inp
   pymcnp/meshtal
   pymcnp/outp
   pymcnp/ptrac
```

## AST Classes

PyMCNP represents MCNP files using the `Inp`, `Meshtal`, and `Ptrac` AST classes and
`inp`, `meshtal`, and `ptrac` subpackages. These classes have important methods for translating PyMCNP and MCNP:

* `from_mcnp`. Parses MCNP source, checking for syntax and semantic errors.
* `to_mcnp`. Generates MCNP source from PyMCNP objects, reformatting.
* `from_file`. Parses MCNP file.
* `to_file`. Generates MCNP file from PyMCNP objects.

These classes, `ptrac.block.History` and the card classes, e.g., `inp.card.Cell_1`, can be subclassed to add methods,
e.g., `class MyInp(pymcnp.Inp)`. A subclass inherits its parent's fields, defaults and parser, so `MyInp.from_file`
returns a `MyInp`, while `Inp.from_file` still returns an `Inp`. A subclass cannot add or redefine fields: an annotation other
than a private name or a `typing.ClassVar`, or a class attribute or method named like an inherited field, raises
`abc.Error`. A subclass instance never equals a parent instance, even
with the same content, since dataclass equality compares the classes; compare `to_mcnp()` instead.

### `Inp` Class

```{eval-rst}
.. autoclass:: pymcnp.Inp
   :members:
   :inherited-members:
```

Cards are found with `Inp.cell_cards(number, material, density, kind)`, `Inp.surface_cards(number, kind)` and
`Inp.data_cards(kind)`, which return tuples of the cards themselves, so edits change the input, e.g.,
`inp.surface_cards(99)[0].r = 600`. `scan(**parameters)` and `scan_with(values, apply)` yield independent copies for
parameter scans. `to_mcnp` wraps lines longer than 80 columns, since MCNP rejects data past column 80.

The keys of `scan` are fields or settable properties, e.g., `inp.scan(nps=[10**4, 10**5])`, or paths into the input
for nested values: dotted attributes and integer indices, e.g., `inp.scan(**{'surfaces[99].r': [5, 10]})`; with
several keys, the last varies fastest. The index into `cells` or `surfaces` is the card number, so `surfaces[99]` is
surface card 99 wherever it is in `inp.surfaces`, and a number no card has raises `abc.Error`. The index into `data` is
the list position, as in `inp.data[i]`, comment cards included. Values are converted to the field's type, e.g.,
`inp.literal.Real`, which compares and computes as a number; a value that does not parse whole, e.g., `'7 8'` for a
radius, raises `abc.Error` (whitespace around it is dropped, and a float such as `10.0` for an integer field raises). A message, e.g., `inp.message = 'outp=run.o'`, gets the `message:` keyword if it has none. A path that does not exist raises `abc.Error`. For changes a path cannot express, use `scan_with(values, apply)` with a function that changes each copy.

[inp subpackage](pymcnp/inp)

### `Outp` Class

```{eval-rst}
.. autoclass:: pymcnp.Outp
   :members:
   :inherited-members:
```

`Outp.summary` and `Outp.fatal_errors` give the headline results and the fatal errors, `Outp.tally(number)` gives one
tally as a dataframe with typed columns, and `Outp.activity(particle)` gives an activity table as a dataframe.
`Outp.tallies()` and `Outp.activities()` return the parsed tally and activity blocks, not dataframes; a tally block's
`tally_number` is an `int`, while its fields, e.g., `number`, are the padded text of the file. Run values such as the
version, the number of histories and the warnings are in `Outp.summary` only.

`Outp.to_dataframe()` stacks all parsed tallies in one dataframe, as `pymcnp convert outp` writes them. Its columns
differ from those of `Outp.tally(number)`: it names the surface column `surface_number` and the tally kind `type`, and
has no `facet` column, whereas `tally` splits surface numbers such as `2.1` into `surface` and `facet` and has a
`quantity` column. In both, `number` and `nps` are `int`s. Use `tally` for analysis and `to_dataframe` for export.

[outp subpackage](pymcnp/outp)

### `Ptrac` Class

```{eval-rst}
.. autoclass:: pymcnp.Ptrac
   :members:
   :inherited-members:
```

PTRAC files can be very large, and `from_file` keeps the whole object tree in memory (about 35 times the file size).
For large files, stream them instead: `Ptrac.stream(path)` yields one `ptrac.Event` at a time (with `nps`, `type`, and values
such as `particle`, `surface`, `cell_entered`, `zaid`, `position`, `energy`; `to_dict()` gives a flat row),
`Ptrac.tracks(path)` yields `ptrac.Track` objects (one particle each, linked to the parent it was banked from and the
originating nuclide `parent_zaid`) and `Ptrac.iter_histories(path)` yields one history at a time (`ptrac.block.History`, or
`ptrac.block.HistoryTruncated` for a last history that was cut short), all with flat memory use. `Ptrac.to_parquet(path, out)`
writes events to a parquet file in chunks, and `to_dataframe` has typed columns including `track` and `parent_zaid`.

A PTRAC file can be cut short, e.g., when an MCNP run is killed. The streaming functions keep the truncated last history
and issue an `abc.Warning`; damage before the final event still raises `abc.Error`. `Ptrac.from_file` does not read the
truncated last history: it stays in the returned remainder, so use `stream` or `iter_histories` for such files.

[ptrac subpackage](pymcnp/ptrac)

### `Meshtal` Class

```{eval-rst}
.. autoclass:: pymcnp.Meshtal
   :members:
   :inherited-members:
```

`Meshtal.from_file` reads the first mesh tally of a file; use `Meshtal.iter_tallies(path)` for files that hold several.
`to_dataframe` gives one dataframe per tally with float columns (`Energy` and `Time` stay strings if a bin is `Total`), and
`tally_number` and `nps` (the number of histories) are `int`s, `particle_name` a plain `str` and `names` a list of plain
`str`; the fields, e.g., `histories`, are the padded text of the file.

[meshtal subpackage](pymcnp/meshtal)

## Utility Classes

The `PtracFilter` and `PtracProcessor` classes help handle large `Ptrac` using generators. `PtracFilter` has
overridable methods for filtering data, and `PtracProcessor` has overridable methods for processing data, and all can be run:

* `check_*`. Returns `True`/`False` if data should be kept/removed. Every `check_*` returns `True` unless overridden, so overriding one restricts only that type of event.
* `process_*`. Operates with side effects on data.
* `run`. Runs the filter or processor. It accepts a `Ptrac` or a path to a PTRAC file; a path is streamed event by event.

### `PtracFilter` Class

```{eval-rst}
.. autoclass:: pymcnp.PtracFilter
   :members:
   :inherited-members:
```

### `PtracProcessor` Class

```{eval-rst}
.. autoclass:: pymcnp.PtracProcessor
   :members:
   :inherited-members:
```

### `Check` Class

`Check(path)` checks and fixes an MCNP input file: `problems()` returns `Problem(line, kind, message)` entries (lines
wider than 80 columns are errors, a card PyMCNP cannot parse is a warning), `check()` yields the unified diff (using `difflib`)
between the file and its reformatted version, and `fix()` rewrites the file, or raises `abc.Error` and leaves it as it is if
PyMCNP cannot parse it completely. The command line equivalent is
`pymcnp check [--diff] [--fix] <inp>`.

```{eval-rst}
.. autoclass:: pymcnp.Check
   :members:
   :inherited-members:
```

```{eval-rst}
.. autoclass:: pymcnp.Check.Problem
   :members:
```

### `Plot` Class

`Plot` plots OUTP files, using `matplotlib`: `pymcnp.Plot().to_pdf(outp, '1', path)` or `pymcnp.Plot().to_show(outp, '1')`.

```{eval-rst}
.. autoclass:: pymcnp.Plot
   :members:
   :inherited-members:
```

### `Run` Class

`Run` runs MCNP simulations in parallel (at most `max_workers` at a time), using `subprocess`. Every input runs in its own
directory, and `run` returns one `Result` per input with `.inp`, `.outp`, `.ptrac`, `.runtpe`, `.log`, `.returncode`,
`.fatal_errors` and `.ok`: `pymcnp.Run(files, command, max_workers, names, check, batch).run(path)`. A failed run raises after all
runs finished, unless `check=False`. Subclasses override the hooks `prehook_file(path, index)`, `posthook_file(result)`,
`prehook_batch(path)` and `posthook_batch(path)`.

```{eval-rst}
.. autoclass:: pymcnp.Run
   :members:
   :inherited-members:
```

```{eval-rst}
.. autoclass:: pymcnp.Result
   :members:
```

### `Visualize` Class

`Visualize` visualizes INP surfaces and cell geometries, using `pyvista`: `pymcnp.Visualize().to_show_surfaces(inp)`,
`to_show_cells(inp)` and the `to_pdf_*` methods.

```{eval-rst}
.. autoclass:: pymcnp.Visualize
   :members:
   :inherited-members:
```
