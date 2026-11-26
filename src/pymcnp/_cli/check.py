"""
Usage:
    pymcnp check [options] <inp>

Options:
    -f --fix        Reformat input file.
    -d --diff       Show the changes --fix would make.

Lines wider than 80 columns are reported as errors. A card that PyMCNP cannot
parse is reported as a warning, since MCNP may still accept it. Checking stops
at the first such card, so run the check again after fixing it. --fix rewraps
cards, but not comments; lines it cannot shorten are reported as errors. It
writes the file as UTF-8.

Exit codes:
    0    No problems (or --fix left no line wider than 80 columns).
    1    Lines wider than 80 columns (with --fix, lines it cannot shorten).
    2    Usage error, or the file does not exist or cannot be read as text.
    3    PyMCNP cannot parse the file, e.g., a card or two cells with one
         number; --fix does not rewrite the file.
"""

import sys
import pathlib
import warnings

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
    check = _io.read(file, Check)
    problems = _io.read(file, lambda _: check.problems())

    unparseable = any(problem.kind == 'warning' for problem in problems)

    # With ``--fix``, the wide lines are reported after fixing, if ``--fix`` cannot shorten them.
    for problem in problems:
        if problem.kind == 'error' and args['--fix'] and not unparseable:
            continue
        report = _io.error if problem.kind == 'error' else _io.warning
        report(f'Line {problem.line}: {problem.message}')

    # The file was read; reading it again for --diff and --fix does not repeat its warning, e.g., read as Latin-1.
    with warnings.catch_warnings():
        warnings.filterwarnings('ignore', abc._text.NOT_UTF8, abc.Warning)
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
                    sys.exit(_io.PROBLEMS)

    if unparseable:
        sys.exit(_io.PARTLY_PARSED)

    if any(problem.kind == 'error' for problem in problems) and not args['--fix']:
        sys.exit(_io.PROBLEMS)

    if not problems or args['--fix']:
        _io.done()
