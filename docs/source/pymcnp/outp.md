# `pymcnp.outp` Subpackage

`pymcnp.outp` contains the OUTP parser. PyMCNP implements an object-oriented recursive
descent parser, approximating OUTP as the following context-free-grammar described in modified Backus-Naur form:

```
...
```

## Table of Contents

```{eval-rst}
.. toctree::
   :maxdepth: 1

   outp/tally
```

## AST Classes

PyMCNP represents OUTP non-terminals with AST classes and stores them in nested subpackages.
These AST class have methods for translating between PyMCNP and OUTP:

* `from_mcnp`. Parses OUTP source, checking for syntax and semantic errors.
* `to_mcnp`. Generates OUTP source from PyMCNP objects, reformatting.

### `AnalysisTallyFluctuation` Class

```{eval-rst}
.. autoclass:: pymcnp.outp.AnalysisTallyFluctuation
   :members:
   :inherited-members:
```

### `Header` Class

```{eval-rst}
.. autoclass:: pymcnp.outp.Header
   :members:
   :inherited-members:
```

### `Mcnp` Class

```{eval-rst}
.. autoclass:: pymcnp.outp.Mcnp
   :members:
   :inherited-members:
```

### `NeutronActivity` Class

```{eval-rst}
.. autoclass:: pymcnp.outp.NeutronActivity
   :members:
   :inherited-members:
```

### `PhotonActivity` Class

```{eval-rst}
.. autoclass:: pymcnp.outp.PhotonActivity
   :members:
   :inherited-members:
```

### `ProblemSummary` Class

```{eval-rst}
.. autoclass:: pymcnp.outp.ProblemSummary
   :members:
   :inherited-members:
```

### `StartingMcrun` Class

```{eval-rst}
.. autoclass:: pymcnp.outp.StartingMcrun
   :members:
   :inherited-members:
```

### `Tally_1A` Class

```{eval-rst}
.. autoclass:: pymcnp.outp.Tally_1A
   :members:
   :inherited-members:
```

[tally subpackage](outp/tally)

### `Tally_1B` Class

```{eval-rst}
.. autoclass:: pymcnp.outp.Tally_1B
   :members:
   :inherited-members:
```

[tally subpackage](outp/tally)

### `Tally_2` Class

```{eval-rst}
.. autoclass:: pymcnp.outp.Tally_2
   :members:
   :inherited-members:
```

[tally subpackage](outp/tally)

### `Tally_4` Class

```{eval-rst}
.. autoclass:: pymcnp.outp.Tally_4
   :members:
   :inherited-members:
```

[tally subpackage](outp/tally)

### `Tally_8` Class

```{eval-rst}
.. autoclass:: pymcnp.outp.Tally_8
   :members:
   :inherited-members:
```

[tally subpackage](outp/tally)

### `UnnormedTallyDensity` Class

```{eval-rst}
.. autoclass:: pymcnp.outp.UnnormedTallyDensity
   :members:
   :inherited-members:
```
