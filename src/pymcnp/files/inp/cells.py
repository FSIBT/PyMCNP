"""
'cells' contains classes representing INP cell card blocks.

'cells' packages the 'Cells' class, providing an importable interface
for INP cell card blocks.
"""


from typing import *

from .block import Block
from .cell import Cell
from .._utils import parser


class Cells(Block):
	"""
	'Cells' represents MNCP INP cell card blocks.

	'Cells' abstracts the INP cell card syntax element and it
	encapsulates all functionallity for parsing cell card blocks.
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

		'from_mcnp' constructs instances of 'Cells' from
		INP strings, so it functions as a class constructor.

		Parameters:
			source: INP to parse.

		Returns:
			Cell block object.
		"""

		block = cls()

		lines = parser.Preprocessor.process_inp(source).split('\n')
		for line in lines:
			if line == '': break
			block.append(Cell.from_mcnp(line))

		return block


	def to_mcnp(self) -> str:
		"""
		'to_mcnp' generates INP from cell block objects.

		'to_mcnp' provides an MCNP endpoints for writing
		INP source strings.

		Returns:
			INP for cell block objects.
		"""

		return '\n'.join([cell.to_mcnp() for cell in self.cards.values()] + [''])


	def to_arguments(self) -> list:
		"""
		'to_arguments' generates lists of cell card objects.

		'to_arguments' creates dictionaries whose keys are 
		attribute names, and whose values are attribute value.

		Returns:
			List of cell card objects.
		"""

		return [card.to_arguments() for card in self.cards.values()]

