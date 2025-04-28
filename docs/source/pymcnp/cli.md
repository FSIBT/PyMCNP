# ``pymcnp.cli`` Subpackage

``pymcnp.cli`` contains classes powering PyMCNP's CLI. Modules correspond to subcommands:

* ``pymcnp check``
* ``pymcnp covert``
* ``pymcnp plot``
* ``pymcnp run``
* ``pymcnp visualize``

## Modules

Each module contains corresponding classes which enapsulate the subcommands' functionality,
enabiling programmatic access to the CLI:

* ``Check``
* ``Convert``
* ``Plot``
* ``Run``

### ``check.Check`` Class

``check`` contains the ``Check`` class which compares MCNP files using ``difflib`` and
formats them.

```{eval-rst}
.. autoclass:: pymcnp.cli.check.Check
   :members:
```

### ``convert.Convert`` Class

``convert`` contains the ``Convert`` class which converts OUTP files, using ``pandas``, to
CSV or parquet files.

```{eval-rst}
.. autoclass:: pymcnp.cli.convert.Convert
   :members:
```

### ``plot.Plot`` Class

``plot`` contains the ``Plot`` class which plots OUTP files, using ``matplotlib``.

```{eval-rst}
.. autoclass:: pymcnp.cli.plot.Plot
   :members:
```

### ``run.Run`` Class

``run`` contains the ``Run`` class which runs MCNP simulations, in series or parallel,
on given INP.

```{eval-rst}
.. autoclass:: pymcnp.cli.run.Run
   :members:
```
