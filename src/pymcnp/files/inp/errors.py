"""
'errors' contains custom exception for the 'inp' module.

Classes:
	INPSyntaxError: Exception for INP syntax issues.
	INPValueError: Exception for INP value issues.
"""


from enum import Enum


class INPSyntaxError(Exception):

	class Codes(Enum):
		INCOMPLETE_CELL_PARAMETER = 0
		EXCESSIVE_CELL_PARAMTER = 1
		INCOPMLETE_SURFACE_LIST = 2

	
	def __init__(self, code: Codes):
		self.code = code


class INPValueError(Exception):

	class Codes(Enum):
		INVALID_CELL_NUMBER = 0
		INVALID_CELL_MATERIAL = 1
		INVALID_CELL_DENSITY = 2
		INVALID_CELL_GEOMETRY = 3
		INVALID_CELL_PARAMETER_KEYWORD = 4
		INVALID_CELL_PARAMETER_DESIGNATOR = 5

		INVALID_INP_TITLE = 6

		INVALID_SURFACE_PARAMETER = 7

	def __init__(self, code: Codes):
		self.code = code


class INPEOFError(Exception):

	def __init__(self):
		pass

