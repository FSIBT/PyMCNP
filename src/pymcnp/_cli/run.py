"""
Usage:
    pymcnp run <inp>... [ options ]

Options:
    -c --command=<command>        Command to run.
    -p --path=<path>              Working directory.
"""

import os
import pathlib

from docopt import docopt

from . import _io
from .. import abc
from ..Inp import Inp
from ..Run import Run


def main() -> None:
    """
    Executes the `pymcnp run` command.
    """

    _io.disclaimer()

    # Processing CLI arguments.
    args = docopt(__doc__)
    path = args['--path'] if args['--path'] else os.getcwd()
    command = args['--command'] if args['--command'] else 'mcnp6'

    # Reading INP.
    try:
        inps = [Inp.from_file(path)[0] for path in map(pathlib.Path, args['<inp>'])]
    except abc.Error as err:
        _io.error(str(err))
        exit(1)

    # Running!
    try:
        Run(inps, command=command).run(pathlib.Path(path))
    except abc.Error as err:
        _io.error(str(err))
        exit(2)

    _io.done()
