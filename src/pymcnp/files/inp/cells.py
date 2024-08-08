"""
'cells' contains classes representing INP cell card blocks.

'cells' packages the 'Cells' class, providing an importable interface
for INP cell card blocks.
"""


from typing import *

from .block import Block
from .cell import Cell


class Cells(Block):
	"""
	'Cells' represents MNCP INP cell card blocks.

	Methods:
		__init__: Initializes 'Cells'
		from_mcnp: Generates cell block objects from INP.
		from_arguments: Generates cell block objects from arguments.
		to_mcnp: Generates INP from cell block objects.
		to_arguments: Generates dictionaries from cell block objects.
	"""


	def __init__(self) -> Self:
		"""
		'__init__' initalizes 'Cells'.
		"""

		super().__init__()


	@classmethod
	def from_mcnp(cls, source: str) -> Self:
		"""
		'from_mcnp' generates cell block objects from INP.

		Parameters:
			source (str): INP to parse.

		Returns:
			block (Cells): Cell block object.
		"""

		block = cls()

		lines = preprocess_mcnp(source).split('\n')
		for line in lines:
			if line == '': break
			block.append(Cell.from_mcnp(line))

		return block


	def to_mcnp(self) -> str:
		"""
		'to_mcnp' generates INP from cell block objects.

		Returns:
			source (str): INP for cell block objects.
		"""

		return '\n'.join([cell.to_mcnp() for cell in self.cards.values()] + [''])


	def to_arguments(self) -> list:
		"""
		'to_arguments' generates lists of cell card objects.

		Returns:
			arguments (list): List of cell card objects.
		"""

		return [card.to_arguments() for card in self.cards.values()]

