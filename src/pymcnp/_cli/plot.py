"""
Usage:
    pymcnp plot [options] <outp> <number>

Arguments:
    <outp>      MCNP output (OUTP) file.
    <number>    Tally number, e.g., 1 for F1 or 14 for F14.

Options:
    --pdf       Write all figures to <outp> with the extension .pdf instead of
                showing them.

Exit codes:
    0    Plotted.
    2    Usage error, e.g., the tally is not in the file, or the file does not
         exist or cannot be read as text.
    3    PyMCNP cannot parse all of the file, e.g., a file of another kind,
         or the tally is in a layout PyMCNP cannot parse yet. The tally is
         plotted if it is in the part PyMCNP parsed.
"""

import sys
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
    Executes the ``pymcnp plot`` command.
    """

    # Processing CLI arguments.
    args = docopt(__doc__)
    number = args['<number>']
    file = pathlib.Path(args['<outp>'])

    # Reading output file.
    outp, remainder = _io.read(file, Outp.from_file)

    partly = _io.partly_parsed(file, remainder, 'line')

    plotter = Plot()

    # Plotting!
    try:
        if args['--pdf']:
            plotter.to_pdf(outp, number, pathlib.Path(_io.get_outfile(file, 'pdf')))
        else:
            plotter.to_show(outp, number)

            matplotlib.pyplot.show()

            matplotlib.pyplot.close()
    except abc.Error as err:
        # A tally that is in the file but not parsed is PyMCNP's limit, not a usage error.
        unparsed = str(number).strip() in outp._unparsed_tallies()
        _io.fail(str(err), _io.PARTLY_PARSED if unparsed else _io.USAGE)

    if partly:
        sys.exit(_io.PARTLY_PARSED)

    _io.done()
