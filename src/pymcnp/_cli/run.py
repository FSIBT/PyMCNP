"""
Usage:
    pymcnp run [options] <inp>...

Options:
    -c --command=<command>        MCNP command to run (default: mcnp6, found on PATH).
    -p --path=<path>              Directory for the runs (default: the current directory).

Each input runs in its own directory, <path>/pymcnp-<timestamp>/run-0000N/. Exits
with 1 if an input cannot be read, 2 if a run failed, and 3 (running nothing) if
PyMCNP cannot parse a card of an input.
"""

import os
import sys
import pathlib

from docopt import docopt

from . import _io
from .. import abc
from ..Inp import Inp
from ..Run import Run


def main() -> None:
    """
    Executes the ``pymcnp run`` command.
    """

    # Processing CLI arguments.
    args = docopt(__doc__)
    path = args['--path'] if args['--path'] else os.getcwd()
    command = args['--command'] if args['--command'] else 'mcnp6'

    # Reading input file.
    try:
        parses = [(file, *Inp.from_file(file)) for file in map(pathlib.Path, args['<inp>'])]
    except abc.Error as err:
        _io.error(str(err))
        sys.exit(1)

    # Running a partly parsed input would run another problem, so run nothing.
    if [file for file, _, remainder in parses if _io.partly_parsed(file, remainder)]:
        _io.warning('Not running, since PyMCNP cannot parse all inputs.')
        sys.exit(3)

    inps = [inpt for _, inpt, _ in parses]

    # Running!
    try:
        Run(inps, command=command).run(pathlib.Path(path))
    except abc.Error as err:
        _io.error(str(err))
        sys.exit(2)

    _io.done()
