# `pymcnp.ptrac` Subpackage

`pymcnp.meshtal` contains PyMCNP's ascii ptrac parser.

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
