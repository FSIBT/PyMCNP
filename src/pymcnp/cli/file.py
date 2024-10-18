"""
``file`` provides utilities for aliasing PyMCNP file objects.

``file`` contains the procedures for executing the ``pymcnp file`` command.
This module underpins the CLI by simplifying commands.
"""

import sys

import docopt

from . import _state


PYMCNP_INP_DOC = """
Usage:
    pymcnp file <alias> ( --read=<file> | --delete )

Options:
    -r --read=<file>    Read INP file and create alias.
    -d --delete         Delete alias.
"""


def main(argv: list[str] = sys.argv[1:]) -> None:
    """
    ``main`` executes the ``pymcnp file`` command.

    ``main`` processes the given command line arguments, and creates or deletes
    PyMCNP aliased INP objects.

    Parameters:
        argv: Tokenized list of CLI arguments.
    """

    args = docopt.docopt(PYMCNP_INP_DOC, argv=argv)

    if args['--read']:
        # Adding alias to save.
        try:
            _state.table.append(args['<alias>'], args['--read'])
        except ValueError:
            print('ALREADY!')
    elif args['--delete']:
        # Removing alias from save.
        try:
            _state.table.remove(args['<alias>'])
        except ValueError:
            print('NOT THERE!')
