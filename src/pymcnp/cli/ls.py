"""
'ls' contains functions for printing INP object information.

Functions:
	list_cells: Outputs strings of INP object cell information.
	list_surfaces: Outputs strings of INP object surface information.
	list_data: Outputs strings of INP object data information.
	list_inp: Outputs strings of all INP object information.
	main: Runs the command line for printing INP object information.
"""


import sys

from . import *
from ..files.inp import inp


def list_cells(inpt: inp.Inp) -> str:
	"""
	'list_cells' outputs strings of INP object cell information.

	Parameters:
		inpt (Inp): INP object.

	Returns:
		out (str): String of INP object cell information.
	"""

	out ="\x1b[4m{:^12.12}\x1b[24m \x1b[4m{:^12.12}\x1b[24m \x1b[4m{:^12.12}\x1b[24m \x1b[4m{:^25.25}\x1b[24m\n".format('NUMBER', 'MATERIAL', 'DENSITY', 'GEOMETRY')
	
	for cell in inpt.cells.cards.values():
		out += f"{cell.number:<12} {cell.material:<12} {cell.density if cell.density else '':<12} {cell.geometry.to_mcnp()}\n"
	
	return out


def list_surfaces(inpt: inp.Inp) -> str:
	"""
	'list_surfaces' outputs strings of INP object surface information.

	Parameters:
		inpt (Inp): INP object.

	Returns:
		out (str): String of INP object surface information.
	"""

	out ="\x1b[4m{:^12.12}\x1b[24m \x1b[4m{:^12.12}\x1b[24m \x1b[4m{:^12.12}\x1b[24m\n".format('NUMBER', 'MNEMONIC', 'TRANSFORM')
	
	for surface in inpt.surfaces.cards.values():
		out += f"{surface.number:<12} {surface.mnemonic:<12} {surface.transfrom if surface.transform else '':<12}\n"
	
	return out


def list_data(inpt: inp.Inp) -> str:
	"""
	'list_data' outputs strings of INP object datum information.

	Parameters:
		inpt (Inp): INP object.

	Returns:
		out (str): String of INP object datum information.
	"""

	out = "\x1b[4m{:^12.12}\x1b[24m \x1b[4m{:^12.12}\x1b[24m\n".format('MNEMONIC', 'NUMBER')
	
	for datum in inpt.data.cards.values():
		out += f"{datum.mnemonic:<12.12} {datum.number if datum.number else '':<12.12}\n"
	
	return out


def list_inp(inpt: inp.Inp) -> str:
	"""
	'list_inp' outputs strings of all INP object information.

	Parameters:
		inpt (Inp): INP object.

	Returns:
		out (str): String of all INP object information.
	"""

	return '\n' + list_cells(inpt) + '\n' + list_surfaces(inpt) + '\n' + list_data(inpt)


def main(argv: list[str] = sys.argv[1:]) -> None:
	"""
	'main' runs the command line for printing INP object information.
 
	Parameters:
		argv (list[str]): Arguments list. 
	"""
	
	inpts = get_save()

	match argv[0] if argv else None:
		case arg if arg is not None and arg[0] != '-':
			if argv[0] not in inpts: error(ERROR_ALIAS_NOT_FOUND)

			try:
				match argv[1] if argv[1:] else None:
					case '-c' | '--cells':
						print(list_cells(inpts[argv[0]][1]), end='')
					case '-s' | '--surfaces':
						print(list_surfaces(inpts[argv[0]][1]), end='')
					case '-d' | '--data':
						print(list_data(inpts[argv[0]][1]), end='')
					case '-a' | '--arguments':
						print(inpts[argv[0]][1].to_arguments())
					case None:
						print(list_inp(inpts[argv[0]][1]))
					case _:
						error(ERROR_UNRECOGNIZED_OPTION)
			except SyntaxError:
				error("INP SyntaxError")
			except ValueError:
				error("INP ValueError")

		case '-a' | '--all':
			for alias, value in inpts.items():
				path, inpt = value
				print(f"\n\x1b[4mOBJECT:\x1b[24m {alias}" + '\n' + list_inp(inpt))

		case None:
			print("\x1b[4m{:^25.25}\x1b[24m \x1b[4m{:^51.51}\x1b[24m \x1b[4m{:^51.51}\x1b[24m".format('NAME', 'TITLE', 'OTHER'))
			for name, value in inpts.items():
				path, inpt = value
				print(f"{name:<25.25} {inpt.title:<51.51} {repr(inpt.other):<51.51}")

