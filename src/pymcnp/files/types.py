"""
'types'
"""


import re
from typing import *
from enum import StrEnum


Z_PATTERN = re.compile(r"\A[+-]?[0-9]+\Z")
R_PATTERN = re.compile(r"\A[+-]?(([0-9]+)|([0-9]+[.][0-9]*))([Ee]([+-][0-9]+))?\Z")

DESIGNATORS = {'n', 'q', 'p', 'e', 'f', '|', '!', 'u', '<', 'v', '>', 'h', 'g', 'l', 'b', '+', '_', '-', '~', 'x', 'c', 'y', 'w', 'o', '@', '/', '*', 'z', 'k', '?', '%', '^', 'd', 't', 's', 'a', '#'}


def cast_fortran_integer(string: str, hook: Callable[int, bool] = lambda _ : True) -> int:
	"""
	'cast_fortran_integer'
	"""

	if Z_PATTERN.match(string) is not None:
		value = int(string)
		if hook(value):
			return value

	return None


def cast_fortran_real(string: str, hook: Callable[float, bool] = lambda _ : True) -> float:
	"""
	'cast_fortran_real'
	"""

	if R_PATTERN.match(string) is not None:
		value = float(string)
		if hook(value):
			return value

	return None


class Designator(StrEnum):
	"""
	'Designator'
	"""


	NEUTRON = 'n'
	ANTI_NEUTRON = 'q'
	PHOTON = 'p'
	ELECTRON = 'e'
	POSITRON = 'f'
	NEGATIVE_MUON = '|'
	POSITIVE_MUON = '!'
	ELECTRON_NEUTRINO = 'u'
	ANTI_ELECTRON_NEUTRINO = '<'
	MUON_NEUTRINO = 'v'
	ANTI_MUON_MEUTRINO = '>'
	PROTON = 'h'
	ANTI_PROTON = 'g'
	LAMBDA_BARYON = 'l'
	ANTI_LAMBDA_BARYON = 'b'
	POSITIVE_SIGMA_BARYON = '+'
	ANTI_POSITIVE_SIGMA_BARYON = '_'
	NEGATIVE_SIGMA_BARYON = '-'
	ANTI_NEGATIVE_SIGMA_BARYON = '~'
	CASCADE = 'x'
	ANTI_CASCADE = 'c'
	NEGATIVE_CASCADE = 'y'
	POSITIVE_CASCADE = 'w'
	OMEGA_BARYON = 'o'
	ANTI_OMEGA_BARYON = '@'
	POSITIVE_PION = '/'
	NEGATIVE_PION = '*'
	NEUTRAL_PION = 'z'
	POSITIVE_KAON = 'k'
	NEGATIVE_KAON = '?'
	SHORT_KAON = '%'
	LONG_KAON = '^'
	DEUTERON = 'd'
	TRITON = 't'
	HELION = 's'
	ALPHA = 'a'
	HEAVY_IONS = '#'


	@classmethod
	def cast_mcnp_designator(cls, string: str) -> tuple[Self]:
		"""
		'cast_mcnp_designator'
		"""

		string = string.lower()

		designators = []

		for substring in string.split(','):
			try:
				designators.append(cls(substring))
			except:
				return None

		return tuple(designators) if designators else None

