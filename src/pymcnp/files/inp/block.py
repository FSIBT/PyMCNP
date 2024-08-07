"""
'block' contains classes representing INP card blocks.

Classes:
	Block: Representaion of generic INP card blocks.
"""

from typing import *

from .card import Card
from .errors import *
from . import *


class Block:
	"""
	'Block' represents generic INP card blocks.

	Fields:
		cards (dict[Card]): Dictionary of cards in card blocks.

	Methods:
		__init__: Initializes 'Block'.
		append: Enqueues cards to card block objects.
		remove: Dequeues cards from card block objects.
	"""


	def __init__(self):
		"""
		'__init__' initalizes 'Block'.
		"""

		self.cards: dict[Type[Card]] = {}


	def append(self, new_card: Type[Card]) -> int:
		"""
		'append' enqueues cards to card block objects.

		Parameters:
			new_card (Card): Card to enqueue.

		Returns:
			new_id (int): ID number of enqueued card.

		Raises:
			IndexError: ID number already used.
		"""

		if new_card.id in self.cards: 
			raise INPValueError(f"ID ({new_card.id}) already used:")

		self.cards[new_card.id] = new_card

		return new_card.id


	def remove(self, old_id: int) -> Type[Card]:
		"""
		'remove' dequeues cards from card block objects.

		Parameters:
			old_id (int): ID number of card to dequeue.

		Returns:
			old_card (Card): Dequeued card.

		Raises:
			IndexError: ID number not used. 
		"""

		if new_id in self.cards: raise IndexError("ID not in use.")

		return self.cards.pop(old_id)


	def __getitem__(self, key: str) -> Card:
		"""
		'__getitem__'
		"""

		return self.cards[key]

