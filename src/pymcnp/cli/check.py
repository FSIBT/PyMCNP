"""
Usage:
    pymcnp check [options] <file>

Options:
    -f --fix                  Reformat input file.
"""

import pathlib
import difflib

from docopt import docopt

from . import _io
from .. import files


def main() -> None:
    """
    Executes the ``pymcnp check`` command.

    ``pymcnp check`` checks INP file syntax.
    """

    _io.warning()

    # Processing CLI arguments.
    args = docopt(__doc__)
    file = pathlib.Path(args['<file>'])

    # Reading INP file.
    try:
        inp = files.inp.Inp.from_mcnp_file(file)
    except files.utils.errors.McnpError as err:
        _io.error(err.__str__())
    except FileNotFoundError:
        _io.error(f'[red][bold]IoError:[/][/] ``{file}`` not found.')

    # Running ``diff``!
    with open(file, 'r') as file:
        diff = difflib.unified_diff(file.readlines(), inp.to_mcnp().split('\n'))
        _io.print('\n'.join(line.rstrip('\n') for line in diff))

    # Handling ``--fix``.
    if args['--fix']:
        inp.to_mcnp_file(file)

    _io.done()
