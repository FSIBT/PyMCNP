"""
'datum' contains the class representing INP data cards.

Classes:
	Datum: Representation of INP data cards.
"""


from typing import *
import collections
import re

from .card import Card
from .errors import *
from . import *


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

	CARD_SYNTAX = {
		'p4': [('a', 'float'), ('B', 'float'), ('C', 'float'), ('D', 'float')],
		'px': [('D', 'float')],
		'py': [('D', 'float')],
		'pz': [('D', 'float')],
		'so': [('r', 'float')],
		's': [('x', 'float'), ('y', 'float'), ('z', 'float'), ('r', 'float')],
		'sx': [('x', 'float'), ('r', 'float')],
		'sy': [('y', 'float'), ('r', 'float')],
		'sz': [('z', 'float'), ('r', 'float')],
		'c/y': [('x', 'float'), ('z', 'float'), ('r', 'float')],
		'c/z': [('x', 'float'), ('y', 'float'), ('r', 'float')],
		'cx': [('r', 'float')],
		'cy': [('r', 'float')],
		'cz': [('r', 'float')],
		'k/x': [('x', 'float'), ('y', 'float'), ('z', 'float'), ('t^2', 'float'), ('+-1' , 'float')],
		'k/y': [('x', 'float'), ('y', 'float'), ('z', 'float'), ('t^2', 'float'), ('+-1' , 'float')],
		'k/z': [('x', 'float'), ('y', 'float'), ('z', 'float'), ('t^2', 'float'), ('+-1' , 'float')],
		'kx': [('x', 'float'), ('t^2', 'float'), ('+-1', 'float')],
		'ky': [('y', 'float'), ('t^2', 'float'), ('+-1', 'float')],
		'kz': [('z', 'float'), ('t^2', 'float'), ('+-1', 'float')],
		'sq': [('A', 'float'), ('B', 'float'), ('C', 'float'), ('D', 'float'), ('E', 'float'), ('F', 'float'), ('G', 'float'), ('x', 'float'), ('y', 'float'), ('z', 'float')],
		'gq': [('A', 'float'), ('B', 'float'), ('C', 'float'), ('D', 'float'), ('E', 'float'), ('F', 'float'), ('G', 'float'), ('H', 'float'), ('J', 'float'), ('K', 'float')],
		'tx': [('x', 'float'), ('y', 'float'), ('z', 'float'), ('A', 'float'), ('B', 'float'), ('C', 'float')],
		'ty': [('x', 'float'), ('y', 'float'), ('z', 'float'), ('A', 'float'), ('B', 'float'), ('C', 'float')],
		'tz': [('x', 'float'), ('y', 'float'), ('z', 'float'), ('A', 'float'), ('B', 'float'), ('C', 'float')],
		'x2': [('xr1', '2darray')],
		'y2': [('yr1', '2darray')],
		'z2': [('zr1', '2darray')],
		'x4': [('xr1', '2darray'), ('xr2', '2darray')],
		'y4': [('yr1', '2darray'), ('yr2', '2darray')],
		'z4': [('zr1', '2darray'), ('zr2', '2darray')],
		'x6': [('xr1', '2darray'), ('xr2', '2darray'), ('xr3', '2darray')],
		'y6': [('yr1', '2darray'), ('yr2', '2darray'), ('yr3', '2darray')],
		'z6': [('zr1', '2darray'), ('zr2', '2darray'), ('zr3', '2darray')],
		'p9': [('xyz1' '3darray'), ('xyz2', '3darray'), ('xyz3', '3darray')],
		'box': [('v', '3darray'), ('a1', '3darray'), ('a2', '3darray'), ('a3', '3darray')],
		'rpp': [('xmin', 'float'), ('xmax', 'float'), ('ymin', 'float'), ('ymax', 'float'), ('zmin', 'float'), ('zmax', 'float')],
		'sph': [('v', '3darray'), ('r', 'float')],
		'rcc': [('v', '3darray'), ('h', '3darray'), ('r', 'float')],
		'rhp9': [('v', '3darray'), ('h', '3darray'), ('r', '3darray')],
		'hex9': [('v', '3darray'), ('h', '3darray'), ('r', '3darray')],
		'rhp15': [('v', '3darray'), ('h', '3darray'), ('r', '3darray'), ('s', '3darray'), ('t', '3darray')],
		'hex15': [('v', '3darray'), ('h', '3darray'), ('r', '3darray'), ('s', '3darray'), ('t', '3darray')],
		'rec10': [('v', '3darray'), ('h', '3darray'), ('v1', '3darray'), ('r', 'float')],
		'rec12': [('v', '3darray'), ('h', '3darray'), ('v1', '3darray'), ('v2', '3darray')],
		'trc': [('v', '3darray'), ('h', '3darray'), ('r1', 'float'), ('r2', 'float')],
		'ell': [('v1', '3darray'), ('v2', '3darray'), ('rm', 'float')],
		'wed': [('v', '3darray'), ('v1', '3darray'), ('v2', '3darray'), ('v3', '3darray')],
		'arb': [('a', '3darray'), ('b', '3darray'), ('c', '3darray'), ('d', '3darray'), ('e', '3darray'), ('f', '3darray'), ('g', '3darray'), ('h', '3darray'), ('n', '6darray')]
	}



	def __init__(self):
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

