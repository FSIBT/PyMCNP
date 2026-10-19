# `pymcnp.meshtal` Subpackage

`pymcnp.meshtal` contains PyMCNP's meshtal file parser.

## Table of Contents

```{eval-rst}
.. toctree::
   :maxdepth: 1

   meshtal/line
   meshtal/block
```

## AST Classes

PyMCNP represents MESHTAL nonterminals with AST classes and stores them in nested subpackages.
These AST class have methods for translating between PyMCNP and MESHTAL:

* `from_mcnp`. Parses MESHTAL source, checking for syntax and semantic errors.
* `to_mcnp`. Generates MESHTAL source from PyMCNP objects, reformatting.

### `Block` Class

```{eval-rst}
.. autoclass:: pymcnp.meshtal.Block
   :members:
   :inherited-members:
```

### `Line` Class

```{eval-rst}
.. autoclass:: pymcnp.meshtal.Line
   :members:
   :inherited-members:
```

[line subpackage](meshtal/line)
