# PyMCNP Package

> [!WARNING]
> Warning: PyMCNP is in active development! Please, double check eveything works. Reports error on [GitHub](https://github.com/FSIBT/PyMCNP).

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
* ``from_file``. Parses MCNP file.
* ``to_file``. Generates MCNP file from PyMCNP objects.

### ``Inp`` Class

```{eval-rst}
.. autoclass:: pymcnp.Inp
   :members:
   :inherited-members:
```

[inp subpackage](pymcnp/inp)

### ``Outp`` Class

```{eval-rst}
.. autoclass:: pymcnp.Outp
   :members:
   :inherited-members:
```

[meshtal subpackage](pymcnp/outp)

### ``Ptrac`` Class

```{eval-rst}
.. autoclass:: pymcnp.Ptrac
   :members:
   :inherited-members:
```

[ptrac subpackage](pymcnp/ptrac)

### ``Meshtal`` Class

```{eval-rst}
.. autoclass:: pymcnp.Meshtal
   :members:
   :inherited-members:
```

[meshtal subpackage](pymcnp/meshtal)

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
   :inherited-members:
```

### ``PtracFiltered`` Class

```{eval-rst}
.. autoclass:: pymcnp.PtracFiltered
   :members:
   :inherited-members:
```

### ``MeshtalProcessed`` Class

```{eval-rst}
.. autoclass:: pymcnp.MeshtalProcessed
   :members:
   :inherited-members:
```

### ``PtracProcessed`` Class

```{eval-rst}
.. autoclass:: pymcnp.PtracProcessed
   :members:
   :inherited-members:
```
