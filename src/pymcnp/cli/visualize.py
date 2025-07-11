"""
Usage:
    pymcnp visualize <inp> [ options ]

Options:
    -c --cells           Visualize cells.
    -s --surfaces        Visualize surfaces.
"""

import os
import pathlib

import pyvista
from docopt import docopt

from . import _io
from ..Inp import Inp
from ..utils import errors


PLOT = pyvista.Plotter()


class Visualize:
    """
    Visualizes INP files.

    Attributes:
        inp: Files to visualize.
    """

    def __init__(self, inp: Inp):
        """
        Initializes ``Visualize``.

        Parameters:
            inp: Files to visualize.
        """

        if inp is None:
            raise errors.CliError(errors.CliCode.SEMANTICS_INP, inp)

        self.inp = inp

    def draw_cells(self):
        """
        Visualizes INP cells.
        """

        # vis = self.inp.draw()
        # PLOT.add_mesh(vis.data)
        # PLOT.show(off_screen="PYTEST_CURRENT_TEST" in os.environ)

    def draw_surfaces(self):
        """
        Visualizes INP surfaces.
        """

        vis = self.inp.draw()
        plot = pyvista.Plotter()
        plot.add_mesh(vis.data)

        if 'PYTEST_CURRENT_TEST' not in os.environ:
            plot.show()  # pragma: no cover


def main() -> None:
    """
    Executes the ``pymcnp visualize`` command.
    """

    _io.disclaimer()

    # Processing CLI arguments.
    args = docopt(__doc__)
    file = pathlib.Path(args['<inp>'])

    # Reading INP.
    try:
        inp = Inp.from_file(file)
        visualize = Visualize(inp)
    except errors.InpError as err:
        _io.error(str(err))
        exit(1)
    except errors.CliError as err:
        _io.error(str(err))
        exit(2)

    # Visualizing!
    if args['--cells']:
        visualize.draw_cells()
    else:
        visualize.draw_surfaces()

    _io.done()
