"""
Usage:
    pymcnp run [<args>...]
    pymcnp check [<args>...]
    pymcnp visualize [<args>...]
    pymcnp convert [<args>...]
    pymcnp plot [<args>...]
    pymcnp help <command>

Commands:
    run        Run MCNP.
    check      Check if we can parse an input file.
    visualize  Create a 3D visualization of an input file.
    convert    Convert the output of an MCNP run into a pandas dataframe.
    plot       Plot the output of an MCNP simulation.
    help       Show help for a specific command.

PyMCNP helps you create, run, analyze MCNP simulation input and output.
"""

import sys

from docopt import docopt

from . import run
from . import check
from . import visualize
from . import convert
from . import plot


def main() -> None:
    """
    Runs the PyMCNP command line interface.
    """

    args = docopt(__doc__, options_first=True)

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
        argv = sys.argv + ['--help']
        if args['<command>'] == 'run':
            docopt(run.__doc__, argv=argv)
        elif args['<command>'] == 'check':
            docopt(check.__doc__, argv=argv)
        elif args['<command>'] == 'visualize':
            docopt(visualize.__doc__, argv=argv)
        elif args['<command>'] == 'convert':
            docopt(convert.__doc__, argv=argv)
        elif args['<command>'] == 'plot':
            docopt(plot.__doc__, argv=argv)
        else:
            print(f'Unknown command: {args["<command>"]}')


if __name__ == '__main__':
    main()  # pragma: no cover
