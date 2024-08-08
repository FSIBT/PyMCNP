"""
'_errors' contains custom exception for the 'files' subpackage.

MCNP catches syntax and semantic errors in MCNP code, and it throws
custom errors with errors codes. '_errors' contains the exception
subclasses and error code enumerations.
"""

from typing import *
from enum import Enum


class MCNPSyntaxCodes(Enum):
	"""
	'MCNPSyntaxCodes' represents 'MCNPSyntaxError' error codes.

	'MCNPSyntaxCodes' enumerates syntax errors, and the enumerations
	categorize syntax errors by MCNP grammar, error type,
	and syntax element. 'KEYWORD' means missing keyword, 'TOOLONG'
	means too many tokens, and 'TOOSHORT' means too few tokens.
	"""

	# INP
	KEYWORD_INP_MESSAGE = 0

	# CELL
	TOOFEW_CELL_GEOMETRY = -1
	TOOLONG_CELL_GEOMETRY = 1


class MCNPSemanticCodes(Enum):
	"""
	'MCNPSemanticCodes' represents 'MCNPSemanticError' error codes.

	'MCNPSemanticCodes' enumerates semantic errors, and the enumerations
	categorize semantic errors by MCNP grammar, error type,
	and syntax element.
	"""

	# INP
	INVALID_INP_TITLE = 0


class MCNPSyntaxError(Exception):
	"""
	'MCNPSyntaxError' represents parser generated sytnax errors.

	MCNP raises syntax errors when source code violates MCNP grammar, 
	notably when sytnax elements are too long or too short.

	Attributes:
		code: Error code.
		line: Line number of error.
	"""


	def __init__(self, code: MCNPSyntaxCodes, line: int = None) -> Self:
		"""
		'__init__' initializes 'MCNPSyntaxError'

		Parameters:
			code: Error code.
			line: Line number.
		"""

		self.code: Codes = code
		self.line: int = line


class MCNPSemanticError(Exception):
	"""
	'MCNPSemanticError' represents parser generated semantic errors.

	MCNP raises semantic errors when source code violates MCNP
	restrictions. MCNP handles value errors and type errors as
	semantic errros.

	Attributes:
		code: Error code.
		line: Line number of error.
	"""


	def __init__(self, code: MCNPSemanticCodes, line: int = None):
		"""
		'__init__' initializes 'MCNPSemanticError'

		Parameters:
			code: Error code.
			line: Line number.
		"""

		self.code: Codes = code
		self.line: int = line

