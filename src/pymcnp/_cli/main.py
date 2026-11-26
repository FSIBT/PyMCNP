"""
Usage:
    pymcnp run [<args>...]
    pymcnp check [<args>...]
    pymcnp visualize [<args>...]
    pymcnp convert [<args>...]
    pymcnp plot [<args>...]
    pymcnp help [<command>]
    pymcnp --version

Commands:
    run        Run MCNP.
    check      Check that PyMCNP can parse an input file and that its lines fit
               in 80 columns; reformat it with --fix.
    visualize  Create a 3D visualization of an input file.
    convert    Convert OUTP, PTRAC, or MESHTAL files to CSV or parquet.
    plot       Plot the output of an MCNP simulation.
    help       Show help for a specific command.

Options:
    --version  Show the PyMCNP version.

PyMCNP helps create, run, analyze MCNP simulation input and output.
"""

import warnings

import rich.markup
from docopt import docopt

import pymcnp

from . import _io
from . import run
from . import check
from . import visualize
from . import convert
from . import plot


def _showwarning(message: Warning | str, category: type[Warning], filename: str, lineno: int, file=None, line: str | None = None) -> None:
    """
    Prints Python warnings as warning panels, without Python's source line; other than PyMCNP's own with their category.
    """

    text = str(message) if issubclass(category, pymcnp.abc.Warning) else f'{category.__name__}: {message}'
    _io.warning(rich.markup.escape(text))


def main() -> None:
    """
    Runs the PyMCNP command line interface.

    Warnings of every command are printed as warning panels.
    """

    showwarning = warnings.showwarning
    warnings.showwarning = _showwarning
    try:
        _main()
    finally:
        warnings.showwarning = showwarning


def _main() -> None:
    """
    Runs the PyMCNP command line interface commands.
    """

    args = docopt(__doc__, options_first=True, version=f'pymcnp {pymcnp.__version__}')

    if args['run']:
        run.main()
    elif args['check']:
        check.main()
    elif args['visualize']:
        visualize.main()
    elif args['convert']:
        convert.main()
    elif args['plot']:
        plot.main()
    elif args['help']:
        if args['<command>'] == 'run':
            print(str(run.__doc__)[1:-1])
        elif args['<command>'] == 'check':
            print(str(check.__doc__)[1:-1])
        elif args['<command>'] == 'visualize':
            print(str(visualize.__doc__)[1:-1])
        elif args['<command>'] == 'convert':
            print(str(convert.__doc__)[1:-1])
        elif args['<command>'] == 'plot':
            print(str(plot.__doc__)[1:-1])
        elif args['<command>'] is None:
            print(str(__doc__)[1:-1])
        else:
            print(str(plot.__doc__)[1:-1])


if __name__ == '__main__':
    main()  # pragma: no cover
