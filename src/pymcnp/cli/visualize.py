"""
Usage:
    pymcnp check [--fix] <input>

Options:
    -f --fix                  Reformat input file.
    -o file --output=file     Write to file instead of overwriting the input file.
"""

from docopt import docopt


def main() -> None:
    """Check the syntax of an input file.

    If `--fix` is given, reformat the output.
    """

    args = docopt(__doc__)
    print(args)
