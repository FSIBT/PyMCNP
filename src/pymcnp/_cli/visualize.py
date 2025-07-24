"""
Usage:
    pymcnp visualize <inp> [ options ]

Options:
    -c --cells          Visualize cells.
    -s --surfaces       Visualize surfaces.
    --pdf               Write PDF.
"""

import os
import pathlib

from docopt import docopt

from . import _io
from .. import errors
from ..Inp import Inp
from ..Visualize import Visualize


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
        if args['--pdf']:
            visualize.to_pdf_cells(_io.get_outfile(file, 'pdf', 'cells'))
        else:
            plot = visualize.to_show_cells()

            if 'PYTEST_CURRENT_TEST' not in os.environ:  # pragma: no cover
                plot.show()

    else:
        if args['--pdf']:
            visualize.to_pdf_surfaces(_io.get_outfile(file, 'pdf', 'surfaces'))
        else:
            plot = visualize.to_show_surfaces()

            if 'PYTEST_CURRENT_TEST' not in os.environ:  # pragma: no cover
                plot.show()

    _io.done()
