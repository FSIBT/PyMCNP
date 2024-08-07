"""
'main' contains functions for the PYMCNP command line.

Functions:
	main: Runs the PYMCNP command line.
"""


import sys

from . import version
from .cli import *
from .cli import run
from .cli import ls
from .cli import cq
from .cli import inpt
from .files.inp import errors as inp_errors


def main(argv: list[str] = sys.argv[1:]) -> None:
	"""
	'main' runs the PYMCNP command line.
	"""

	#try:
	match argv[0] if argv else None:
		case 'ls':
			ls.main(argv[1:])
		case 'cq':
			cq.main(argv[1:])
		case 'run':
			run.main(argv[1:])
		case 'input':
			inpt.main(argv[1:])
		case 'help':
			print("HELP :)")
		case None:
			print(f"\n\t\x1b[1mPYMCNP\x1b[0m\n\tVersion {version.__version__}\n\n\tMauricio Ayllon Unzueta\n\tArun Persaud\n\tDevin Pease\n")
		case _:
			error(ERROR_UNRECOGNIZED_ARGS)
	#except inp_errors.INPValueError as err:
		#error(ERROR_INP_VALUE(str(err)))
	#except inp_errors.INPSyntaxError as err:
		#error(ERROR_INP_SYNTAX(str(err)))


if __name__ == '__main__':
	main()

