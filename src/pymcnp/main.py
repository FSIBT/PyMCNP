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
    help       Show help for a specific command

PyMCNP helps you create, modify, and run MCNP simulations and aparse its output.
"""

import sys

from docopt import docopt

import pymcnp


def main() -> None:
    """The command line interface to PyMCNP."""

    args = docopt(__doc__, version=pymcnp.version.__version__, options_first=True)

    if args['run']:
        pymcnp.cli.run.main()
    elif args['check']:
        pymcnp.cli.check.main()
    elif args['visualize']:
        pymcnp.cli.visualize.main()
    elif args['convert']:
        pymcnp.cli.convert.main()
    elif args['plot']:
        pymcnp.cli.plot.main()
    elif args['help']:
        argv = sys.argv + ['--help']
        if args['<command>'] == 'run':
            docopt(pymcnp.cli.run.__doc__, argv=argv)
        elif args['<command>'] == 'check':
            docopt(pymcnp.cli.check.__doc__, argv=argv)
        elif args['<command>'] == 'visualize':
            docopt(pymcnp.cli.visualize.__doc__, argv=argv)
        elif args['<command>'] == 'convert':
            docopt(pymcnp.cli.convert.__doc__, argv=argv)
        elif args['<command>'] == 'plot':
            docopt(pymcnp.cli.plot.__doc__, argv=argv)
        else:
            print(f'Unknown command: {args["<command>"]}')


if __name__ == '__main__':
    main()
