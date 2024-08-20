"""
'_errors' contains custom exception for the 'files' subpackage.

MCNP catches syntax and semantic errors in MCNP code, and it throws
custom errors with errors codes. '_errors' contains the exception
subclasses and error code enumerations.
"""

from typing import Self
from enum import Enum


class MCNPSyntaxCodes(Enum):
    """
    'MCNPSyntaxCodes' represents 'MCNPSyntaxError' error codes.

    'MCNPSyntaxCodes' enumerates syntax errors, and the enumerations
    categorize syntax errors by MCNP grammar, error type,
    and syntax element. 'KEYWORD' means missing keyword, 'TOOLONG'
    means too many tokens, and 'TOOSHORT' means too few tokens.
    """

    KEYWORD_INP_MESSAGE = 0
    TOOFEW_INP = -1
    TOOLONG_INP = 1

    TOOFEW_CELL_GEOMETRY = -10
    TOOLONG_CELL_GEOMETRY = 10
    TOOFEW_CELL_PARAMETERS = -11
    TOOLONG_CELL_PARAMETERS = 11
    TOOFEW_CELL = -12
    TOOLONG_CELL = 12

    KEYWORD_COMMENT_C = 20

    TOOFEW_SURFACE_ENTRIES = -30
    TOOMANY_SURFACE_ENTRIES = 30

    TOOFEW_DATUM_ENTRIES = -40
    TOOMANY_DATUM_ENTRIES = 40


class MCNPSemanticCodes(Enum):
    """
    'MCNPSemanticCodes' represents 'MCNPSemanticError' error codes.

    'MCNPSemanticCodes' enumerates semantic errors, and the enumerations
    categorize semantic errors by MCNP grammar, error type,
    and syntax element.
    """

    INVALID_MCNP_DESIGNATOR = 0
    INVALID_INP_TITLE = 1

    INVALID_PARAMETER_KEYWORD = 2
    INVALID_PARAMETER_SUFFIX = 3
    INVALID_PARAMETER_VALUE = 4

    INVALID_CELL_NUMBER = 5
    INVALID_CELL_MATERIAL = 6
    INVALID_CELL_DENSITY = 7
    INVALID_CELL_GEOMETRY = 8
    INVALID_CELL_PARAMETERS = 9

    INVALID_SURFACE_NUMBER = 10
    INVALID_SURFACE_MNEMONIC = 11
    INVALID_SURFACE_TRANSFORMPERIODIC = 12
    INVALID_SURFACE_PARAMETER = 13

    INVALID_DATUM_MNEMONIC = 20
    INVALID_DATUM_PARAMETER = 21
    INVALID_DATUM_SUFFIX = 22
    INVALID_DAWWG_KEYWORD = 23
    INVALID_DAWWG_VALUE = 24
    INVALID_EMBED_KEYWORD = 25
    INVALID_EMBED_VALUE = 26
    INVALID_MATERIAL_KEYWORD = 27
    INVALID_MATERIAL_VALUE = 28


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

        self.code: MCNPSyntaxCodes = code
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

    def __init__(self, code: MCNPSemanticCodes, line: int = None) -> Self:
        """
        '__init__' initializes 'MCNPSemanticError'

        Parameters:
            code: Error code.
            line: Line number.
        """

        self.code: MCNPSemanticCodes = code
        self.line: int = line
