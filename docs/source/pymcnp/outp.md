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
These AST class have methods for translating between PyMCNP and OUTP:

* `from_mcnp`. Parses OUTP source, checking for syntax and semantic errors.
* `to_mcnp`. Generates OUTP source from PyMCNP objects, reformatting.

### `Block` Class

```{eval-rst}
.. autoclass:: pymcnp.outp.Block
   :members:
   :inherited-members:
```

### `Line` Class

```{eval-rst}
.. autoclass:: pymcnp.outp.Line
   :members:
   :inherited-members:
```

### `Subblock` Class

```{eval-rst}
.. autoclass:: pymcnp.outp.Subblock
   :members:
   :inherited-members:
```

[subblock subpackage](outp/subblock)
