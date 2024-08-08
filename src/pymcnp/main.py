"""
'main' contains functions for the PYMCNP command line.

Functions:
	main: Runs the PYMCNP command line.
"""


import os
import sys
from typing import *

from . import version
from .cli import *
from .cli import run
from .cli import ls
from .cli import cq
from .cli import inpt
from .cli import _io
from .files._utils import parser
from .files._utils import errors
from .files._utils import types


PYMCNP_DIR = '.pymcnp/'
PYMCNP_SAVE_FILE = PYMCNP_DIR + 'pymcnp-save.txt'


def main(argv: list[str] = sys.argv[1:]) -> None:
	"""
	'main' runs the PYMCNP command line.
	"""

	# Initializing PYMCNP Directory
	if not os.path.isdir(PYMCNP_DIR):
		os.mkdir(PYMCNP_DIR)
		os.system(f"touch {PYMCNP_SAVE_FILE}")
	elif not os.path.isfile(PYMCNP_SAVE_FILE):
		os.system(f"touch {PYMCNP_SAVE_FILE}")

	# Processing Command
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
			_io.error(_io.ERROR_UNRECOGNIZED_ARGS)
	#except inp_errors.INPValueError as err:
		#_io.error(_io.ERROR_INP_VALUE(str(err)))
	#except inp_errors.INPSyntaxError as err:
		#_io.error(_io.ERROR_INP_SYNTAX(str(err)))


if __name__ == '__main__':
	main()

