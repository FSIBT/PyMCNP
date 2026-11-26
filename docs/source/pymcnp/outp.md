# `pymcnp.outp` Subpackage

`pymcnp.outp` contains PyMCNP's output file parser.

## Table of Contents

```{eval-rst}
.. toctree::
   :maxdepth: 1

   outp/block
   outp/line
   outp/subblock
```

## AST Classes

PyMCNP represents OUTP nonterminals with AST classes and stores them in nested subpackages.
These AST classes have methods for translating between PyMCNP and OUTP:

* `from_mcnp`. Parses OUTP source, checking for syntax and semantic errors.
* `to_mcnp`. Generates OUTP source from PyMCNP objects, reformatting.

### `Block` Class

```{eval-rst}
.. autoclass:: pymcnp.outp.Block
   :members:
   :inherited-members:
```

[block subpackage](outp/block)

### `Footer` Class

```{eval-rst}
.. autoclass:: pymcnp.outp.Footer
   :members:
   :inherited-members:
```

### `Header` Class

```{eval-rst}
.. autoclass:: pymcnp.outp.Header
   :members:
   :inherited-members:
```

### `Line` Class

```{eval-rst}
.. autoclass:: pymcnp.outp.Line
   :members:
   :inherited-members:
```

[line subpackage](outp/line)

### `Subblock` Class

```{eval-rst}
.. autoclass:: pymcnp.outp.Subblock
   :members:
   :inherited-members:
```

[subblock subpackage](outp/subblock)

## Summary Classes

`Outp.summary` returns a `Summary`, with one `TallyCheck` per tally in `Summary.checks`.

### `Summary` Class

```{eval-rst}
.. autoclass:: pymcnp.outp.Summary
   :members:
```

### `TallyCheck` Class

```{eval-rst}
.. autoclass:: pymcnp.outp.TallyCheck
   :members:
```
