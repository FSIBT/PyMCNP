"""
Usage:
    pymcnp ls [<args>...]
    pymcnp run [<args>...]
    pymcnp file [<args>...]
    pymcnp ptrac [<args>...]
    pymcnp help <command>

Commands:
    ls      List aliases or alias content.
    run     Run MCNP.
    file    Create alias
    ptrac   Edit PTRAC files.
    help    Show help for a specific command

PyMCNP help you create, modify, and run MCNP simulations and aparse its output.

"""

import sys

from docopt import docopt

import pymcnp


def main() -> None:
    """The command line interface to PyMCNP."""

    args = docopt(__doc__, version=pymcnp.version.__version__, options_first=True)

    if args['ls']:
        pymcnp.cli.ls.main()
    elif args['run']:
        pymcnp.cli.run.main()
    elif args['file']:
        pymcnp.cli.file.main()
    elif args['help']:
        argv = sys.argv + ['--help']
        if args['<command>'] == 'file':
            docopt(pymcnp.cli.file.__doc__, argv=argv)
        elif args['<command>'] == 'ls':
            docopt(pymcnp.cli.ls.__doc__, argv=argv)
        elif args['<command>'] == 'run':
            docopt(pymcnp.cli.run.__doc__, argv=argv)
        else:
            print(f'Unknown command: {args["<command>"]}')


if __name__ == '__main__':
    main()
