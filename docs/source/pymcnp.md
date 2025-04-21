# PyMCNP Package

PyMCNP provides the backend for the CLI and useful tools for programatically interfacing with
MCNP. This package supports INP, PTRAC, and MESHTAL parsing and the CLI backend using subpackages:

* [inp subpackage](/pymcnp/inp): INP parsing.

* [meshtal subpackage](/pymcnp/meshtal): MESHTAL parsing.

* [ptrac subpackage](/pymcnp/ptrac): PTRAC parsing. 

* [cli subpackage](/pymcnp/cli): CLI backend.

## Table of Contents

```{eval-rst}
.. toctree::
   :maxdepth: 1

   pymcnp/cli
   pymcnp/inp
   pymcnp/meshtal
   pymcnp/outp
   pymcnp/ptrac
```

## AST Classes

PyMCNP represents MCNP files using the ``Inp``, ``Meshtal``, and ``Ptrac`` AST classes and
``inp``, ``meshtal``, and ``ptrac`` subpackages. These classes have important methods for translating PyMCNP and MCNP:

* ``from_mcnp``. Parses MCNP source, checking for syntax and semantic errors.

* ``to_mcnp``. Generates MCNP source from PyMCNP objects, reformatting.

* ``from_mcnp_file``. Parses MCNP file.

* ``to_mcnp_file``. Generates MCNP file from PyMCNP objects.

### ``Inp`` Class

```{eval-rst}
.. autoclass:: pymcnp.Inp
   :members:
```

[inp subpackage](pymcnp/inp)

### ``Meshtal`` Class

```{eval-rst}
.. autoclass:: pymcnp.Meshtal
   :members:
```

[meshtal subpackage](pymcnp/meshtal)

### ``Ptrac`` Class

```{eval-rst}
.. autoclass:: pymcnp.Ptrac
   :members:
```

[ptrac subpackage](pymcnp/ptrac)

## Builder Classes

AST classes are immutable, but ``Inp`` has a builder class. ``InpBuilder`` is a mutable wrapper without input
validation, and it has a method for constructing ``Inp``:

* ``build``. Attempts to build ``Inp`` using ``InpBuilder``'s fields.

### ``InpBuilder`` Class

```{eval-rst}
.. autoclass:: pymcnp.InpBuilder
   :members:
```

[inp subpackage](pymcnp/inp)

## Filter & Processor Classes

The ``*Filtered`` and ``*Processed`` classes help handle large ``Meshtal`` and ``Ptrac`` using generators.
``PtracFiltered`` and ``MeshtalFiltered`` have overridable methods for filtering data, ``PtracProcessed``
and ``MeshtalProcessed`` have overridable methods for processing data, and all can be run:

* ``check_*``. Returns ``True``/``False`` if data should be kept/removed.

* ``process_*``. Operates with side effects on data.

* ``run``. Runs the filter or processor.

### ``MeshtalFiltered`` Class

```{eval-rst}
.. autoclass:: pymcnp.MeshtalFiltered
   :members:
```

### ``PtracFiltered`` Class

```{eval-rst}
.. autoclass:: pymcnp.PtracFiltered
   :members:
```

### ``MeshtalProcessed`` Class

```{eval-rst}
.. autoclass:: pymcnp.MeshtalProcessed
   :members:
```

### ``PtracProcessed`` Class

```{eval-rst}
.. autoclass:: pymcnp.PtracProcessed
   :members:
```
