"""
'ptrac'
"""


from enum import *
from typing import *
import tempfile
import collections
import multiprocessing

import mcnptools

from . import *
from .header import Header
from .history import History
from .. import parser


class Ptrac:
	"""
	'Ptrac'
	"""

	def __init__(self):
		"""
		'__init__'
		"""

		self.header: Header = None
		self.histories: list[History] = None


	@classmethod
	def from_mcnp(cls, source: str) -> Self:
		"""
		'from_mcnp'
		"""

		ptrac = cls()

		# Processing Header
		ptrac.header, lines = Header().from_mcnp(source)

		# Processing History
		ptrac.histories = []

		while lines:
			history, lines = History().from_mcnp(lines, ptrac.header)
			ptrac.histories.append(history)

		return ptrac


	@classmethod
	def from_mcnp_file(cls, filename: str):
		"""
		'from_mcnp_file'
		"""

		with open(filename, 'r') as file:
			source = '\n'.join(file.readlines())

		return self.from_mcnp(source)


	def to_arguments(self) -> dict:
		"""
		'to_arguments'
		"""

		return {'header': self.header.to_arguments(), 'histories': [history.to_arguments() for history in self.histories]}

