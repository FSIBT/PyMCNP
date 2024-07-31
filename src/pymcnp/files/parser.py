"""
'parser'
"""


import re
import collections


class Parser():
	"""
	'Parser'
	"""

	def __init__(self, source: str, delimiter: str, err: Exception):
		"""
		'__init__'
		"""

		self.deque = collections.deque(re.split(delimiter, source))
		self.err = err


	def popl(self) -> str:
		"""
		'popl'
		"""

		if not bool(self): raise self.err
		return self.deque.popleft()


	def peekl(self) -> str:
		"""
		'peekl'
		"""

		if not bool(self): raise self.err
		return self.deque[0]


	def popr(self) -> str:
		"""
		'popr'
		"""

		if not bool(self): raise self.err
		return self.deque.pop()


	def peekr(self) -> str:
		"""
		'peekr'
		"""

		if not bool(self): raise self.err
		return self.deque[-1]


	def __len__(self):
		"""
		'__len__'
		"""
		
		return len(self.deque)


	def __bool__(self):
		"""
		'__bool__'
		"""

		return len(self.deque) != 0


	def __str__(self):
		"""
		'__str__'
		"""

		return str(list(self.deque))


class Deque():
	"""
	'Deque'
	"""


	def __init__(self, items: list[any], err: Exception):
		"""
		'__init__'
		"""

		self.deque = collections.deque(items)
		self.err = err


	def pushl(self, item: any) -> None:
		"""
		'pushl'
		"""

		self.deque.appendleft(item)


	def pushr(self, item: any) -> None:
		"""
		'pushr'
		"""

		self.deque.append(item)


	def popl(self) -> any:
		"""
		'popl'
		"""

		if not bool(self): raise self.err
		return self.deque.popleft()


	def peekl(self) -> str:
		"""
		'peekl'
		"""

		if not bool(self): raise self.err
		return self.deque[0]


	def popr(self) -> str:
		"""
		'popr'
		"""

		if not bool(self): raise self.err
		return self.deque.pop()


	def peekr(self) -> str:
		"""
		'peekr'
		"""

		if not bool(self): raise self.err
		return self.deque[-1]


	def __len__(self):
		"""
		'__len__'
		"""
		
		return len(self.deque)


	def __bool__(self):
		"""
		'__bool__'
		"""

		return len(self.deque) != 0


	def __str__(self):
		"""
		'__str__'
		"""

		return str(list(self.deque))
