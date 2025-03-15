"""
Usage:
    pymcnp visualize <inp> [ options ]

Options:
    -c --cells           Visualize cells.
    -s --surfaces        Visualize surfaces.
"""

import pathlib

from docopt import docopt

from . import _io
from ..Inp import Inp
from ..utils import errors
from ..utils import _visualization


def main() -> None:
    """
    Executes the ``pymcnp visualize`` command.
    """

    _io.disclaimer()

    # Processing CLI arguments.
    args = docopt(__doc__)
    inp = pathlib.Path(args['<inp>'])

    # Reading INP file(s).
    try:
        inp = Inp.from_mcnp_file(inp)
    except errors.InpError as err:
        _io.error(str(err))
        exit(1)
    except errors.CliError as err:
        _io.error(str(err))
        exit(2)

    # Visualizing!
    surfaces = {surface.number: surface.to_pyvista() for surface in inp.surfaces}

    if args['--cells']:
        vis = inp.cells.to_pyvista(surfaces)
        vis.data.plot()
    else:
        vis = sum(surfaces.values(), _visualization.McnpVisualization())
        vis.data.plot()

    _io.done()
