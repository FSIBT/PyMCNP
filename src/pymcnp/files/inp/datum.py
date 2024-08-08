"""
'datum' contains the class representing INP data cards.

Classes:
	Datum: Representation of INP data cards.
"""


from typing import *
import collections
import re

from .card import Card
from .._utils import parser
from .._utils import errors
from .._utils import types

class Datum(Card):
	"""
	'Datum' represents INP data cards.

	Fields:
		mnemonic (str): Data card mnemonic.

	Methods:
		__init__: Initializes 'Datum'.
		from_mcnp: Generates data card objects from INP.
		from_arguments: Generates data card objects from arguments.
		to_mcnp: Generates INP from data card objects.
		to_arguments: Generates list from data card objects.
		to_json: Generates JOSN from data card objects.
	"""

	
	MNUMONICS_GEOMETRY = ('vol', 'area', 'tr', 'trcl', 'u', 'lat', 'fill', 'uran', 'dawwg', 'dm', 'embed', 'embee', 'embeb', 'embem', 'embtb', 'embtm')
	MNUMONICS_MATERIAL = ('m', 'mt', 'mx', 'mpn', 'otfbd', 'totnu', 'nonu', 'awtab', 'xs', 'void', 'mgopt', 'drxs')
	MNUMONICS_PHYSICS = ('mode', 'phys', 'act', 'cut', 'elpt', 'tmp', 'thtme', 'mphys', 'lca', 'lcb', 'lcc', 'lea', 'leb', 'fmult', 'tropt', 'unc', 'cosp', 'cosy', 'bfld', 'bflcl', 'field')
	MNUMONICS_SOURCE = ('sdef', 'si', 'sp', 'sb', 'ds', 'sc', 'ssw', 'ssr', 'kcode', 'ksrc', 'kopts', 'hsrc', 'burn', 'source', 'srcdx')
	MNUMONICS_TALLY = ('f', 'fip', 'fir', 'fic', 'fc', 'e', 't', 'c', 'fq', 'fm', 'de', 'df', 'em', 'tm', 'cm', 'cf', 'sf', 'fs', 'sd', 'fu', 'tallyx', 'ft', 'tf', 'notrn', 'pert', 'kpert', 'ksen', 'tmesh', 'fmesh', 'spdtl')
	MNUMONICS_VARIANCE = ('imp', 'var', 'wwe', 'wwt', 'wwn', 'wwp', 'wwg', 'wwge', 'wwgt', 'mesh', 'esplt', 'tsplt', 'ext', 'vect', 'fcl', 'bxt', 'dd', 'pd', 'dxc', 'bbrem', 'pikmt', 'spabi', 'pwt')
	MNUMONICS_PERIPHERAL = ('nps', 'ctme', 'stop', 'print', 'talnp', 'prdmp', 'ptrac', 'mplot', 'histp', 'rand', 'dbcn', 'lost', 'idum', 'rdym', 'za', 'zb', 'zc', 'zd', 'files')
	
	MNUMONICS_ALL = ('vol', 'area', 'tr', 'trcl', 'u', 'lat', 'fill', 'uran', 'dawwg', 'dm', 'embed', 'embee', 'embeb', 'embem', 'embtb', 'embtm', 'm', 'mt', 'mx', 'mpn', 'otfbd', 'totnu', 'nonu', 'awtab', 'xs', 'void', 'mgopt', 'drxs', 'mode', 'phys', 'act', 'cut', 'elpt', 'tmp', 'thtme', 'mphys', 'lca', 'lcb', 'lcc', 'lea', 'leb', 'fmult', 'tropt', 'unc', 'cosp', 'cosy', 'bfld', 'bflcl', 'field', 'sdef', 'si', 'sp', 'sb', 'ds', 'sc', 'ssw', 'ssr', 'kcode', 'ksrc', 'kopts', 'hsrc', 'burn', 'source', 'srcdx', 'f', 'fip', 'fir', 'fic', 'fc', 'e', 't', 'c', 'fq', 'fm', 'de', 'df', 'em', 'tm', 'cm', 'cf', 'sf', 'fs', 'sd', 'fu', 'tallyx', 'ft', 'tf', 'notrn', 'pert', 'kpert', 'ksen', 'tmesh', 'fmesh', 'spdtl', 'imp', 'var', 'wwe', 'wwt', 'wwn', 'wwp', 'wwg', 'wwge', 'wwgt', 'mesh', 'esplt', 'tsplt', 'ext', 'vect', 'fcl', 'bxt', 'dd', 'pd', 'dxc', 'bbrem', 'pikmt', 'spabi', 'pwt', 'nps', 'ctme', 'stop', 'print', 'talnp', 'prdmp', 'ptrac', 'mplot', 'histp', 'rand', 'dbcn', 'lost', 'idum', 'rdym', 'za', 'zb', 'zc', 'zd', 'files')
	MNUMONICS_EXTENDED = ('m', 'mt', 'mx')


	def __init__(self) -> Self:
		"""
		'__init__' initalizes 'Datum'
		"""

		super().__init__()

		self.mnemonic: str = None
		self.number: int = None
		self.parameters: list[str] = []


	@classmethod
	def from_mcnp(cls, card: str) -> Self:
		"""
		'from_mcnp' generates data card objects from INP.

		Parameters:
			card (str): INP to parse.

		Returns:
			datum (Datum): Data card object.
		"""

		datum = cls()

		entries = Deque(card.lower().split(' '))
		if not entries: raise INPSyntaxError
		entry = entries.popleft()

		# Processing Mnumonic
		#if not entry.startswith(datum.MNUMONICS_ALL): raise INPSyntaxError(card)
		datum.id = entry
		mnemonic = re.findall(r"[^\W\d_]+|\d+", entry)
		if len(mnemonic) == 1:
			datum.mnemonic = mnemonic[0]
		elif len(mnemonic) > 1:
			datum.mnemonic = mnemonic[0]
			datum.number = mnemonic[1]

		#if not entries: raise INPSyntaxError(card)
		
		# Processing Parameters
		match datum.mnemonic:
			case _:
				datum.parameters += list(entries)

		return datum


	@classmethod
	def from_arguments(cls, mnemonic: str, parameters: list[str]) -> Self:
		"""
		'from_arguments' generates data card objects from arguments.

		Parameters:
			mnemonic (str): Data card mnemonic.
			parameters (list[str]): Data card parameters.

		Returns:
			datum (Data): Data card object.
		"""

		datum = cls()

		# Processing Mnemonic
		mnemonic = mnemonic.lower()
		if not mnemonic.startswith(datum.MNUMONICS_ALL): raise INPSyntaxError
		datum.mnemonic = mnemonic
		datum.id = datum.mnemonic

		# Processing Parameters
		datum.parameters = ' '.join(parameters)

		return datum


	def to_mcnp(self) -> str:
		"""
		'to_mcnp' generates INP from data card objects.

		Returns:
			source (str): INP for data card object.
		"""

		# Formatting Number
		number_str = f"{self.number}" if self.number is not None else ''

		return f"{self.mnemonic}{number_str} {' '.join(self.parameters)}"


	def to_arguments(self) -> list:
		"""
		'to_arguments' generates dictionaries from data card objects.

		Returns:
			arguments (list): Dictionary of data card object data.
		"""

		return {'mnemoinc': self.mnemonic, 'number': self.number, 'parameters': self.parameters}

