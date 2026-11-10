# `pymcnp.ptrac` Subpackage

`pymcnp.ptrac` contains PyMCNP's ascii PTRAC parser.

## Table of Contents

```{eval-rst}
.. toctree::
   :maxdepth: 1

   ptrac/line
   ptrac/block
```

## AST Classes

PyMCNP represents PTRAC nonterminals with AST classes and stores them in nested subpackages.
These AST class have methods for translating between PyMCNP and PTRAC:

* `from_mcnp`. Parses PTRAC source, checking for syntax and semantic errors.
* `to_mcnp`. Generates PTRAC source from PyMCNP objects, reformatting.

### `Block` Class

```{eval-rst}
.. autoclass:: pymcnp.ptrac.Block
   :members:
   :inherited-members:
```

### `Line` Class

```{eval-rst}
.. autoclass:: pymcnp.ptrac.Line
   :members:
   :inherited-members:
```

[line subpackage](ptrac/line)

[block subpackage](ptrac/block)

## Streaming Classes

`Ptrac.stream`, `Ptrac.tracks`, and `Ptrac.to_parquet` give PTRAC events with their own type and values by meaning.

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

### `EventType` Class

```{eval-rst}
.. autoclass:: pymcnp.ptrac.EventType
   :members:
```

### `Particle` Class

```{eval-rst}
.. autoclass:: pymcnp.ptrac.Particle
   :members:
```

### `Surface` Class

```{eval-rst}
.. autoclass:: pymcnp.ptrac.Surface
   :members:
```

### `ParquetWriter` Class

```{eval-rst}
.. autoclass:: pymcnp.ptrac.ParquetWriter
   :members:
```

### `tracks` Function

```{eval-rst}
.. autofunction:: pymcnp.ptrac.tracks
```

### `to_dataframe` Function

```{eval-rst}
.. autofunction:: pymcnp.ptrac.to_dataframe
```
