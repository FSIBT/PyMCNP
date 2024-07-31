"""
'header'
"""


from typing import *

from . import *
from .. import parser
from .. import types


class Header:
	"""
	'Header'
	"""


	def __init__(self):
		"""
		'__init__'
		"""

		self.code: str = None
		self.code_date: str = None
		self.version: str = None
		self.run_date: str = None
		self.run_time: str = None
		self.title: str = None
		self.settings: dict[PtracKeywords, list[float]] = {
			PtracKeywords.BUFFER: None,
			PtracKeywords.CELL: None,
			PtracKeywords.EVENT: None,
			PtracKeywords.FILE: None,
			PtracKeywords.FILTER: None,
			PtracKeywords.MAX: None,	
			PtracKeywords.MENP: None,
			PtracKeywords.NPS: None,	
			PtracKeywords.SURFACE: None,
			PtracKeywords.TALLY: None, 
			PtracKeywords.TYPE: None, 
			PtracKeywords.VALUE: None, 
			PtracKeywords.WRITE: None, 
			PtracKeywords.UNKNOWN: None, 
		}
		self.numbers: list[int] = None
		self.ids: list[int] = None


	@classmethod
	def from_mcnp(cls, source: str) -> tuple[Self, str]:
		"""
		'from_mcnp'
		"""

		header = cls()

		lines = parser.Parser(preprocess_ptrac(source), '\n', EOFError)

		# Processing Magic Number
		if lines.pop() != '-1': raise SyntaxError

		# Processing Header
		entries = parser.Parser(lines.pop(), ' ', EOFError)
		if len(entries) != 5: raise SyntaxError
		header.code, header.code_date, header.version, header.run_date, header.run_time = entries.deque

		# Processing Title
		line = lines.pop()
		if len(line) > 80: return SyntaxError
		header.title = line

		# Processing Input Block
		entries = parser.Parser(lines.pop(), ' ', EOFError)
		if len(entries) != 10: raise SyntaxError

		m = types.cast_fortran_real(entries.pop(), lambda f: f == 13 or f == 14 and int(f) - f == 0)
		if m is None: raise SyntaxError

		for i in range(0, int(m)):
			if not entries:
				entries = parser.Parser(lines.pop(), ' ', EOFError)
				if len(entries) != 10: raise SyntaxError

			n = types.cast_fortran_real(entries.pop(), lambda f: f >= 0 and int(f) - f == 0)
			if n is None: raise SyntaxError

			values = [None] * int(n)
			for j in range(0, int(n)):
				if not entries:
					entries = parser.Parser(lines.pop(), ' ', EOFError)
					if len(entries) != 10: raise SyntaxError

				values[j] = entries.pop()

			header.settings[PtracKeywords(i + 1)] = values

		while entries:
			if types.cast_fortran_real(entries.pop(), lambda f: f == 0) is None: raise ValueError

		# Processing Numbers
		entries = lines.pop().split(' ')
		if len(entries) != 20: raise SyntaxError
		header.numbers = [None] * 20

		for i, entry in enumerate(entries):
			n = types.cast_fortran_integer(entry, lambda i: i >= 0)
			if n is None: raise SyntaxError

			header.numbers[i] = n

		# Processing Entry Counts
		entries = parser.Parser(lines.pop(), ' ', EOFError)
		if len(entries) > 30: raise SyntaxError

		total = sum(header.numbers[:10])
		header.ids = [None] * total

		for i in range(0, total):
			if not entries:
				line = lines.pop()
				entries = parser.Parser(line, ' ', EOFError)
				if len(entries) > 30: raise SyntaxError

			header.ids[i] = entries.pop()

		while entries:
			if types.cast_fortran_real(entries.pop(), lambda f: f == 0) is None: raise ValueError

		return header, '\n'.join(list(lines.deque))


	def to_arguments(self):
		"""
		'to_arguments'
		"""

		return {'code': self.code, 'code_date': self.code_date, 'version': self.version, 'run_date': self.run_date, 'run_time': self.run_time, 'title': self.title, 'settings': self.settings, 'numbers': self.numbers, 'ids': self.ids}

