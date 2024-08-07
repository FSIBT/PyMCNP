import re


def preprocess_mcnp(string: str) -> str:
	processed_source = string.lower() + '\n'
	processed_source = re.sub(r'\t', '        ', processed_source)
	processed_source = re.sub(r' &\n     ', ' ', processed_source)
	processed_source = re.sub(r"([$].*\n?)|(\nc\n)", '\n', processed_source)
	processed_source = re.sub(r"\nc .*", '', processed_source)
	processed_source = re.compile(r" +").sub(" ", processed_source)
	processed_source = re.sub(r" \n", "\n", processed_source)
	processed_source = re.sub(r"\n ", " ", processed_source)

	return processed_source



def add_continuation_lines(string: str) -> str:
	out = ''
	line_length = 0
	words = string.split(' ')

	for word in words:
		if len(word) + line_length > 80 or len(word) + line_length > 78 and words:
			out += ' &\n     ' 
			line_length = 5

		out += word + ' '
		line_length += len(word) + 1

	return out


from typing import *
import re


CELL_PARAMS = ('imp', 'vol', 'pwt', 'ext', 'fcl', 'wwn', 'dxc', 'nonu', 'pd', 'tmp', 'u', 'trcl', '*tral', 'lat', 'fill', '*fill' 'elpt', 'cosy', 'bflcl', 'unc')
CELL_PARAMS_DESIGNATABLE = ('imp')
SURFACE_MNEMONICS = ('p', 'px', 'py', 'pz', 'so', 'cx', 'cy', 'cz', 's', 'sx', 'sy', 'sz', 'c/x', 'c/y', 'c/z', 'kx', 'ky', 'kz', 'k/x', 'k/y', 'k/z', 'sq', 'gq', 'tx', 'ty', 'tz', 'x', 'y', 'z', 'box', 'rec', 'rpp', 'sph', 'rcc', 'ell', 'rhp', 'hex', 'trc', 'wed', 'arb')
DESIGNATORS = ('n', 'p', 'e', 'l', 'q', 'u', 'v', 'f', 'h', 'l', '+', '-', 'x', 'y', 'o', '!', '<', '>', 'g', '/', 'z', 'k', '%', '^', 'b', '_', '~', 'c', 'w', '@', 'd', 't', 's', 'a', '*', '?', '#')

def is_integer(string: str, callback: Callable[int, bool] = lambda _ : True):
	try:
		return callback(int(string))
	except:
		return False


def is_real(string: str, callback: Callable[float, bool] = lambda _ : True):
	try:
		return callback(float(string))
	except:
		return False


# CELLS
def is_geometry(string: str):
	return string[0] in ['+', '(', '#', ':', '-'] or string[0].isnumeric()


def is_params_key(key: str):
	return key.startswith(CELL_PARAMS)


def is_params_item(key: str, value: any):
	if not key.startswith(CELL_PARAMS):
		return False

	match key:
		case 'imp':
			return is_integer(value, lambda i : 0 <= i)
		case 'vol':
			return is_real(value, lambda f : 0 < f)
		case _:
			return False


def is_params_designator(key: str, designator: str, callback: Callable[str, bool] = lambda _ : True):
	if not key.startswith(CELL_PARAMS_DESIGNATABLE):
		return False

	for symbol in designator.split(','):
		if symbol not in DESIGNATORS:
			return False

	return callback(designator)

# SURFACES
def is_mnemonic(string: str):
	string = string.lower()
	return string.startswith(SURFACE_MNEMONICS)

from . import inp
