"""
Usage:
    pymcnp check <inp>

Lines wider than 80 columns are reported as errors. A card that PyMCNP cannot
parse is reported as a warning, since MCNP may still accept it. Checking stops
at the first such card, so run the check again after fixing it.
"""

import pathlib
import sys

from docopt import docopt

from . import _io
from .. import abc
from ..Check import Check


def main() -> None:
    """
    Executes the ``pymcnp check`` command.
    """

    # Processing CLI arguments.
    args = docopt(__doc__)

    file = pathlib.Path(args['<inp>'])

    checker = Check()

    # Checking input file.
    try:
        problems = checker.check(file)
    except abc.Error as err:
        _io.error(str(err))
        sys.exit(1)

    for problem in problems:
        match type(problem):
            case abc.Warning:
                _io.warning(str(problem))
            case abc.Error:
                _io.error(str(problem))

    _io.done()

    if problems:
        sys.exit(2)
