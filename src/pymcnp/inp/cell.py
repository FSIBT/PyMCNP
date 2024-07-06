"""
'cell' contains the class representing INP cell cards.

Classes:
	Cell: Representation of INP cell cards.
"""


from typing import *
import collections
import re

from .card import Card
from .errors import *
from . import *


class Cell(Card):
	"""
	'Cell' represents INP cell cards.

	Fields:
		number (int): Cell card number.
		material (int): Cell material number.
		density (int): Cell density value.
		geometry (str): Cell geometry specification.
		parameters (dict[float]): Cell parameter table.

	Methods:
		__init__: Initializes 'Cell'.
		from_mcnp: Generates cell card objects from INP.
		from_arguments: Generates cell card objects from arguments.
		to_mcnp: Generates INP from cell card objects.
		to_arguments: Generates dictionaries from cell card objects.
	"""


	def __init__(self):
		"""
		'__init__' initializes 'Cell'.
		"""

		super().__init__()

		self.number: int = None
		self.mateiral: int = None
		self.density: float = None
		self.geometry: str = ''
		self.parameters: dict[str, Union[tuple, float]] = {}


	@classmethod
	def from_mcnp(cls, card: str) -> Self:
		"""
		'from_mcnp' generates cell card objects from INP.

		Parameters:
			card (str): INP to parse.

		Returns:
			cell (Cell): Cell card object.
		"""

		cell = cls()

		entries = Deque(card.lower().split(' '))
		if not entries: raise INPSyntaxError
		entry = entries.popleft()
		
		# Processing Card Number
		if not is_integer(entry, lambda i : 1 <= i and i <= 99_999_999): raise INPValueError(entry)
		cell.number = int(entry)
		cell.id = cell.number

		if not entries: raise INPSyntaxError
		entry = entries.popleft()

		# Processing Material Number
		if not is_integer(entry, lambda i : 0 <= i and i <= 99_999_999): raise INPValueError
		cell.material = int(entry)

		if not entries: raise INPSyntaxError
		entry = entries.popleft()

		# Processing Material Density
		if cell.material:
			if not is_real(entry, lambda f : f != 0): raise INPValueError
			cell.density = float(entry)

			if not entries: raise INPSyntaxError
			entry = entries.popleft()

		# Processing Geometry
		while is_geometry(entry):
			cell.geometry += entry + ' '

			if not entries: break
			entry = entries.popleft()

		if cell.geometry == '': raise INPValueError(entry)
		cell.geometry = cell.geometry[:-1]
		
		# Processing Parameters
		while is_params_key(entry):
			tokens = re.split(r":|=", entry)
			match len(tokens):
				case 2:
					key, value, designator = tokens, None
					if not is_params_item(key, value): raise INPValueError

					if key in cell.parameters: raise INPSyntaxError
					cell.parameters[key] = (designator, value)
				case 3:
					key, designator, value = tokens
					if not is_params_item(key, value): raise INPValueError
					if not is_params_designator(key, designator): raise INPValueError

					if key in cell.parameters:
						cell.parameters[key][designator] = value
					else:
						cell.parameters[key] = {}
						cell.parameters[key][designator] = value
				case _:
					raise INPSyntaxError(card)

			if not entries: break
			entry = entries.popleft()

		# Processing Extra Entries
		if entries: raise INPSyntaxError(entries)
		
		return cell


	@classmethod
	def from_arguments(cls, number: int, material: int, geometry: str, parameters: dict[tuple[str, any]], density: int = None) -> Self:
		"""
		'from_arguments' generates cell card objects from arguments.

		Parameters:
			number (int): Cell card number.
			material (int): Cell card material.
			density (int): Cell card density.
			geometry (str): Cell card geometry.
			parameters (dict[tuple[str, any]]): Cell card parameter table.

		Returns:
			cell (Cell): Call card object.
		"""

		cell = cls()

		# Processing Card Number
		if not (1 < number and number < 99_999_999): raise INPValueError
		cell.number = number
		cell.id = cell.number

		# Processing Mateiral Number
		if not (0 < material and material < 99_999_999): raise INPValueError
		cell.material = material

		# Processing Density
		if not density != 0: raise INPValueError
		cell.density = density

		# Processing Geometry
		for element in geometry.lower():
			if not is_geometry(element): raise INPValueError

		cell.geometry = geometry

		# Processing Parameters
		for key, pair in key.items():
			designator, value = pair

			if designator:
				if not is_params_item(key, value): raise INPValueError
				if not is_params_designator(key, designator): raise INPValueError
			else:
				if not is_params_item(key, value): raise INPValueError

		cell.parameters = parameters

		return cell


	def to_mcnp(self) -> str:
		"""
		'to_mcnp' generates INP from cell card objects.

		Returns:
			source (str): INP for cell card object.
		"""

		# Formatting Density
		density_str = ''

		if self.material:
			density_str = f" {self.density}"

		# Formatting Parameters
		parameters_str = ''
		
		for key, value in self.parameters.items():
			if isinstance(value, dict):
				for designator, val in self.parameters[key].items():
					parameters_str += f"{key}:{designator}={val}"
			else:
				parameters_str += f"{key}={value[1]}"


		return add_continuation_lines(f"{self.number} {self.material}{density_str} {self.geometry} {parameters_str}")


	def to_arguments(self) -> dict:
		"""
		'to_arguments' generates dictionary from cell card objects.

		Returns:
			arguments (dict): Dictionary for cell card object.
		"""

		return {'j': self.number, 'm': self.material, 'd': self.density, 'geom': self.geometry, 'params': self.parameters}

