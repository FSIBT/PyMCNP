"""
'main' contains functions for the PYMCNP command line.

Functions:
	main: Runs the PYMCNP command line.
"""


import sys

from .cli import *
from .cli import run
from .cli import ls
from .cli import cq
from .cli import inpt
from .inp import errors as inp_errors


def main(argv: list[str] = sys.argv[1:]) -> None:
	"""
	'main' runs the PYMCNP command line.
	"""

	try:
		match argv[0] if argv else None:
			case 'ls':
				ls.main(argv[1:])
			case 'cq':
				cq.main(argv[1:])
			case 'run':
				run.main(argv[1:])
			case 'inpt':
				inpt.main(argv[1:])
			case 'help':
				pass
			case None:
				print("\n\t\x1b[1mPYMCNP\x1b[0m\n\tVersion 0.0\n\n\tMauricio Ayllon Unzueta\n\tArun Persaud\n\tDevin Pease\n")
			case _:
				error(ERROR_UNRECOGNIZED_ARGS)
	except inp_errors.INPValueError as err:
		error(ERROR_INP_VALUE(err.value))
	except inp_errors.INPSyntaxError as err:
		error(ERROR_INP_SYNTAX(err.value))


if __name__ == '__main__':
	main()

