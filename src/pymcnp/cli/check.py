"""
Usage:
    pymcnp check <inp> [options]

Options:
    -f --fix        Reformat input file.
"""

import pathlib
import difflib

from docopt import docopt

from . import _io
from ..Inp import Inp
from ..utils import errors


def main() -> None:
    """
    Executes the ``pymcnp check`` command.
    """

    _io.disclaimer()

    # Processing CLI arguments.
    args = docopt(__doc__)
    file = pathlib.Path(args['<inp>'])

    # Reading INP file.
    try:
        inp = Inp.from_mcnp_file(file)
    except errors.InpError as err:
        _io.error(str(err))
        exit(1)
    except errors.CliError as err:
        _io.error(str(err))
        exit(2)

    # Checking!
    with open(file, 'r') as file:
        diff = difflib.unified_diff(file.read().split('\n'), inp.to_mcnp().split('\n'))
        _io.print('\n'.join(line.rstrip('\n') for line in diff))

    if args['--fix']:
        inp.to_mcnp_file(file)

    _io.done()
