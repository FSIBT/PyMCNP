"""
Usage:
    pymcnp check [options] <input_file>

Options:
    -f --fix                  Reformat input file.
    -o file --output=file     Write to file instead of overwriting the input file.
"""

from pathlib import Path
import sys

from docopt import docopt
from rich import print
from rich.panel import Panel

import pymcnp


def main() -> None:
    """Check the syntax of an input file.

    If `--fix` is given, reformat the output.
    If `--output=file` is given, write to an output file instead of stdout.
    """

    args = docopt(__doc__)

    input_file = Path(args['<input_file>'])

    print(
        Panel(
            '[orange3]Warning[/] PyMCNP is just getting started.'
            'Please double check the output to make sure everyhing is working as expected'
            'If you find an error, please report it at https://github.com/FSIBT/PyMCNP/issues'
        )
    )

    if not input_file.is_file():
        print(f'[red]ERROR[/] Input file {input_file} does not exists.')
        sys.exit(1)

    try:
        data = pymcnp.read_input(input_file)
    except:  # noqa
        print('[red]ERROR[/] Cannot read input file.')
        print(
            '     We would appreciate if you can report this '
            '(and if possible share the input file) at https://github.com/FSIBT/PyMCNP/issues'
            'Thanks! -- your PyMCNP team'
        )
        sys.exit(2)

    if args['--fix']:
        output = args['--output']
        if output is None:
            print(data.to_mcnp())
        else:
            output = Path(output)
            if output.is_file():
                print('[orange3]Warning[/] Overwriting existing file.')
            data.to_mcnp_file(output)
            print(':thumbs_up: Rewrote input file.')
    else:
        print(f':thumbs_up: Input file {input_file} can be parsed.')
