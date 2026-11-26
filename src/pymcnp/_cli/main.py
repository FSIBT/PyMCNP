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

Exit codes (of every command):
    0    Success.
    1    The input or output has problems, or the command failed.
    2    Usage error, or a file does not exist or cannot be read.
    3    PyMCNP cannot parse all of a file.

PyMCNP helps create, run, analyze MCNP simulation input and output.
"""

import sys
import warnings

from docopt import docopt
from docopt import DocoptExit

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
    _io.warning(text)


def main() -> None:
    """
    Runs the PyMCNP command line interface.

    Warnings of every command are printed as warning panels. Usage errors
    print the usage and exit with 2.
    """

    showwarning = warnings.showwarning
    warnings.showwarning = _showwarning
    try:
        _main()
    except DocoptExit as err:
        print(err, file=sys.stderr)
        sys.exit(_io.USAGE)
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
        commands = {'run': run, 'check': check, 'visualize': visualize, 'convert': convert, 'plot': plot}
        if args['<command>'] is None:
            print(str(__doc__)[1:-1])
        elif args['<command>'] in commands:
            print(str(commands[args['<command>']].__doc__)[1:-1])
        else:
            _io.fail(f'No command {args["<command>"]}; the commands are {", ".join(commands)}.', _io.USAGE)


if __name__ == '__main__':
    main()  # pragma: no cover
