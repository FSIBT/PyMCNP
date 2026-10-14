# Installation

PyMCNP is accessible for installation through [PyPI](https://pypi.org/project/pymcnp/) and [GitHub](https://github.com/FSIBT/PyMCNP).

## Using uv (recommended)

We recommend [uv](https://docs.astral.sh/uv/) for installing PyMCNP. Optionally, create a virtual environment first, activate it, and install into it:

    uv venv
    source .venv/bin/activate
    uv pip install pymcnp

On Windows, activate the environment with `.venv\Scripts\activate` instead.

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

The latest version of PyMCNP is availiable on [GitHub](https://github.com/FSIBT/PyMCNP) and can be "pip installed":

    pip install git+https://github.com/FSIBT/PyMCNP

### Developer Version

The PyMCNP source code is availiable on [GitHub](https://github.com/FSIBT/PyMCNP) for contributions ([guidelines](contributing.md)), suggestions, and bug reports:

    git clone https://github.com/FSIBT/PyMCNP
    cd PyMCNP
    pip install -e .[docs,test,dev]
