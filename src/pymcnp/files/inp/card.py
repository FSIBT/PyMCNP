"""
'card' contains classes representing INP cards.

'card' packages the 'Card' class, providing an importable inferace
for generic INP cards.
"""


from typing import *


class Card:
	""" 
	'Card' represents generic INP cards.

	'Card' abstracts the commonalities of INP cell, surface, and data
	cards. It represents INP cards as abstract syntax elements.

	Attributes:
		id: Card identifier.
		line: Line number.
		comment: Inline comment.
	"""


	def __init__(self) -> Self:
		"""
		'__init__' initalizes 'Card'.
		"""

		self.id: Union[int, str] = None
		self.line: int = None
		self.comment: str = None

