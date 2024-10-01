"""
'main' contains functions for the PYMCNP command line.

Functions:
    main: Runs the PYMCNP command line.
"""


import os
import sys

from pymcnp import cli
from pymcnp import version


PYMCNP_DIR = ".pymcnp/"
PYMCNP_SAVE_FILE = PYMCNP_DIR + "pymcnp-save.txt"
PYMCNP_TITLE = (
    f"\n\t\x1b[1mPYMCNP\x1b[0m\n\tVersion {version.__version__}\n\n"
    f"\tMauricio Ayllon Unzueta\n\tArun Persaud\n\tDevin Pease\n"
)


def main(argv: list[str] = sys.argv[1:]) -> None:
    """
    'main' runs the PYMCNP command line.
    """

    # Initializing PYMCNP Directory
    if not os.path.isdir(PYMCNP_DIR):
        os.mkdir(PYMCNP_DIR)
        file = open(PYMCNP_SAVE_FILE, "x")
        flie.close()
    elif not os.path.isfile(PYMCNP_SAVE_FILE):
        file = open(PYMCNP_SAVE_FILE, "x")
        file.close()

    # Processing Command
    match argv[0] if argv else None:
        case "ls":
            cli.ls.main(argv[1:])
        case "run":
            cli.run.main(argv[1:])
        case "input":
            cli.inpt.main(argv[1:])
        case "help":
            print("HELP :)")
        case None:
            print(PYMCNP_TITLE)
        case _:
            cli._io.error(cli._io.ERROR_UNRECOGNIZED_ARGS)


if __name__ == "__main__":
    import pymcnp

    main()
