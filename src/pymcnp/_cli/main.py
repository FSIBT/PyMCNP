"""
Usage:
    pymcnp run [<args>...]
    pymcnp check [<args>...]
    pymcnp visualize [<args>...]
    pymcnp convert [<args>...]
    pymcnp plot [<args>...]
    pymcnp help [<command>]

Commands:
    run        Run MCNP.
    check      Check if we can parse an input file.
    visualize  Create a 3D visualization of an input file.
    convert    Convert the output of an MCNP run into a pandas dataframe.
    plot       Plot the output of an MCNP simulation.
    help       Show help for a specific command.

PyMCNP helps you create, run, analyze MCNP simulation input and output.
"""

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
