import sys
import pathlib

from .. import files


def read_input(filename: pathlib.Path | str) -> files.inp.Inp:
    filename = pathlib.Path(filename)

    if not filename.is_file():
        print(f'[red]ERROR[/] Input file {filename} does not exists.')
        sys.exit(1)

    return files.inp.Inp.from_mcnp_file(filename)
