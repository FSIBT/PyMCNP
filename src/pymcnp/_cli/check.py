"""
Usage:
    pymcnp check [options] <inp>

Options:
    -f --fix        Reformat input file.
    -d --diff       Show the changes --fix would make.

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
    Executes the `pymcnp check` command.
    """

    # Processing CLI arguments.
    args = docopt(__doc__)
    file = pathlib.Path(args['<inp>'])

    # Checking INP.
    try:
        check = Check(file)
        problems = check.problems()
    except abc.Error as err:
        _io.error(str(err))
        sys.exit(1)

    for problem in problems:
        report = _io.error if problem.kind == 'error' else _io.warning
        report(f'Line {problem.line}: {problem.message}')

    unparseable = any(problem.kind == 'warning' for problem in problems)

    if args['--diff'] and not unparseable:
        diff = [line.rstrip('\n') for line in check.check()]
        if diff:
            print('\n'.join(diff))

    # Fixing!
    if args['--fix']:
        if unparseable:
            _io.warning('Not reformatting, since PyMCNP cannot parse the file.')
        else:
            check.fix()

    if unparseable:
        sys.exit(2)

    if any(problem.kind == 'error' for problem in problems) and not args['--fix']:
        sys.exit(3)

    if not problems or args['--fix']:
        _io.done()
