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


class Check:
    """
    Checks MCNP files.

    Attribute:
        path: File to check.
    """

    def __init__(self, path: str | pathlib.Path):
        """
        Initializes ``Check``.

        Attribute:
            path: File to check.

        Raises:
            CLIError: SEMANTICS_PATH.
        """

        if path is None:
            raise errors.CliError(errors.CliCode.SEMANTICS_PATH, path)

        self.path = pathlib.Path(path)

    def check(self):
        """
        Checks a file.
        """

        with self.path.open('r') as file:
            current = file.read()
            correct = Inp.from_mcnp(current).to_mcnp()

            return difflib.unified_diff(current.split('\n'), correct.split('\n'))

    def fix(self):
        """
        Fixes a file.
        """

        Inp.from_file(self.path).to_file(self.path)


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
        check = Check(file)
        check.check()
    except errors.InpError as err:
        _io.error(str(err))
        exit(1)
    except errors.CliError as err:
        _io.error(str(err))
        exit(2)

    if args['--fix']:
        check.fix()

    _io.done()
