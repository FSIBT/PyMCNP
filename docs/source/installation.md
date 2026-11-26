# Installation

PyMCNP is accessible for installation through [PyPI](https://pypi.org/project/pymcnp/) and [GitHub](https://github.com/FSIBT/PyMCNP).

```{eval-rst}
.. note::
   PyMCNP supports MCNP 6.1 to 6.3 and Python 3.11 to 3.15.
```

## Requirements

- Python 3.11 or newer.
- MCNP, only for running simulations (`pymcnp run`, `pymcnp.Run`). MCNP is not included with PyMCNP; it is distributed by
  [RSICC](https://rsicc.ornl.gov). PyMCNP starts it as a program on your `PATH`, by default `mcnp6` (change it with
  `pymcnp run -c <command>` or `Run(..., command=...)`), and MCNP finds its nuclear data through the `DATAPATH`
  environment variable. Everything else, reading, checking, editing, visualizing, converting and plotting, works without
  MCNP.

After installing, continue with [Getting Started](getting_started.md).

## Using uv (recommended)

We recommend [uv](https://docs.astral.sh/uv/) for installing PyMCNP. Optionally, create a virtual environment first, activate it, and install into it:

    uv venv
    source .venv/bin/activate
    uv pip install pymcnp

On Windows, activate the environment with `.venv\Scripts\activate` instead.

PyMCNP reads and writes files as UTF-8 text on every OS, and reads files with Windows (CRLF) or Unix (LF) line ends.

Without a virtual environment, uv can also install PyMCNP as a command-line tool:

    uv tool install pymcnp

The latest version from [GitHub](https://github.com/FSIBT/PyMCNP) and the developer version work the same way:

    uv pip install git+https://github.com/FSIBT/PyMCNP

    git clone https://github.com/FSIBT/PyMCNP
    cd PyMCNP
    uv venv
    source .venv/bin/activate
    uv pip install -e .[docs,test,dev]

## Using pip

### Released Version

The released versions of PyMCNP are available on [PyPI](https://pypi.org/project/pymcnp/) and can be "pip installed":

    pip install pymcnp

### Latest Version

The latest version of PyMCNP is available on [GitHub](https://github.com/FSIBT/PyMCNP) and can be "pip installed":

    pip install git+https://github.com/FSIBT/PyMCNP

### Developer Version

The PyMCNP source code is available on [GitHub](https://github.com/FSIBT/PyMCNP) for contributions ([guidelines](contributing.md)), suggestions, and bug reports:

    git clone https://github.com/FSIBT/PyMCNP
    cd PyMCNP
    pip install -e .[docs,test,dev]
