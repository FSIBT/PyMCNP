"""
'surfaces' contains classes representing INP surface card blocks.

Classes:
	Surfaces: Representaion of INP surface card blocks.
"""


from typing import *

from .block import Block
from .surface import Surface
from .._utils import parser


class Surfaces(Block):
	"""
	'Surfaces' represents MNCP INP surface card blocks.
	"""


	def __init__(self) -> Self:
		"""
		'__init__' initalizes 'Surfaces'.
		"""

		super().__init__()


	@classmethod
	def from_mcnp(cls, source: str) -> Self:
		"""
		'from_mcnp' generates surface block objects from INP.

		Parameters:
			source (str): INP to parse.

		Returns:
			block (Surfaces): Surface block object.
		"""

		block = cls()

		lines = parser.Preprocessor.process_inp(source).split('\n')
		for line in lines:
			if line == '': break
			block.append(Surface.from_mcnp(line))

		return block


	def to_mcnp(self) -> str:
		"""
		'to_mcnp' generates INP from surface block objects.

		Returns:
			source (str): INP for surface block object.
		"""

		return '\n'.join([surface.to_mcnp() for surface in self.cards.values()] + [''])


	def to_arguments(self) -> list:
		"""
		'to_arguments' generates lists of surface card objects.

		Returns:
			arugments (list): List of surface blocks object.
		"""

		return [card.to_arguments() for card in self.cards.values()]


	def to_cadquery(self, hasHeader: Optional[bool] = False) -> str:
		"""
		'to_cadquery' generates cadquery from surface block objects.

		Parameters:
			hasHeader (bool): Boolean to include cadquery header.

		Returns:
			cadquery (str): Cadquery for surface block object.
		"""

		cadquery = 'import cadquery as cq\n\n' if hasHeader else ''
		surfaces_line = '\nsurfaces = cq.Workplane()'

		for surface in self.cards.values():
			if (hasattr(surface, 'to_cadquery')):
				new_cadquery = surface.to_cadquery(hasHeader = False)
				surfaces_line += f".add({new_cadquery.split(maxsplit=1)[0]})"
				cadquery += new_cadquery

		return cadquery + surfaces_line + '\n\n'


	def to_cadquery_file(self, filename: str) -> int:
		"""
		'to_cadquery_file' generates cadquery files from surface block objects.

		Parameters:
			filename (str): Output filename.
			hasHeader (bool): Boolean to include cadquery header.

		Returns:
			chars_written (int): Number of chars written to file.
		"""

		with open(filename, 'w') as file:
			return file.write(self.to_cadquery(hasHeader = True))

		return 0

