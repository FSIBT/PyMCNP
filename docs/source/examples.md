# Examples

```{eval-rst}
.. note:: 
   Examples that write files put them in an ``output`` directory next to the example scripts (``examples/output``),
   which is ignored by git. Delete it to clean up.

   Some examples (``do_visualize.py``, ``do_plot.py``, ``do_parameter_scan.py``) open windows and wait until you close
   them, so they need a display. On a machine without one, e.g., over SSH or in CI, set the environment variables
   ``PYVISTA_OFF_SCREEN=true`` and ``MPLBACKEND=Agg``; the windows are not opened and the scripts run to the end.
```

PyMCNP includes examples for reading INP, PTRAC, and OUTP, creating INP, and doing workflows, such as visualizing, running, and plotting. [Automating Models, Runs, and Plots](examples/automate.md) shows a complete example, from a model built with loops to plots of the result.

## Table of Contents

```{eval-rst}
.. toctree::
   :maxdepth: 1

   examples/automate
   examples/create
   examples/do
   examples/read
```
