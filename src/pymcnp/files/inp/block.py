"""
'block' contains classes representing INP card blocks.

'block' packages the 'Block' class, providing an importable interface
for generic INP card blocks.
"""


from typing import *

from . import card
from .._utils import errors


class Block:
	"""
	'Block' represents generic INP card blocks.

	'Block' abstracts the common properties of INP cell, surface, and
	data blocks. It represents INP card blocks as abstract syntax elements.

	Attributes:
		cards: Dictionary of cards in a card block indexed by their id attributes.
	"""


	def __init__(self) -> Self:
		"""
		'__init__' initalizes 'Block'.
		"""

		self.cards: dict[card.Card] = {}


	def append(self, new_card: card.Card) -> int:
		"""
		'append' enqueues cards to card block objects.

		'append' adds cards to the 'cards' dictionary. It stores
		cards at the index equals to their id attribute, but it
		raises errors if collisions occur. 'append' wraps the
		adctionary 'add' method with PYMCNP error handling.

		Parameters:
			new_card: Card to append.

		Returns:
			ID number of the append card.
		"""

		if new_card is None or new_card.id is None:
			return None

		if new_card.id in self.cards: 
			raise ValueError

		self.cards[new_card.id] = new_card

		return new_card.id


	def remove(self, old_id: int) -> card.Card:
		"""
		'remove' dequeues cards from card block objects.

		'remove' removes cards from the 'cards' dictionary given
		their id number. If no entry exists for the given key, 
		'remove' returns None. 'remove' wraps the dictionary 'pop'
		method with PYMCNP error handling.

		Parameters:
			old_id: ID number of card to remove.

		Returns:
			Removed card with the given id number.
		"""

		if old_id is None:
			return None

		try:
			return self.cards.pop(old_id)
		except KeyError:
			return None

