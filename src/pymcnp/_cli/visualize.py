"""
Usage:
    pymcnp visualize [options...] <inp>

Options:
    --cells                        Visualize all cells.
    --surfaces                     Visualize all surfaces.
    --cells-skip=<numbers>         Visualize all cells except listed cells.
    --surfaces-skip=<numbers>      Visualize all surfaces except listed surfaces.
    -c --cell=<numbers>            Visualize listed cells.
    -s --surface=<numbers>         Visualize listed surfaces.
    --pdf                          Write PDF.

Options may be given more than once; each gives its own plot, e.g., -c 1 -c 2,3
shows cell 1, then cells 2 and 3 together.

Exit codes:
    0    Visualized.
    1    PyMCNP cannot parse the input or visualize it.
    2    Usage error, e.g., no such cell or surface, or the file does not exist
         or cannot be read as text.
    3    PyMCNP cannot parse all of the input; the part before is visualized.
"""

import sys
import pathlib

from docopt import docopt

from . import _io
from .. import abc
from ..Inp import Inp
from ..Visualize import Visualize


def main() -> None:
    """
    Executes the ``pymcnp visualize`` command.
    """

    # Processing CLI arguments.
    args = docopt(__doc__)
    file = pathlib.Path(args['<inp>'])

    # Reading input file.
    inpt, remainder = _io.read(file, Inp.from_file, 'card')

    partly = _io.partly_parsed(file, remainder)

    if not (args['--cells-skip'] or args['--surfaces-skip'] or args['--cells'] or args['--surfaces'] or args['--cell'] or args['--surface']):
        args['--cells'] = True
        args['--surfaces'] = True

    for option, items in (('--cell', inpt.cells), ('--surface', inpt.surfaces), ('--cells-skip', inpt.cells), ('--surfaces-skip', inpt.surfaces)):
        known = {int(item.j) for item in items if hasattr(item, 'j')}

        for numbers in args[option]:
            try:
                wanted = [int(number) for number in numbers.split(',')]
            except ValueError:
                _io.fail(f'{option}: expected numbers separated by commas, e.g., 1,2, not {numbers}.', _io.USAGE)

            missing = [str(number) for number in wanted if number not in known]
            if missing:
                _io.fail(f'{option}: no such {"cell" if "cell" in option else "surface"}: {", ".join(missing)}.', _io.USAGE)

    visualize = Visualize()

    # Visualizing!
    try:
        if args['--cells']:
            if args['--pdf']:
                out = _io.get_outfile(file, 'pdf', 'cells')
                visualize.to_pdf_cells(inpt, out)
                _io.info(f'Wrote {out}')
            else:
                plot = visualize.to_show_cells(inpt)

                plot.show()

        if args['--surfaces']:
            if args['--pdf']:
                out = _io.get_outfile(file, 'pdf', 'surfaces')
                visualize.to_pdf_surfaces(inpt, out)
                _io.info(f'Wrote {out}')
            else:
                plot = visualize.to_show_surfaces(inpt)

                plot.show()

        for number in args['--cells-skip']:
            number = tuple(map(int, number.split(',')))

            if args['--pdf']:
                out = _io.get_outfile(file, 'pdf', 'cells-skip')
                visualize.to_pdf_cells(inpt, out, skip=number)
                _io.info(f'Wrote {out}')
            else:
                plot = visualize.to_show_cells(inpt, skip=number)

                plot.show()

        for number in args['--surfaces-skip']:
            number = tuple(map(int, number.split(',')))

            if args['--pdf']:
                out = _io.get_outfile(file, 'pdf', 'surfaces-skip')
                visualize.to_pdf_surfaces(inpt, out, skip=number)
                _io.info(f'Wrote {out}')
            else:
                plot = visualize.to_show_surfaces(inpt, skip=number)

                plot.show()

        for number in args['--cell']:
            number = [item.strip() for item in number.split(',')]

            if args['--pdf']:
                out = _io.get_outfile(file, 'pdf', 'cell_' + '_'.join(number))
                visualize.to_pdf_cell(inpt, out, *number)
                _io.info(f'Wrote {out}')
            else:
                plot = visualize.to_show_cell(inpt, *number)

                plot.show()

        for number in args['--surface']:
            number = [item.strip() for item in number.split(',')]

            if args['--pdf']:
                out = _io.get_outfile(file, 'pdf', 'surface_' + '_'.join(number))
                visualize.to_pdf_surface(inpt, out, *number)
                _io.info(f'Wrote {out}')
            else:
                plot = visualize.to_show_surface(inpt, *number)

                plot.show()
    except abc.Error as err:
        _io.fail(str(err), _io.PROBLEMS)

    if partly:
        sys.exit(_io.PARTLY_PARSED)

    _io.done()
