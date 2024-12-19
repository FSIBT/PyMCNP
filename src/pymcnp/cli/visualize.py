"""
Usage:
    pymcnp visualize <file>
"""

from docopt import docopt


def main() -> None:
    """
    Executes the ``pymcnp visualize`` command.

    ``pymcnp visualize`` visualizes INP files using PyVISTA.
    """

    args = docopt(__doc__)
    print(args)
