"""Usage:
   mcnptools-format <inputfile>

Plots the input file and parsed and reformatted version side-by-side.
Works best on a wide screen. This program is at the moment mostly used
to veryfiy and test the parsing code.

"""


from pathlib import Path
from itertools import zip_longest
import sys

import docopt
from rich import print

import mcnptools as mt


def main():
    command = docopt.docopt(__doc__)
    # print(command)

    INPUT = Path(command["<inputfile>"])

    if not INPUT.is_file():
        print(f"[red]ERROR[/] Cannot find input file '{INPUT.absolute()}'.")
        sys.exit(1)

    orig = INPUT.read_text()

    new = mt.input_reader.Input(INPUT).to_mcnp()

    for a, b in zip_longest(orig.split("\n"), new.split("\n")):
        if a is None:
            a = ""
        if b is None:
            b = ""
        print(f"{a.rstrip():90s} | {b.rstrip():90s}")


if __name__ == "__main__":
    main()
