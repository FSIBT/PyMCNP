"""
'inp' contains the class representing INP files.

Classes:
	Inp: Representation of INP files.
"""


from typing import *
import collections
import re

from .errors import *
from .block import Block
from .cells import Cells
from .surfaces import Surfaces
from .data import Data

from . import *
from .. import parser


class Inp:
	"""
	'Inp' represents INP files.

	Fields:
		message (str): INP message block.
		title (str): INP title block.
		cells (Cells): INP cell card block.
		surfaces (Surfaces): INP surface card block.
		data (Data): INP data card block.
		other (str): INP other block.

	Methods:
		__init__: Initializes 'Inp'.
		from_mcnp: Generates input objects from INP.
		from_mcnp_file: Generates input objects from INP files.
		from_arguments: Generates input objects from arguments.
		to_mcnp: Generates INP from input objects.
		to_mcnp_file: Generates INP files from input objects.
		to_arguments: Generates list from input objects.
	"""


	def __init__(self):
		"""
		'__init__' initializes 'Inp'.
		"""

		self.message: str = None
		self.title: str = None
		self.cells: Type[Cells] = Cells()
		self.surfaces: Type[surfaces] = Surfaces()
		self.data: Type[Data] = Data()
		self.other: str = None


	@classmethod
	def from_mcnp(cls, source: str) -> Self:
		"""
		'from_mcnp' generates input objects from INP.

		Parameters:
			source (str): INP to parse.

		Returns:
			inp (Input): Input object.
		"""
		
		inp = cls()

		lines = parser.Parser(preprocess_mcnp(source), '\n', EOFError)

		# Processing Message Block
		line = lines.peekl()
		if line[:9] == "message:":
			inp.message = lines.popl()

			while lines:
				inp.message += lines.popl()


		# Processing Title
		inp.title = lines.popl()

		# Processing Cell Cards
		index = list(lines.deque).index('')
		cell_lines = '\n'.join(lines.popl() for _ in range(0, index))
		inp.cells = Cells.from_mcnp(cell_lines)

		lines.popl()

		# Processing Surface Cards
		index = list(lines.deque).index('')
		surface_lines = '\n'.join(lines.popl() for _ in range(0, index))
		inp.surfaces = Surfaces.from_mcnp(surface_lines)
		
		lines.popl()

		# Processing Datum Cards
		index = list(lines.deque).index('')
		datum_lines = '\n'.join(lines.popl() for _ in range(0, index))
		inp.data = Data.from_mcnp(datum_lines)

		inp.other = ''
		while lines:
			inp.other += lines.popl()

		return inp


	@classmethod
	def from_mcnp_file(cls, filename: str) -> Self:
		"""
		'from_file' generates input objects from filenames.

		Parameters:
			filename (str): Name of file to parse.

		Returns:
			inp (Input): Input object.
		"""

		source = ''
		with open(filename, 'r') as file:
			source = ''.join(file.readlines())

		return cls.from_mcnp(source)
			

	@classmethod
	def from_arguments(cls, title: str, cells: Cells, surfaces: Surfaces, data: Data = Data(), message: Optional[str] = '', other: Optional[str] = '') -> str:
		"""
		'from_mcnp' generates input objects from INP.
			
		Parameters (str): INP to parse.
			title (str): INP title block.
			cells (Cells): INP cell block.
			surface (Surfaces): INP surface block.
			data (Optional[Data]): INP data block
			message (Optional[str]): INP message block.

		Returns:
			inp (Input): Input object.
		"""

		inp = cls()

		inp.message = message
		inp.title = title
		inp.cells = cells
		inp.surfaces = surfaces
		inp.data = data
		inp.other = other

		return inp


	def to_mcnp(self) -> str:
		"""
		'to_mcnp' generates INP from input objects.

		Returns:
			source (str): INP for input object.
		"""

		# Appending Message Block
		source = self.message + '\n' if self.message else ''

		# Appending Title Block
		if not self.title: raise INPValueError(INPValueError.Codes.INVALID_INP_TITLE)
		if len(self.title) > 80: raise INPValueError(INPValueError.Codes.INVALID_INP_TITLE)
		source += self.title + '\n'

		# Appending Blocks
		source += Cells.to_mcnp(self.cells) + '\n'
		source += Surfaces.to_mcnp(self.surfaces) + '\n'
		source += Data.to_mcnp(self.data) + '\n'

		return source


	def to_mcnp_file(self, filename: str) -> int:
		"""
		'to_mcnp_file' generates INP files from input objects.

		Parameters (str):
			filename (str): Output filename.
		"""

		with open(filename, 'w') as file:
			return file.write(self.to_mcnp())

		return 0


	def to_arguments(self) -> dict:
		"""
		'to_arguments' generates dictionaries from input objects.

		Returns:
			arguments (list): Dictionary of input object data.

		Returns:
			chars_written (int): Number of chars written to file.
		"""
		
		return {'message': self.message, 'title': self.title, 'cells': self.cells.to_arguments(), 'surfaces': self.surfaces.to_arguments(), 'data': self.data.to_arguments(), 'other': self.other}


	def set_title(self, title: str) -> None:
		"""
		'set_title'
		"""

		if title is None or len(self.title) > 80: raise INPValueError(INPValueError.Codes.INVALID_INP_TITLE)
		self.title = title

