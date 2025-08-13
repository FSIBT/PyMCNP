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
from .. import errors
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

    # Reading OUTP.
    try:
        outp = Outp.from_file(file)
        plot = Plot(outp)

        # Plotting!
        if args['--pdf']:
            plot.to_pdf(number, pathlib.Path(_io.get_outfile(file, 'pdf')))
        else:
            plot.to_show(number)

            if 'PYTEST_CURRENT_TEST' not in os.environ:  # pragma: no cover
                matplotlib.pyplot.show()

            matplotlib.pyplot.close()
    except errors.OutpError as err:
        _io.error(str(err))
        exit(1)
    except errors.CliError as err:
        _io.error(str(err))
        exit(2)
    # except errors.TypesError as err:
    # _io.error(str(err))
    # exit(3)

    _io.done()
