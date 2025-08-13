# `pymcnp.types` Subpackage

`pymcnp.types` contains parsers for basic types, such as integers, zaids, and surface geometry formulas. PyMCNP
implements classes for types to integrate them into the object-oriented recursive decent parsers.

## AST Classes

PyMCNP represents types with AST classes. These AST class have methods for translating
between PyMCNP and MCNP:

* `from_mcnp`. Parses MCNP source, checking for syntax and semantic errors.
* `to_mcnp`. Generates MCNP source from PyMCNP objects, reformatting.

### `Designator` Classes

```{eval-rst}
.. autoclass:: pymcnp.types.Designator
   :members:
   :inherited-members:
```

### `Distribution` Classes

```{eval-rst}
.. autoclass:: pymcnp.types.Distribution
   :members:
   :inherited-members:
```

### `Generator` Classes

```{eval-rst}
.. autoclass:: pymcnp.types.Generator
   :members:
   :inherited-members:
```

### `Geometry` Classes

```{eval-rst}
.. autoclass:: pymcnp.types.Geometry
   :members:
   :inherited-members:
```

### `Horizontal` Classes

```{eval-rst}
.. autoclass:: pymcnp.types.Horizontal
   :members:
   :inherited-members:
```

### `Index` Classes

```{eval-rst}
.. autoclass:: pymcnp.types.Index
   :members:
   :inherited-members:
```

### `Integer` Classes

```{eval-rst}
.. autoclass:: pymcnp.types.Integer
   :members:
   :inherited-members:
```

### `Lattice` Classes

```{eval-rst}
.. autoclass:: pymcnp.types.Lattice
   :members:
   :inherited-members:
```

### `Real` Classes

```{eval-rst}
.. autoclass:: pymcnp.types.Real
   :members:
   :inherited-members:
```

### `String` Classes

```{eval-rst}
.. autoclass:: pymcnp.types.String
   :members:
   :inherited-members:
```

### `Substance` Classes

```{eval-rst}
.. autoclass:: pymcnp.types.Substance
   :members:
   :inherited-members:
```

### `Transformation` Classes

```{eval-rst}
.. autoclass:: pymcnp.types.Transformation
   :members:
   :inherited-members:
```

### `Tuple` Classes

```{eval-rst}
.. autoclass:: pymcnp.types.Tuple
   :members:
   :inherited-members:
```

### `Zaid` Classes

```{eval-rst}
.. autoclass:: pymcnp.types.Zaid
   :members:
   :inherited-members:
```
