# ``pymcnp.inp`` Subpackage

> [!WARNING]
> The following non-terminals are not currently supported:
> * data.Field (3.3.3.12)
> * data.Mplot (3.3.7.2.5)
> * data.Burn (3.3.4.13)
> * data.Embed.Overlap (3.3.1.6.2)
> * data.Tmesh (3.3.5.24)
> * data.Spabi (3.3.6.16)
> The following non-terminals are partial supported:
> * data.Fm (3.3.5.7)
> * data.Ft (3.3.5.18)

``pymcnp.inp`` contains the INP parser. PyMCNP implements an object-oriented recursive
descent parser, approximates INP as the following context-free-grammar described in modified Bakus-Naur form:

```
<CellOption> = ...;
<Cell> = <Integer> " " <Integer> ( " " <Real> )? " " <Geometry> ( " " <CellOption>)*;

<SurfaceOption> = ...;
<Surface> = ( "+" | "*" ) <Integer> ( " " <Integer> )? <SurfaceOption>;

<DataOption> = ...;
<Data> = <DataOption>;
```

## Table of Contents

```{eval-rst}
.. toctree::
   :maxdepth: 1

   inp/cell
   inp/like
   inp/surface
   inp/data
```

## AST Classes

PyMCNP represents INP non-terminals with AST classes and stores them in nested subpackages.
These AST class have methods for translating PyMCNP and INP:

* ``from_mcnp``. Parses INP source, checking for syntax and semantic errors.
* ``to_mcnp``. Generates INP source from PyMCNP objects, reformatting.

### ``Comment`` Class

```{eval-rst}
.. autoclass:: pymcnp.inp.Comment
   :members:
   :inherited-members:
```

### ``Cell`` Class

```{eval-rst}
.. autoclass:: pymcnp.inp.Cell
   :members:
   :inherited-members:
```

[cell subpackage](inp/cell)

### ``Like`` Class

```{eval-rst}
.. autoclass:: pymcnp.inp.Like
   :members:
   :inherited-members:
```

[like subpackage](inp/like)

### ``Surface`` Class

```{eval-rst}
.. autoclass:: pymcnp.inp.Surface
   :members:
   :inherited-members:
```

[surface subpackage](inp/surface)

### ``Data`` Class

```{eval-rst}
.. autoclass:: pymcnp.inp.Data
   :members:
   :inherited-members:
```

[data subpackage](inp/data)
