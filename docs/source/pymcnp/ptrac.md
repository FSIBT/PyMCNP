# ``pymcnp.ptrac`` Subpackage

``pymcnp.ptrac`` contains the PTRAC parser. PyMCNP implements an object-oriented recursive
descent parser, modeling PTRAC as the following context-free-grammar described in modified Bakus-Naur form:

```
...
```

## Table of Contents

```{eval-rst}
.. toctree::
   :maxdepth: 1

   ptrac/history
```

## AST Classes

PyMCNP represents PTRAC non-terminals with AST classes and stores them in nested subpackages.
These AST class have methods for translating PyMCNP and PTRAC:

* ``from_mcnp``. Parses PTRAC source, checking for syntax and semantic errors.

* ``to_mcnp``. Generates PTRAC source from PyMCNP objects, reformatting.

### ``Header`` Class

```{eval-rst}
.. autoclass:: pymcnp.ptrac.Header
   :members:
```

### ``History`` Class

```{eval-rst}
.. autoclass:: pymcnp.ptrac.History
   :members:
```

[history subpackage](ptrac/history)
