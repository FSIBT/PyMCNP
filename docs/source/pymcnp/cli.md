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
* ``Run``

### ``run.Run`` Class

``run`` contains the ``Run`` class which runs MCNP simulations, in series or parallel,
on given INP.

```{eval-rst}
.. autoclass:: pymcnp.cli.run.Run
   :members:
```
