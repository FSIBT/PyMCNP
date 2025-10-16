# `pymcnp.meshtal` Subpackage

`pymcnp.meshtal` contains the MESHTAL parser. PyMCNP implements an object-oriented recursive
descent parser, approximating MESHTAL as the following context-free-grammar described in modified Backus-Naur form:

```
...
```

## AST Classes

PyMCNP represents MESHTAL non-terminals with AST classes and stores them in nested subpackages.
These AST class have methods for translating between PyMCNP and MESHTAL:

* `from_mcnp`. Parses MESHTAL source, checking for syntax and semantic errors.
* `to_mcnp`. Generates MESHTAL source from PyMCNP objects, reformatting.

### `Header` Class

```{eval-rst}
.. autoclass:: pymcnp.meshtal.Header
   :members:
   :inherited-members:
```

### `Tally` Class

```{eval-rst}
.. autoclass:: pymcnp.meshtal.Tally
   :members:
   :inherited-members:
```
