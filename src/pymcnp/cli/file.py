"""
Usage:
    pymcnp [-h|--help] file <alias> (--read=<file> | --delete)

Options:
    -r <file>, --read=<file>    Read INP file and create alias.
    -d --delete                 Delete alias.
"""

from docopt import docopt

from . import _state


def main() -> None:
    """Defines or deletes aliases for input files."""

    args = docopt(__doc__)

    if args['--read']:
        try:
            _state.table.append(args['<alias>'], args['--read'])
        except ValueError:
            print('ALREADY!')
    elif args['--delete']:
        try:
            _state.table.remove(args['<alias>'])
        except ValueError:
            print('NOT THERE!')
