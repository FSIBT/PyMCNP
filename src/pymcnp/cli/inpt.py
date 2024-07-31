"""
'input' contains functions for printing PYMCNP object information.

Functions:
	main:
"""


import os
import re
import sys
import datetime

from . import *
from ..files.inp import inp
from ..files.inp import cell
from ..files.inp import surface
from ..files.inp import datum


def main(argv: list = sys.argv[1:]) -> None:
	"""
	'main' runs the command line for interacting with INP objects.

	Parameters:
		argv (list[str]): Arguments list.
	"""

	match argv[0] if argv else None:
		case '-r' | '--read':
			if len(argv) < 3: error(ERROR_INSUFFICENT_ARGS)

			if not os.path.isfile(argv[2]): error(ERROR_FILE_NOT_FOUND)
			inpt = inp.Inp.from_mcnp_file(argv[2])

			inpts = get_save()
			filename = f"mcnp-save-{datetime.datetime.utcnow().timestamp()}"
			inpts[argv[1]] = (filename, inpt)
			set_save(inpts)

			with open(filename, 'w') as file:
				file.write(inpts[argv[1]][1].to_mcnp())

		case '-w' | '--write':
			match argv[1] if argv[1:] else None:
				case '-c' | '--cell':
					if len(argv) < 4: error(ERROR_INSUFFICENT_ARGS)

					inpts = get_save()
					if argv[2] not in inpts: error(ERROR_ALIAS_NOT_FOUND)
					inpts[argv[2]][1].cells.append(cell.Cell().from_mcnp(argv[3]))

					with open(inpts[argv[2]][0], 'w') as file:
						file.write(inpts[argv[2]][1].to_mcnp())

					print(INFO_BUILD_CELL)

				case '-s' | '--surface':
					if len(argv) < 4: error(ERROR_INSUFFICENT_ARGS)
					
					inpts = get_save()
					if argv[2] not in inpts: error(ERROR_ALIAS_NOT_FOUND)
					inpts[argv[2]][1].surfaces.append(surface.Surface().from_mcnp(argv[3]))

					with open(inpts[argv[2]][0], 'w') as file:
						file.write(inpts[argv[2]][1].to_mcnp())

					print(INFO_BUILD_SURFACE)
					
				case '-d' | '--datum':
					if len(argv) < 4: error(ERROR_INSUFFICENT_ARGS)

					inpts = get_save()
					if argv[2] not in inpts: error(ERROR_ALIAS_NOT_FOUND)
					inpts[argv[2]][1].data.append(datum.Datum().from_mcnp(argv[3]))
					
					with open(inpts[argv[2]][0], 'w') as file:
						file.write(inpts[argv[2]][1].to_mcnp())

					print(INFO_BUILD_DATUM)

				case '-i' | '--inp':
					if len(argv) < 4: error(ERROR_INSUFFICENT_ARGS)

					inpt = inp.Inp.from_arguments(argv[3], inp.Cells(), inp.Surfaces(), inp.Data())
					filename = f"mcnp-save-{datetime.datetime.utcnow().timestamp()}"

					inpts = get_save()
					inpts[argv[2]] = (filename, inpt)
					set_save(inpts)

					with open(filename, 'w') as file:
						file.write(inpts[argv[2]][1].to_mcnp())

					print(INFO_BUILD_INP)

				case '-t' | '--title':
					if len(argv) < 4: error(ERROR_INSUFFICENT_ARGS)

					inpts = get_save()
					if argv[2] not in inpts: error(ERROR_ALIAS_NOT_FOUND)
					inpts[argv[2]][1].title = argv[3]

					with open(inpts[argv[2]][0], 'w') as file:
						file.write(inpts[argv[2]][1].to_mcnp())

					print(INFO_BUILD_TITLE)

				case '-o' | '--other':
					if len(argv) < 4: error(ERROR_INSUFFICENT_ARGS)

					inpts = get_save()
					if argv[2] not in inpts: error(ERROR_ALIAS_NOT_FOUND)
					inpts[argv[2]][1].other = argv[3]

					with open(inpts[argv[2]][0], 'w') as file:
						file.write(inpts[argv[2]][1].to_mcnp())

					print(INFO_BUILD_OTHER)

				case '-m' | '--message':
					if len(argv) < 4: error(ERROR_INSUFFICENT_ARGS)

					inpts = get_save()
					if argv[2] not in inpts: error(ERROR_ALIAS_NOT_FOUND)
					inpts[argv[2]][1].message = argv[3]

					with open(inpts[argv[2]][0], 'w') as file:
						file.write(inpts[argv[2]][1].to_mcnp())

					print(INFO_BUILD_MESSAGE)

				case None:
					error(ERROR_INSUFFICENT_ARGS)

				case _:
					error(ERROR_UNRECOGNIZED_OPTION)

		case '-d' | '--delete':
			if len(argv) < 2: error(ERROR_INSUFFICENT_ARGS)

			inpts = get_save()
			if argv[1] not in inpts: error(ERROR_ALIAS_NOT_FOUND)
			inpts.pop(argv[1])
			set_save(inpts)

		case None:
			error(ERROR_INSUFFICENT_ARGS)

		case _:
			error(ERROR_UNRECOGNIZED_OPTION)

