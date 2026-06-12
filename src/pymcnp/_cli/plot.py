"""
Usage:
    pymcnp plot <outp> <number> [ options ]

Options:
    --pdf       Write PDF.
"""

import os
import pathlib

import matplotlib.pyplot
import matplotlib.backends.backend_pdf
from docopt import docopt

from . import _io
from .. import abc
from ..Outp import Outp
from ..Plot import Plot


def main() -> None:
    """
    Executes the `pymcnp plot` command.
    """

    _io.disclaimer()

    # Processing CLI arguments.
    args = docopt(__doc__)
    number = args['<number>']
    file = pathlib.Path(args['<outp>'])

    # Reading output file.
    try:
        outp = Outp.from_file(file)[0]
        plot = Plot(outp)
    except abc.Error as err:
        _io.error(str(err))
        exit(1)

    # Plotting!
    try:
        if args['--pdf']:
            plot.to_pdf(number, pathlib.Path(_io.get_outfile(file, 'pdf')))
        else:
            plot.to_show(number)

            if 'PYTEST_CURRENT_TEST' not in os.environ:  # pragma: no cover
                matplotlib.pyplot.show()

            matplotlib.pyplot.close()
    except abc.Error as err:
        _io.error(str(err))
        exit(2)

    _io.done()
