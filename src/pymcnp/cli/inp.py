"""
``inp`` provides utilities for aliasing PyMCNP INP objects.

``inp`` contains the procedures for executing the ``pymcnp inp`` command. This
module underpins the CLI by simplifying commands.
"""

import sys

import docopt

from .. import files
from . import _save


PYMCNP_INP_DOC = """
Usage:
    pymcnp inp ((--read <alias> <file>)|(--delete <alias>))

Options:
    -r --read       Read INP file and create alias.
    -d --delete     Delete alias.
"""


def main(argv: list[str] = sys.argv[1:]) -> None:
    """
    ``main`` executes the ``pymcnp inp`` command.

    ``main`` processes the given command line arguments, and creates or deletes
    PyMCNP aliased INP objects.

    Parameters:
        argv: Tokenized list of CLI arguments.
    """

    args = docopt.docopt(PYMCNP_INP_DOC, argv=argv)
    aliases = _save.Save.get_save()

    if args["--read"]:
        # Adding alias to save.
        aliases[args["<alias>"]] = (args["<file>"], files.inp.Inp.from_mcnp_file(args["<file>"]))
    elif args["--delete"]:
        # Removing alias from save.
        aliases.pop(args["<alias>"])

    _save.Save.set_save(aliases)
