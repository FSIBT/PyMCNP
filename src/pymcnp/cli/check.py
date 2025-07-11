"""
Usage:
    pymcnp check <inp> [options]

Options:
    -f --fix        Reformat input file.
"""

import os
import pathlib
import difflib

from docopt import docopt

from . import _io
from ..Inp import Inp
from ..utils import errors


class Check:
    """
    Checks OUTP files.

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

        try:
            with self.path.open('r') as file:
                current = file.read()
                correct = Inp.from_mcnp(current).to_mcnp()

                return difflib.unified_diff(current.split('\n'), correct.split('\n'))
        except FileNotFoundError:
            raise errors.CliError(errors.CliCode.SEMANTICS_PATH, self.path)

    def fix(self):
        """
        Fixes a file.
        """

        inp = Inp.from_file(self.path)

        if 'PYTEST_CURRENT_TEST' not in os.environ:  # pragma: no cover
            inp.to_file(self.path)


def main() -> None:
    """
    Executes the ``pymcnp check`` command.
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

    if args['--fix']:
        check.fix()

    _io.done()
