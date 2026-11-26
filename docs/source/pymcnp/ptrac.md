# `pymcnp.ptrac` Subpackage

`pymcnp.ptrac` contains PyMCNP's ascii PTRAC parser.

## Table of Contents

```{eval-rst}
.. toctree::
   :maxdepth: 1

   ptrac/block
   ptrac/line
```

## AST Classes

PyMCNP represents PTRAC nonterminals with AST classes and stores them in nested subpackages.
These AST classes have methods for translating between PyMCNP and PTRAC:

* `from_mcnp`. Parses PTRAC source, checking for syntax and semantic errors.
* `to_mcnp`. Generates PTRAC source from PyMCNP objects, reformatting.

A PTRAC file is a header followed by histories (`ptrac.block.History`), and each history holds event blocks named after
the variables of the MCNP manual (`EventSource_1`, ..., `EventTermination_4`). The `type` on an event's first line is the type
of the *next* event, so PyMCNP picks an event's block class by the type announced on the previous line.

For large files use the streaming functions of `pymcnp.Ptrac` (`stream`, `tracks`, `iter_histories`, `to_parquet`) rather than
`from_file`; they also read files cut short by a killed MCNP run, keeping the truncated last history
(`ptrac.block.HistoryTruncated`) with an `abc.Warning`, whereas `Ptrac.from_file` leaves that history in the remainder.
`PtracFilter.run(path)` and `PtracProcessor.run(path)` stream a path too.

### `Block` Class

```{eval-rst}
.. autoclass:: pymcnp.ptrac.Block
   :members:
   :inherited-members:
```

[block subpackage](ptrac/block)

### `Line` Class

```{eval-rst}
.. autoclass:: pymcnp.ptrac.Line
   :members:
   :inherited-members:
```

[line subpackage](ptrac/line)

## Streaming Classes

The streaming functions of `pymcnp.Ptrac` yield these classes instead of the AST classes, so large files are read with
flat memory use.

### `Event` Class

```{eval-rst}
.. autoclass:: pymcnp.ptrac.Event
   :members:
```

### `Track` Class

```{eval-rst}
.. autoclass:: pymcnp.ptrac.Track
   :members:
```

### `tracks` Function

```{eval-rst}
.. autofunction:: pymcnp.ptrac.tracks
```

### `EventType` Class

```{eval-rst}
.. autoclass:: pymcnp.ptrac.EventType
   :members:
   :undoc-members:
```

### `Particle` Class

```{eval-rst}
.. autoclass:: pymcnp.ptrac.Particle
   :members:
   :undoc-members:
```

### `Surface` Class

```{eval-rst}
.. autoclass:: pymcnp.ptrac.Surface
   :members:
```

### `to_dataframe` Function

```{eval-rst}
.. autofunction:: pymcnp.ptrac.to_dataframe
```

### `ParquetWriter` Class

```{eval-rst}
.. autoclass:: pymcnp.ptrac.ParquetWriter
   :members:
   :undoc-members:
```
