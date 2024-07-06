"""
'errors' contains custom exception for the 'inp' module.

Classes:
	INPSyntaxError: Exception for INP syntax issues.
	INPValueError: Exception for INP value issues.
"""


class INPSyntaxError(Exception):
	
	def __init__(self, value):
		self.value = value


class INPValueError(Exception):

	def __init__(self, value):
		self.value = value

