"""
Usage:
    pymcnp check [options] <inp>

Options:
    -f --fix        Reformat input file.
    -d --diff       Show the changes --fix would make.

Lines wider than 80 columns are reported as errors. A card that PyMCNP cannot
parse is reported as a warning, since MCNP may still accept it. Checking stops
at the first such card, so run the check again after fixing it. --fix rewraps
cards, but not comments; lines it cannot shorten are reported as errors.

Exit codes:
    0    No problems (or --fix left no line wider than 80 columns).
    1    Lines wider than 80 columns (with --fix, lines it cannot shorten).
    2    The file does not exist.
    3    PyMCNP cannot parse a card; --fix does not rewrite the file.
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

    # Checking INP.
    try:
        check = Check(file)
        problems = check.problems()
    except abc.Error as err:
        _io.error(str(err))
        sys.exit(2)

    unparseable = any(problem.kind == 'warning' for problem in problems)

    # With ``--fix``, the wide lines are reported after fixing, if ``--fix`` cannot shorten them.
    for problem in problems:
        if problem.kind == 'error' and args['--fix'] and not unparseable:
            continue
        report = _io.error if problem.kind == 'error' else _io.warning
        report(f'Line {problem.line}: {problem.message}')

    if args['--diff'] and not unparseable:
        diff = [line.rstrip('\n') for line in check.check()]
        if diff:
            print('\n'.join(diff))

    if args['--fix']:
        if unparseable:
            _io.warning('Not reformatting, since PyMCNP cannot parse the file.')
        else:
            remaining = check.fix()
            for problem in remaining:
                _io.error(f'Line {problem.line}: {problem.message} --fix cannot shorten this line, e.g., a long comment; shorten it by hand.')
            if remaining:
                sys.exit(1)

    if unparseable:
        sys.exit(3)

    if any(problem.kind == 'error' for problem in problems) and not args['--fix']:
        sys.exit(1)

    if not problems or args['--fix']:
        _io.done()
