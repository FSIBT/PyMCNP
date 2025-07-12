# ``pymcnp.cli`` Subpackage

``pymcnp.cli`` contains classes powering PyMCNP's CLI. Modules correspond to subcommands:

* ``pymcnp check``
* ``pymcnp covert``
* ``pymcnp plot``
* ``pymcnp run``
* ``pymcnp visualize``

## CLI Classes

### ``Check`` Class

``Check`` compares and fixes MCNP files, using ``difflib``,

```{eval-rst}
.. autoclass:: pymcnp.cli.Check
   :members:
   :inherited-members:
```

### ``Convert`` Class

``Convert`` converts OUTP files to csv or parquet files, using ``pandas``.

```{eval-rst}
.. autoclass:: pymcnp.cli.Convert
   :members:
   :inherited-members:
```

### ``Plot`` Class

``Plot`` plots OUTP files, using ``matplotlib``.

```{eval-rst}
.. autoclass:: pymcnp.cli.Plot
   :members:
   :inherited-members:
```

### ``Run`` Class

``Run`` runs MCNP simulations in parallel, using ``subprocess``.

```{eval-rst}
.. autoclass:: pymcnp.cli.Run
   :members:
   :inherited-members:
```

### ``Visualize`` Class

``Visualize`` visualizes INP surfaces and cell geometries, using ``pyvista``.

```{eval-rst}
.. autoclass:: pymcnp.cli.Visualize
   :members:
   :inherited-members:
```
