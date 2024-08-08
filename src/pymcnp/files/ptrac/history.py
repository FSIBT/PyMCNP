"""
'history'
"""


from typing import *

from . import *
from .event import Event
from .header import Header
from .._utils import parser
from .._utils import types


class History:
	"""
	'History'
	"""


	def __init__(self) -> Self:
		"""
		'__init__'
		"""

		self.header: Header = None
		self.next_type: EventTypes = None

		self.nps: int = None
		self.ncl: int = None
		self.nsf: int = None
		self.jptal: int = None
		self.tal: int = None

		self.events: list[Event] = None


	def set_nps(self, nps: int) -> None:
		"""
		'set_nps'
		"""

		if nps is None:
			raise ValueError

		self.nps = nps


	def set_ncl(self, ncl: int) -> None:
		"""
		'set_ncl'
		"""

		if ncl is None:
			raise ValueError

		self.ncl = ncl


	def set_nfs(self, nfs: int) -> None:
		"""
		'set_nfs'
		"""

		if nfs is None:
			raise ValueError

		self.nfs = nfs


	def set_jptal(self, jptal: int) -> None:
		"""
		'set_jptal'
		"""

		if jptal is None:
			raise ValueError

		self.jptal = jptal


	def set_tal(self, tal: int) -> None:
		"""
		'set_tal'
		"""

		if tal is None:
			raise ValueError

		self.tal = tal


	def set_next_type(self, next_type: Event.EventTypes) -> None:
		"""
		'set_next_type'
		"""

		if next_type is None:
			return ValueError

		self.next_type = next_type


	@classmethod
	def from_mcnp(cls, source: str, header: Header) -> tuple[Self, str]:
		"""
		'from_mcnp'
		"""

		history = cls()
		history.header = header

		lines = parser.Parser(preprocess_ptrac(source), '\n', EOFError)

		# Processing I Line
		tokens = parser.Parser(lines.popl(), ' ', SyntaxError)
		if len(tokens) != header.numbers[0]: raise SyntaxError

		for i in range(0, header.numbers[0]):
			match header.ids[i]:
				case '1':
					value = cast_fortran_integer(tokens.popl())
					history.set_nps(value)
				case '2':
					value = Event.EventTypes.cast_mcnp_event_types(tokens.popl())
					history.set_next_type(value)
				case '3':
					value = cast_fortran_integer(tokens.popl())
					history.set_ncl(value)
				case '4':
					value = cast_fortran_integer(tokens.popl())
					history.set_nsf(value)
				case '5':
					value = cast_fortran_integer(tokens.popl())
					history.set_jptal(value)
				case '6':
					value = cast_fortran_real(tokens.popl())
					history.set_tal(value)

		# Processing J & P Lines
		events = []

		tokens = parser.Parser(lines.peekl(), ' ', SyntaxError) 

		next_type = history.next_type
		while next_type != Event.EventTypes.FLAG:
			event = Event().from_mcnp(lines.popl() + '\n' + lines.popl(), history.header, next_type)
			events.append(event)
			next_type = event.next_type

		history.events = tuple(events)

		return history, '\n'.join(list(lines.deque))


	def to_arguments(self) -> dict:
		"""
		'to_arguments'
		"""

		return {'nps': self.nps, 'ncl': self.ncl, 'nsf': self.nsf, 'jptal': self.jptal, 'tal': self.tal, 'events': [event.to_arguments() for event in self.events]}

