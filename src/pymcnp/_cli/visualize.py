"""
Usage:
    pymcnp visualize <inp> [ options... ]

Options:
    -c --cells                     Visualize all cells.
    -s --surfaces                  Visualize all surfaces.
    -c --cells-skip=<numbers>      Visualize all cells except listed cells.
    -s --surfaces-skip=<numbers>   Visualize all surfaces excepted listed surfaces.
    -c --cell=<numbers>            Visualize listed cells.
    -s --surface=<numbers>         Visualize listed surfaces.
    --pdf                          Write PDF.
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
    Executes the `pymcnp visualize` command.
    """

    _io.disclaimer()

    # Processing CLI arguments.
    args = docopt(__doc__)
    file = pathlib.Path(args['<inp>'])

    # Reading INP.
    try:
        inpt = Inp.from_file(file)
        visualize = Visualize(inpt)
    except errors.InpError as err:
        _io.error(str(err))
        exit(1)
    except errors.CliError as err:
        _io.error(str(err))
        exit(2)
    except errors.TypesError as err:
        _io.error(str(err))
        exit(3)

    if not (args['--cells-skip'] or args['--surfaces-skip'] or args['--cells'] or args['--surfaces'] or args['--cell'] or args['--surface']):
        args['--cells'] = True
        args['--surfaces'] = True

    # Visualizing!
    try:
        if args['--cells']:
            if args['--pdf']:
                visualize.to_pdf_cells(_io.get_outfile(file, 'pdf', 'cells'))
            else:
                plot = visualize.to_show_cells()

                if 'PYTEST_CURRENT_TEST' not in os.environ:  # pragma: no cover
                    plot.show()

        if args['--surfaces']:
            if args['--pdf']:
                visualize.to_pdf_surfaces(_io.get_outfile(file, 'pdf', 'surfaces'))
            else:
                plot = visualize.to_show_surfaces()

                if 'PYTEST_CURRENT_TEST' not in os.environ:  # pragma: no cover
                    plot.show()

        for number in args['--cells-skip']:
            number = tuple(map(int, number.split(',')))

            if args['--pdf']:
                visualize.to_pdf_cells(_io.get_outfile(file, 'pdf', 'cells'))
            else:
                plot = visualize.to_show_cells(skip=number)

                if 'PYTEST_CURRENT_TEST' not in os.environ:  # pragma: no cover
                    plot.show()

        for number in args['--surfaces-skip']:
            number = tuple(map(int, number.split(',')))

            if args['--pdf']:
                visualize.to_pdf_surfaces(_io.get_outfile(file, 'pdf', 'surfaces'))
            else:
                plot = visualize.to_show_surfaces(skip=number)

                if 'PYTEST_CURRENT_TEST' not in os.environ:  # pragma: no cover
                    plot.show()

        for number in args['--cell']:
            number = number.split(',')

            if args['--pdf']:
                visualize.to_pdf_cell(number, _io.get_outfile(file, 'pdf', f'cell_{number}'))
            else:
                plot = visualize.to_show_cell(number)

            if 'PYTEST_CURRENT_TEST' not in os.environ:  # pragma: no cover
                plot.show()

        for number in args['--surface']:
            number = number.split(',')

            if args['--pdf']:
                visualize.to_pdf_cells(number, _io.get_outfile(file, 'pdf', f'surface_{number}'))
            else:
                plot = visualize.to_show_surface(number)

                if 'PYTEST_CURRENT_TEST' not in os.environ:  # pragma: no cover
                    plot.show()
    except errors.TypesError as err:
        _io.error(str(err))
        exit(3)

    _io.done()
