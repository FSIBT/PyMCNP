# PyMCNP Library

```{eval-rst}
.. warning:: 
   PyMCNP is in active development! Please, double check everything works. Reports error on [GitHub](https://github.com/FSIBT/PyMCNP).
```

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

[inp subpackage](pymcnp/inp)

### `Outp` Class

```{eval-rst}
.. autoclass:: pymcnp.Outp
   :members:
   :inherited-members:
```

[meshtal subpackage](pymcnp/outp)

### `Ptrac` Class

```{eval-rst}
.. autoclass:: pymcnp.Ptrac
   :members:
   :inherited-members:
```

[ptrac subpackage](pymcnp/ptrac)

### `Meshtal` Class

```{eval-rst}
.. autoclass:: pymcnp.Meshtal
   :members:
   :inherited-members:
```

[meshtal subpackage](pymcnp/meshtal)

## Utility Classes

The `PtracFilter` and `PtracProcessor` classes help handle large `Ptrac` using generators. `PtracFilter` have 
overridable methods for filtering data, and `PtracProcessor` have overridable methods for processing data, and all can be run:

* `check_*`. Returns `True`/`False` if data should be kept/removed.
* `process_*`. Operates with side effects on data.
* `run`. Runs the filter or processor.

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

`Check` compares and fixes MCNP files, using `difflib`,

```{eval-rst}
.. autoclass:: pymcnp.Check
   :members:
   :inherited-members:
```

### `Convert` Class

`Convert` converts OUTP files to csv or parquet files, using `pandas`.

```{eval-rst}
.. autoclass:: pymcnp.Convert
   :members:
   :inherited-members:
```

### `Plot` Class

`Plot` plots OUTP files, using `matplotlib`.

```{eval-rst}
.. autoclass:: pymcnp.Plot
   :members:
   :inherited-members:
```

### `Run` Class

`Run` runs MCNP simulations in parallel, using `subprocess`.

```{eval-rst}
.. autoclass:: pymcnp.Run
   :members:
   :inherited-members:
```

### `Visualize` Class

`Visualize` visualizes INP surfaces and cell geometries, using `pyvista`.

```{eval-rst}
.. autoclass:: pymcnp.Visualize
   :members:
   :inherited-members:
```
