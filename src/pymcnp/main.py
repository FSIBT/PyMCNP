"""
``main`` the PYMCNP command line entrypoint.

``main`` runs the PyMCNP command line using ``docopt``. This module implemented
PyMCNP as a script (``python3 main.py``) and command (``pymcnp``).
"""

import sys

import docopt

import pymcnp


PYMCNP_DIR = '.pymcnp/'
PYMCNP_SAVE_FILE = f'{PYMCNP_DIR}pymcnp-save.txt'

PYMCNP_TITLE = f"""
    \x1b[1mPyMCNP\x1b[0m
    Version {pymcnp.version.__version__}

    Mauricio Ayllon Unzueta
    Arun Persaud
    Devin Pease
"""

PYMCNP_DOC = """
\x1b[1mpymcnp\x1b[0m - Python interface for MCNP.

Usage:
    pymcnp [<command> [<args>...]]

Commands:
    ls      List aliases or alias content.
    run     Run MCNP.
    file    Edit INP files.
    ptrac   Edit PTRAC files.
    help    Show help.
"""


def main(argv: list[str] = sys.argv[1:]) -> None:
    """
    ``main`` executes the ``pymcnp`` command.

    ``main`` processes the given command line arguments, and selects the
    corresponding subcommand.

    Parameters:
        argv: Tokenized list of CLI arguments.
    """

    args = docopt.docopt(
        PYMCNP_DOC, argv=argv, version=pymcnp.version.__version__, options_first=True
    )

    match args['<command>']:
        case 'ls':
            pymcnp.cli.ls.main(argv=argv)
        case 'run':
            pymcnp.cli.run.main(argv=argv)
        case 'file':
            pymcnp.cli.file.main(argv=argv)
        case 'help':
            print(PYMCNP_DOC)
        case None:
            print(PYMCNP_TITLE)
        case _:
            print(PYMCNP_DOC)


if __name__ == '__main__':
    import pymcnp

    main()
