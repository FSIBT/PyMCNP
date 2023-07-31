"""Usage:
   mcnptools-format (-s|-u|-n) <inputfile>

Options:
  -s --side-by-side    plot old and new side by side
  -u --unified         unified diff
  -n                   new file only

Plots the input file and parsed and reformatted version side-by-side.
Works best on a wide screen. This program is at the moment mostly used
to veryfiy and test the parsing code.

"""


import difflib
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

    if command["--side-by-side"]:
        for a, b in zip_longest(orig.split("\n"), new.split("\n")):
            if a is None:
                a = ""
            if b is None:
                b = ""
            print(f"{a.rstrip():<90} | {b.rstrip():<90}")
    elif command["--unified"]:
        a, b = orig.split("\n"), new.split("\n")
        for line in difflib.unified_diff(a, b, fromfile="original", tofile="formatted"):
            if line[0] == "+":
                print(f"[green]{line[0]}[/]{line[1:]}")
            elif line[0] == "-":
                print(f"[red]{line[0]}[/]{line[1:]}")
            else:
                print(line)
    else:
        print(new)


if __name__ == "__main__":
    main()
