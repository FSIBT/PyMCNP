"""
Usage:
    pymcnp visualize [options...] <inp>

Options:
    --cells                        Visualize all cells.
    --surfaces                     Visualize all surfaces.
    --cells-skip=<numbers>         Visualize all cells except listed cells.
    --surfaces-skip=<numbers>      Visualize all surfaces excepted listed surfaces.
    -c --cell=<numbers>            Visualize listed cells.
    -s --surface=<numbers>         Visualize listed surfaces.
    --pdf                          Write PDF.
"""

import os
import sys
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

    # Processing CLI arguments.
    args = docopt(__doc__)
    file = pathlib.Path(args['<inp>'])

    # Reading INP.
    try:
        inpt = Inp.from_file(file)
        visualize = Visualize(inpt)
    except errors.InpError as err:
        _io.error(str(err))
        sys.exit(1)
    except errors.CliError as err:
        _io.error(str(err))
        sys.exit(2)
    except errors.TypesError as err:
        _io.error(str(err))
        sys.exit(3)

    if not (args['--cells-skip'] or args['--surfaces-skip'] or args['--cells'] or args['--surfaces'] or args['--cell'] or args['--surface']):
        args['--cells'] = True
        args['--surfaces'] = True

    for option, items in (('--cell', inpt.cells), ('--surface', inpt.surfaces), ('--cells-skip', inpt.cells), ('--surfaces-skip', inpt.surfaces)):
        known = {str(item.number) for item in items if hasattr(item, 'number')}

        for numbers in args[option]:
            missing = [number for number in numbers.split(',') if number not in known]

            if missing:
                _io.error(f'{option}: no such {"cell" if "cell" in option else "surface"}: {", ".join(missing)}.')
                sys.exit(2)

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
                visualize.to_pdf_cells(_io.get_outfile(file, 'pdf', 'cells-skip'), skip=number)
            else:
                plot = visualize.to_show_cells(skip=number)

                if 'PYTEST_CURRENT_TEST' not in os.environ:  # pragma: no cover
                    plot.show()

        for number in args['--surfaces-skip']:
            number = tuple(map(int, number.split(',')))

            if args['--pdf']:
                visualize.to_pdf_surfaces(_io.get_outfile(file, 'pdf', 'surfaces-skip'), skip=number)
            else:
                plot = visualize.to_show_surfaces(skip=number)

                if 'PYTEST_CURRENT_TEST' not in os.environ:  # pragma: no cover
                    plot.show()

        for number in args['--cell']:
            number = number.split(',')

            if args['--pdf']:
                visualize.to_pdf_cell(number, _io.get_outfile(file, 'pdf', 'cell-' + '_'.join(number)))
            else:
                plot = visualize.to_show_cell(number)

                if 'PYTEST_CURRENT_TEST' not in os.environ:  # pragma: no cover
                    plot.show()

        for number in args['--surface']:
            number = number.split(',')

            if args['--pdf']:
                visualize.to_pdf_surface(number, _io.get_outfile(file, 'pdf', 'surface-' + '_'.join(number)))
            else:
                plot = visualize.to_show_surface(number)

                if 'PYTEST_CURRENT_TEST' not in os.environ:  # pragma: no cover
                    plot.show()
    except errors.TypesError as err:
        _io.error(str(err))
        sys.exit(3)

    _io.done()
