# PyMCNP Library

PyMCNP provides the backend for the CLI and useful tools for programatically interfacing with
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

[inp subpackage](pymcnp/inp)

### `Outp` Class

```{eval-rst}
.. autoclass:: pymcnp.Outp
   :members:
   :inherited-members:
```

`Outp.summary` and `Outp.fatal_errors` give the headline results and the fatal errors, `Outp.tally(number)` gives one
tally as a dataframe with typed columns, and `Outp.activity(particle)` gives an activity table as a dataframe.
`Outp.tallies()` and `Outp.activities()` return the parsed tally and activity blocks, not dataframes.

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
`tally_number` is an `int`, `particle_name` a plain `str` and `names` a list of plain `str`.

[meshtal subpackage](pymcnp/meshtal)

## Utility Classes

The `PtracFilter` and `PtracProcessor` classes help handle large `Ptrac` using generators. `PtracFilter` have 
overridable methods for filtering data, and `PtracProcessor` have overridable methods for processing data, and all can be run:

* `check_*`. Returns `True`/`False` if data should be kept/removed.
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
between the file and its reformatted version, and `fix()` rewrites the file. The command line equivalent is
`pymcnp check [--diff] [--fix] <inp>`.

```{eval-rst}
.. autoclass:: pymcnp.Check
   :members:
   :inherited-members:
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
