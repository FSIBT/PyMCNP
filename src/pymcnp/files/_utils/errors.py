"""
``errors`` contains custom exception for the ``files`` subpackage.

MCNP catches syntax and semantic errors in MCNP code, and it throws
custom errors with errors codes. ``errors`` contains the exception
subclasses and error code enumerations.
"""


from enum import Enum


class MCNPSyntaxCodes(Enum):
    """
    ``MCNPSyntaxCodes`` represents ``MCNPSyntaxError`` error codes.

    ``MCNPSyntaxCodes`` enumerates syntax errors, and the enumerations
    categorize syntax errors by MCNP grammar, error type,
    and syntax element. ``KEYWORD`` means missing keyword, ``TOOLONG``
    means too many tokens, and ``TOOSHORT`` means too few tokens.
    """

    KEYWORD_INP_MESSAGE = 0
    TOOFEW_INP = -1
    TOOLONG_INP = 1

    TOOFEW_CELL = -12
    TOOLONG_CELL = 12
    TOOFEW_CELL_GEOMETRY = -10
    TOOLONG_CELL_GEOMETRY = 10
    TOOFEW_CELL_OPTION = -11
    TOOLONG_CELL_OPTION = 11

    KEYWORD_COMMENT_C = 20

    TOOFEW_SURFACE = -30
    TOOLONG_SURFACE = 30
    TOOFEW_SURFACE_ENTRIES = -31
    TOOMANY_SURFACE_ENTRIES = 31

    TOOFEW_DATUM = -40
    TOOLONG_DATUM = 40
    TOOFEW_DATUM_DAWWG_OPTION = -41
    TOOLONG_DATUM_DAWWG_OPTION = 41


class MCNPSemanticCodes(Enum):
    """
    ``MCNPSemanticCodes`` represents ``MCNPSemanticError`` error codes.

    ``MCNPSemanticCodes`` enumerates semantic errors, and the enumerations
    categorize semantic errors by MCNP grammar, error type,
    and syntax element.
    """

    INVALID_MCNP_DESIGNATOR = 0
    INVALID_INP_MESSAGE = 1
    INVALID_INP_TITLE = 2
    INVALID_INP_CELLS = 3
    INVALID_INP_SURFACES = 4
    INVALID_INP_DATA = 5
    INVALID_INP_OTHER = 6

    INVALID_CELL_NUMBER = 10
    INVALID_CELL_MATERIAL = 11
    INVALID_CELL_DENSITY = 12
    INVALID_CELL_GEOMETRY = 13
    INVALID_CELL_PARAMETER = 14
    INVALID_CELL_OPTION = 15
    INVALID_CELL_OPTION_DESIGNATOR = 16
    INVALID_CELL_OPTION_SUFFIX = 17
    INVALID_CELL_OPTION_KEYWORD = 18
    INVALID_CELL_OPTION_VALUE = 19

    INVALID_SURFACE_NUMBER = 20
    INVALID_SURFACE_MNEMONIC = 21
    INVALID_SURFACE_TRANSFORMPERIODIC = 22
    INVALID_SURFACE_PARAMETER = 23

    INVALID_DATUM_MNEMONIC = 30
    INVALID_DATUM_DESIGNATOR = 31
    INVALID_DATUM_SUFFIX = 32
    INVALID_DATUM_PARAMETERS = 33
    INVALID_DATUM_DAWWG_KEYWORD = 34
    INVALID_DATUM_DAWWG_VALUE = 35
    INVALID_DATUM_EMBED_KEYWORD = 36
    INVALID_DATUM_EMBED_VALUE = 37
    INVALID_DATUM_EMBEE_KEYWORD = 38
    INVALID_DATUM_EMBEE_VALUE = 39
    INVALID_DATUM_MATERIAL_KEYWORD = 40
    INVALID_DATUM_MATERIAL_VALUE = 41

    INVALID_COMMENT_CONTENT = 50


class MCNPSyntaxError(Exception):
    """
    ``MCNPSyntaxError`` represents parser generated sytnax errors.

    MCNP raises syntax errors when source code violates MCNP grammar,
    notably when sytnax elements are too long or too short.

    Attributes:
        code: Error code.
        line: Line number of error.
    """

    def __init__(self, code: MCNPSyntaxCodes, line: int = None):
        """
        ``__init__`` initializes ``MCNPSyntaxError``

        Parameters:
            code: Error code.
            line: Line number.
        """

        self.code: MCNPSyntaxCodes = code
        self.line: int = line

    def __str__(self) -> str:
        """
        ``__str__`` stringifies ``MCNPSyntaxError``.
        """

        match self.code:
            case MCNPSyntaxCodes.KEYWORD_INP_MESSAGE:
                return "Missing `message:` keyword in INP message block."
            case MCNPSyntaxCodes.TOOFEW_INP:
                return ""
            case MCNPSyntaxCodes.TOOLONG_INP:
                return ""
            case MCNPSyntaxCodes.TOOFEW_CELL:
                return ""
            case MCNPSyntaxCodes.TOOLONG_CELL:
                return ""
            case MCNPSyntaxCodes.TOOFEW_CELL_GEOMETRY:
                return ""
            case MCNPSyntaxCodes.TOOLONG_CELL_GEOMETRY:
                return ""
            case MCNPSyntaxCodes.TOOFEW_CELL_OPTION:
                return ""
            case MCNPSyntaxCodes.TOOLONG_CELL_OPTION:
                return ""
            case MCNPSyntaxCodes.KEYWORD_COMMENT_C:
                return "Missing `c ` keyword in INP comment."
            case MCNPSyntaxCodes.TOOFEW_SURFACE:
                return ""
            case MCNPSyntaxCodes.TOOLONG_SURFACE:
                return ""
            case MCNPSyntaxCodes.TOOFEW_SURFACE_ENTRIES:
                return ""
            case MCNPSyntaxCodes.TOOMANY_SURFACE_ENTRIES:
                return ""
            case MCNPSyntaxCodes.TOOFEW_DATUM:
                return ""
            case MCNPSyntaxCodes.TOOLONG_DATUM:
                return ""
            case MCNPSyntaxCodes.TOOFEW_DATUM_DAWWG_OPTION:
                return ""
            case MCNPSyntaxCodes.TOOLONG_DATUM_DAWWG_OPTION:
                return ""


