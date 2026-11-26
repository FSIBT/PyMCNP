# PyMCNP Documentation

PyMCNP is a Python package and CLI for interfacing
with [MCNP](https://mcnp.lanl.gov). PyMCNP parses MCNP files,
visualizes simulation geometries, and runs MCNP simulations in parallel.

## Example

Inputs are Python objects, so loops can build geometries that are impractical to write by hand, and the results go straight into `pandas` and `matplotlib`.
This builds 441 iron discs of random thickness over a rough concrete floor, tallies the neutron flux of a point source, and plots the result (an excerpt; the elided parts are in the full example):

```{eval-rst}
.. literalinclude:: ../../examples/home.py
   :language: python
```

![Setup](images/example_02_setup.png)
![Flux](images/example_02_flux.png)

New to PyMCNP? Start with [Getting Started](getting_started.md).

The [full example](examples/automate.md) includes the complete model, the geometry plot, and the flux plot.

## Table of Contents

```{eval-rst}
.. toctree::
   :maxdepth: 1

   installation
   getting_started
   examples
   cli
   pymcnp
   skill
   contributing
   changelog
```
