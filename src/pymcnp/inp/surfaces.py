"""
'surfaces' contains classes representing INP surface card blocks.

Classes:
	Surfaces: Representaion of INP surface card blocks.
"""


from typing import *

from .block import Block
from .surface import Surface

from . import *


class Surfaces(Block):
	"""
	'Surfaces' represents MNCP INP surface card blocks.

	Methods:
		__init__: Initializes 'Surfaces'.
		from_mcnp: Generates surface block objects from INP.
		from_arguments: Generates surface block objects from arguments.
		to_mcnp: Generates INP from surface block objects.
		to_arguments: Generates lists of surface card objects.
		to_cadquery: Generates cadquery from surface block objects.
		to_cadquery_file: Generates cadquery file from surface block objects.
	"""


	def __init__(self):
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

		lines = preprocess_mcnp(source).split('\n')
		for line in lines:
			if line == '': break
			block.append(Surface.from_mcnp(line))

		return block


	@classmethod
	def from_arguments(cls, cell_cards: list[Surface]) -> Self:
		"""
		'from_arguments' generates surface block objects from arguments.

		Parameterrs:
			surface_cards (list): List of surface cards.
		"""

		surfaces = cls()

		for surface in surface_cards:
			surfaces.append(surface)

		return surfaces


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

		for surface in self.cards.values():
			surface_cadquery = surface.to_cadquery()
			if surface_cadquery:
				cadquery += surface_cadquery

		return cadquery + '\n'


	def to_cadquery_file(self, filename: str, hasHeader: Optional[bool] = False) -> int:
		"""
		'to_cadquery_file' generates cadquery files from surface block objects.

		Parameters:
			filename (str): Output filename.
			hasHeader (bool): Boolean to include cadquery header.

		Returns:
			chars_written (int): Number of chars written to file.
		"""

		with open(filename, 'w') as file:
			return file.write(self.to_cadquery(hasHeader))

		return 0

