"""
'cq' contains functions for interacting with cadquery and cq-editor.

Functions:
	run_cadquery_file: Runs cq-editor on INP files.
	run_cadquery_object: Runs cq-editor on INP objects.
	main: Runs the command line for interacting with cadquery and cq-editor.
"""


import os
import sys
import datetime
from typing import *

from . import *
from ..inp import inp


def run_cadquery_file(filename: str, arguments: Optional[str] = '') -> None:
	"""
	'run_cadquery_file' runs cq-editor on INP file.

	Parameter:
		filename (str): Cadquery filename.
		arguments (str): Additional MCNP arguments.
	"""

	inpt = inp.Inp().from_mcnp_file(filename)
	inpt.surfaces.to_cadquery_file(filename + '.py', hasHeader = True)
	os.system(f"cq-editor {filename}.py {arguments}")


def run_cadquery_object(inpt: inp.Inp,  arguments: Optional[str] = '') -> None:
	"""
	'run_cadquery_object' runs cq-editor on INP objects.

	Parameter:
		inpt (Inp): INP object.
		arguments (str): Additional MCNP arguments.
	"""

	filename = f"cadquery-run-{datetime.datetime.utcnow().timestamp()}"
	inpt.surfaces.to_cadquery_file(filename + '.py', hasHeader = True)
	os.system(f"cq-editor {filename}.py {arguments}")


def main(argv: list = sys.argv[1:]) -> None:
	""" 
	'main' runs the command line for interacting with cadquery and cq-editor.

	Parameter:
		argv (list): Arguments list.
	"""

	inpts = get_save()

	match argv[0] if argv else None:
		case arg if arg is not None and arg[0] != '-':
			if argv[0] not in inpts: error(ERROR_ALIAS_NOT_FOUND)
				
			print(INFO_RUNNING_CQEDITOR)
			run_cadquery_object(inpts[argv[0]][1])

		case '-f' | '--file':
			if len(argv) < 2: error(ERROR_INSUFFICENT_ARGS)

			print(INFO_RUNNING_CQEDITOR)
			run_cadquery_file(argv[1])

		case None:
			error(ERROR_INSUFFICENT_ARGS)

		case _:
			error(ERROR_UNRECOGNIZED_OPTION)

