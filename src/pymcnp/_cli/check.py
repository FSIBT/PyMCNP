"""
Usage:
    pymcnp check <inp> [options]

Options:
    -f --fix        Reformat input file.
"""

import pathlib

from docopt import docopt

from . import _io
from .. import errors
from ..Check import Check


def main() -> None:
    """
    Executes the `pymcnp check` command.
    """

    _io.disclaimer()

    # Processing CLI arguments.
    args = docopt(__doc__)
    file = pathlib.Path(args['<inp>'])

    # Reading INP.
    try:
        check = Check(file)
        check.check()
    except errors.InpError as err:
        _io.error(str(err))
        exit(1)
    except errors.CliError as err:
        _io.error(str(err))
        exit(2)
    except errors.TypesError as err:
        _io.error(str(err))
        exit(3)

    if args['--fix']:
        check.fix()

    _io.done()
