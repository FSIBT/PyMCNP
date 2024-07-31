"""
'event'
"""


from typing import *

from . import *
from ..parser import *
from ..types import *


class Event:
	"""
	'Event'
	"""


	def __init__(self):
		"""
		'__init__'
		"""

		self.J: list[int] = None
		self.P: list[float] = None


	@classmethod
	def from_mcnp(cls, source: str) -> tuple[Self, str]:
		"""
		'from_mcnp'
		"""

		event = cls()

		lines = Parser(preprocess_ptrac(source), '\n', EOFError)
		if len(lines) != 2: raise SyntaxError

		# Processing J Line
		event.J = []

		entries = lines.pop().split(' ')
		for entry in entries:
			value = cast_fortran_real(entry)
			if value is None: raise ValueError

			event.J.append(value)

		# Processing P Line
		event.P = []

		entries = lines.pop().split(' ')
		for entry in entries:
			value = cast_fortran_real(entry)
			if value is None: raise ValueError

			event.P.append(value)

		return event


	def to_arguments(self) -> dict:
		"""
		'to_arguments'
		"""

		return {'j_line': self.J, 'p_line': self.P}