class MCNPSemanticError(Exception):
    """
    ``MCNPSemanticError`` represents parser generated semantic errors.

    MCNP raises semantic errors when source code violates MCNP
    restrictions. MCNP handles value errors and type errors as
    semantic errros.

    Attributes:
        code: Error code.
        line: Line number of error.
    """

    def __init__(self, code: MCNPSemanticCodes, line: int = None):
        """
        ``__init__`` initializes ``MCNPSemanticError``

        Parameters:
            code: Error code.
            line: Line number.
        """

        self.code: MCNPSemanticCodes = code
        self.line: int = line

    def __str__(self) -> str:
        match self.code:
            case MCNPSemanticCodes.INVALID_MCNP_DESIGNATOR:
                return ""
            case MCNPSemanticCodes.INVALID_INP_MESSAGE:
                return ""
            case MCNPSemanticCodes.INVALID_INP_TITLE:
                return ""
            case MCNPSemanticCodes.INVALID_INP_CELLS:
                return ""
            case MCNPSemanticCodes.INVALID_INP_SURFACES:
                return ""
            case MCNPSemanticCodes.INVALID_INP_DATA:
                return ""
            case MCNPSemanticCodes.INVALID_INP_OTHER:
                return ""
            case MCNPSemanticCodes.INVALID_CELL_NUMBER:
                return ""
            case MCNPSemanticCodes.INVALID_CELL_MATERIAL:
                return ""
            case MCNPSemanticCodes.INVALID_CELL_DENSITY:
                return ""
            case MCNPSemanticCodes.INVALID_CELL_GEOMETRY:
                return ""
            case MCNPSemanticCodes.INVALID_CELL_PARAMETER:
                return ""
            case MCNPSemanticCodes.INVALID_CELL_OPTION:
                return ""
            case MCNPSemanticCodes.INVALID_CELL_OPTION_DESIGNATOR:
                return ""
            case MCNPSemanticCodes.INVALID_CELL_OPTION_SUFFIX:
                return ""
            case MCNPSemanticCodes.INVALID_CELL_OPTION_KEYWORD:
                return ""
            case MCNPSemanticCodes.INVALID_CELL_OPTION_VALUE:
                return ""
            case MCNPSemanticCodes.INVALID_SURFACE_NUMBER:
                return ""
            case MCNPSemanticCodes.INVALID_SURFACE_MNEMONIC:
                return ""
            case MCNPSemanticCodes.INVALID_SURFACE_TRANSFORMPERIODIC:
                return ""
            case MCNPSemanticCodes.INVALID_SURFACE_PARAMETER:
                return ""
            case MCNPSemanticCodes.INVALID_DATUM_MNEMONIC:
                return ""
            case MCNPSemanticCodes.INVALID_DATUM_DESIGNATOR:
                return ""
            case MCNPSemanticCodes.INVALID_DATUM_SUFFIX:
                return ""
            case MCNPSemanticCodes.INVALID_DATUM_PARAMETERS:
                return ""
            case MCNPSemanticCodes.INVALID_DATUM_DAWWG_KEYWORD:
                return ""
            case MCNPSemanticCodes.INVALID_DATUM_DAWWG_VALUE:
                return ""
            case MCNPSemanticCodes.INVALID_DATUM_EMBED_KEYWORD:
                return ""
            case MCNPSemanticCodes.INVALID_DATUM_EMBED_VALUE:
                return ""
            case MCNPSemanticCodes.INVALID_DATUM_EMBEE_KEYWORD:
                return ""
            case MCNPSemanticCodes.INVALID_DATUM_EMBEE_VALUE:
                return ""
            case MCNPSemanticCodes.INVALID_DATUM_MATERIAL_KEYWORD:
                return ""
            case MCNPSemanticCodes.INVALID_DATUM_MATERIAL_VALUE:
                return ""
            case MCNPSemanticCodes.INVALID_COMMENT_CONTENT:
                return ""
