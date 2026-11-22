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
These AST class have methods for translating between PyMCNP and PTRAC:

* `from_mcnp`. Parses PTRAC source, checking for syntax and semantic errors.
* `to_mcnp`. Generates PTRAC source from PyMCNP objects, reformatting.

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
