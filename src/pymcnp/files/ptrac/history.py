"""
'history'
"""


from typing import *

from . import *
from .event import Event
from .header import Header
from .. import parser
from .. import types


class History:
	"""
	'History'
	"""


	def __init__(self):
		"""
		'__init__'
		"""

		self.nps: int = None
		self.type: PtracEventType = None
		self.cell_number: int = None
		self.surface_number: int = None
		self.tally_number: int = None
		self.tfc: float = None
		self.events: list[Event] = None


	@classmethod
	def from_mcnp(cls, source: str, header: Header) -> tuple[Self, str]:
		"""
		'from_mcnp'
		"""

		history = cls()

		lines = parser.Parser(preprocess_ptrac(source), '\n', EOFError)

		# Processing I Lines
		entries = lines.pop().split(' ')
		if len(entries) != header.numbers[0]: raise SyntaxError
		#history.nps, history.type, history.cell_number, history.surface_number, history.tally_number, history.TFC = entries

		# Processing J & P Lines
		history.events = []

		entries = lines.peek().split(' ')
		while len(lines) >= 2 and types.cast_fortran_integer(entries[0]) is not None and types.cast_fortran_integer(entries[-1]) is not None:
			history.events.append(Event().from_mcnp(lines.pop() + '\n' + lines.pop()))

		return history, '\n'.join(list(lines.deque))


	def to_arguments(self) -> dict:
		"""
		'to_arguments'
		"""

		return {'nps': self.nps, 'type': self.type, 'cell_number': self.cell_number, 'surface_number': self.surface_number, 'tally_number': self.tally_number, 'tfc': self.tfc, 'events': [event.to_arguments() for event in self.events]}

