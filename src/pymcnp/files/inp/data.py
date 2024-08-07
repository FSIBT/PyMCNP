"""
'data' contains classes representing INP data card blocks.

Classes:
	Data: Representaion of INP data card blocks.
"""


from typing import *

from .block import Block
from .datum import Datum

from . import *


class Data(Block):
	"""
	'Data' represents MNCP INP data card blocks.

	Methods:
		__init__: Initializes 'Data'
		from_mcnp: Generates data block objects from INP.
		from_arguments: Generates data block objects from arguments.
		to_mcnp: Generates INP from data block objects.
		to_arguments: Generates lists of datum card objects.
	"""


	def __init__(self):
		"""
		'__init__' initalizes 'Data'.
		"""

		super().__init__()


	@classmethod
	def from_mcnp(cls, source: str) -> Self:
		"""
		'from_mcnp' generates data block objects from INP.

		Parameters:
			source (str): INP to parse.

		Returns:
			block (Data): Data block object.
		"""

		block = cls()

		lines = preprocess_mcnp(source).split('\n')
		for line in lines:
			if line == '': break
			block.append(Datum.from_mcnp(line))

		return block


	@classmethod
	def from_arguments(cls, datum_cards: str) -> Self:
		"""
		'from_arguments' generates data block objects from arguments.

		Parameters:
			datum_cards (list): List of datum cards.
		"""

		data = cls()

		for datum in datum_cards:
			data.append(datum)

		return data


	def to_mcnp(self) -> str:
		"""
		'to_mcnp' generates INP from data block objects.

		Returns:
			source (str): INP for data block objects.
		"""

		return '\n'.join([datum.to_mcnp() for datum in self.cards.values()])


	def to_arguments(self) -> list:
		"""
		'to_arguments' generates lists of datum card objects.

		Returns:
			arguments (list): List of datum block objects.
		"""

		return [card.to_arguments() for card in self.cards.values()]

