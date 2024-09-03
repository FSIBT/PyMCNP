"""
'main' contains functions for the PYMCNP command line.

Functions:
    main: Runs the PYMCNP command line.
"""


import os
import sys

import pymcnp.cli
import pymcnp.version as version


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
        os.system(f"touch {PYMCNP_SAVE_FILE}")
    elif not os.path.isfile(PYMCNP_SAVE_FILE):
        os.system(f"touch {PYMCNP_SAVE_FILE}")

    # Processing Command
    match argv[0] if argv else None:
        case "ls":
            pymcnp.cli.ls.main(argv[1:])
        case "run":
            pymcnp.cli.run.main(argv[1:])
        case "input":
            pymcnp.cli.inpt.main(argv[1:])
        case "help":
            print("HELP :)")
        case None:
            print(PYMCNP_TITLE)
        case _:
            pymcnp.cli._io.error(_io.ERROR_UNRECOGNIZED_ARGS)


if __name__ == "__main__":
    main()
