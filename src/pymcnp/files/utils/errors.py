"""
``errors`` contains custom exception for the ``files`` subpackage.

PyMCNP catches syntax and semantic errors in PyMCNP code, and it throws
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
    TOOFEW_SURFACE = -20
    TOOLONG_SURFACE = 20
    TOOFEW_SURFACE_ENTRIES = -21
    TOOMANY_SURFACE_ENTRIES = 21
    TOOFEW_DATUM = -30
    TOOLONG_DATUM = 30
    TOOFEW_DATUM_URAN = -31
    TOOLONG_DATUM_URAN = 31
    TOOFEW_DATUM_DAWWG = -32
    TOOLONG_DATUM_DAWWG = 32
    TOOFEW_DATUM_EMBED = -33
    TOOLONG_DATUM_EMBED = 33
    TOOFEW_DATUM_EMBEE = -34
    TOOLONG_DATUM_EMBEE = 34
    TOOFEW_DATUM_MATERIAL = -35
    TOOLONG_DATUM_MATERIAL = 35
    TOOFEW_DATUM_WEIGHT = -36
    TOOLONG_DATUM_WEIGHT = 36
    TOOFEW_DATUM_ACTIVATION = -37
    TOOLONG_DATUM_ACTIVATION = 37
    TOOFEW_DATUM_SOURCE = -38
    TOOLONG_DATUM_SOURCE = 38

    KEYWORD_DATUM_TOTNU_NO = 41
    KEYWORD_COMMENT_C = 50

    KEYWORD_HEADER_MINUS1 = 100
    TOOFEW_HEADER = -101
    TOOMANY_HEADER = 101
    TOOFEW_EVENT = -102
    TOOLONG_EVENT = 102
    TOFEW_HISTORY = -103
    TOLONG_HISTORY = 103

    TOOFEW_ZAID = -200
    TOOLONG_ZAID = 200


class MCNPSemanticCodes(Enum):
    """
    ``MCNPSemanticCodes`` represents ``MCNPSemanticError`` error codes.

    ``MCNPSemanticCodes`` enumerates semantic errors, and the enumerations
    categorize semantic errors by MCNP grammar, error type,
    and syntax element.
    """

    INVALID_MCNP_INTEGER = 200
    INVALID_MCNP_REAL = 201
    INVALID_MCNP_DESIGNATOR = 210
    INVALID_MCNP_ZAID = 220
    INVALID_ZAID_Z = 221
    INVALID_ZAID_A = 222
    INVALID_ZAID_ABX = 223

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
    INVALID_CELL_OPTION = 14
    INVALID_CELL_OPTION_DESIGNATOR = 15
    INVALID_CELL_OPTION_SUFFIX = 16
    INVALID_CELL_OPTION_KEYWORD = 17
    INVALID_CELL_OPTION_VALUE = 18
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
    INVALID_DATUM_ACTIVATION_KEYWORD = 42
    INVALID_DATUM_ACTIVATION_VALUE = 43
    INVALID_DATUM_SOURCE_KEYWORD = 44
    INVALID_DATUM_SOURCE_VALUE = 45

    INVALID_COMMENT_CONTENT = 90

    INVALID_HEADER_CODE = 100
    INVALID_HEADER_CODEDATE = 101
    INVALID_HEADER_VERSION = 102
    INVALID_HEADER_RUNDATE = 103
    INVALID_HEADER_RUNTIME = 104
    INVALID_HEADER_TITLE = 105
    INVALID_HEADER_SETTINGS = 106
    INVALID_HEADER_NUMBERS = 107
    INVALID_EVENT_TYPE = 110
    INVALID_EVENT_NTER = 111
    INVALID_EVENT_NODE = 112
    INVALID_EVENT_NSR = 113
    INVALID_EVENT_NXS = 114
    INVALID_EVENT_NTYNMTP = 115
    INVALID_EVENT_NSF = 116
    INVALID_EVENT_ANGLE = 117
    INVALID_EVENT_BRANCH = 119
    INVALID_EVENT_IPT = 119
    INVALID_EVENT_NCL = 120
    INVALID_EVENT_MAT = 121
    INVALID_EVENT_NCP = 122
    INVALID_EVENT_XXX = 123
    INVALID_EVENT_YYY = 124
    INVALID_EVENT_ZZZ = 125
    INVALID_EVENT_UUU = 126
    INVALID_EVENT_VVV = 127
    INVALID_EVENT_WWW = 128
    INVALID_EVENT_ERG = 129
    INVALID_EVENT_WGT = 130
    INVALID_EVENT_TME = 131
    INVALID_HISTORY_NPS = 140
    INVALID_HISTORY_NCL = 141
    INVALID_HISTORY_NSF = 142
    INVALID_HISTORY_JPTAL = 143
    INVALID_HISTORY_TAL = 144
    INVALID_HISTORY_NEXTTYPE = 145


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
                return f"Missing `message:` keyword in INP message block, line {self.line}."
            case MCNPSyntaxCodes.TOOFEW_INP:
                return f"Incomplete INP file, line {self.line}."
            case MCNPSyntaxCodes.TOOLONG_INP:
                return f"Unexpected tokens in INP file, line {self.line}."
            case MCNPSyntaxCodes.TOOFEW_CELL:
                return f"Incomplete INP cell card, line {self.line}."
            case MCNPSyntaxCodes.TOOLONG_CELL:
                return f"Unexpected tokens in INP cell card, line {self.line}."
            case MCNPSyntaxCodes.TOOFEW_CELL_GEOMETRY:
                return f"Incomplete INP cell card geometry, line {self.line}."
            case MCNPSyntaxCodes.TOOLONG_CELL_GEOMETRY:
                return f"Unexpected tokens in INP cell card geometry, line {self.line}."
            case MCNPSyntaxCodes.TOOFEW_CELL_OPTION:
                return f"Incomplete INP cell card option, line {self.line}."
            case MCNPSyntaxCodes.TOOLONG_CELL_OPTION:
                return f"Unexpected tokens in INP cell card option, line {self.line}."
            case MCNPSyntaxCodes.TOOFEW_SURFACE:
                return f"Incomplete INP surface car, line {self.line}."
            case MCNPSyntaxCodes.TOOLONG_SURFACE:
                return f"Unexpected tokens in INP surface car, line {self.line}."
            case MCNPSyntaxCodes.TOOFEW_SURFACE_ENTRIES:
                return f"Incomplete INP surface card entries, line {self.line}."
            case MCNPSyntaxCodes.TOOMANY_SURFACE_ENTRIES:
                return f"Unexpected tokens in INP surface card entries, line {self.line}."
            case MCNPSyntaxCodes.TOOFEW_DATUM:
                return f"Incomplete INP data card, line {self.line}."
            case MCNPSyntaxCodes.TOOLONG_DATUM:
                return f"Unexpected tokens in INP data card, line {self.line}."
            case MCNPSyntaxCodes.TOOFEW_DATUM_URAN:
                return f"Incomplete INP URAN card, line {self.line}."
            case MCNPSyntaxCodes.TOOLONG_DATUM_URAN:
                return f"Unexpected tokens in INP URAN card, line {self.line}."
            case MCNPSyntaxCodes.TOOFEW_DATUM_DAWWG:
                return f"Incomplete INP DAWWG card, line {self.line}."
            case MCNPSyntaxCodes.TOOLONG_DATUM_DAWWG:
                return f"Unexpected tokens in INP DAWWG card, line {self.line}."
            case MCNPSyntaxCodes.TOOFEW_DATUM_EMBED:
                return f"Incomplete INP EMBED card, line {self.line}."
            case MCNPSyntaxCodes.TOOLONG_DATUM_EMBED:
                return f"Unexpected tokens in INP EMBED card, line {self.line}."
            case MCNPSyntaxCodes.TOOFEW_DATUM_EMBEE:
                return f"Incomplete INP EMBEE card, line {self.line}."
            case MCNPSyntaxCodes.TOOLONG_DATUM_EMBEE:
                return f"Unexpected tokens in INP EMBEE card, line {self.line}."
            case MCNPSyntaxCodes.TOOFEW_DATUM_MATERIAL:
                return f"Incomplete INP material data card, line {self.line}."
            case MCNPSyntaxCodes.TOOLONG_DATUM_MATERIAL:
                return f"Unexpected tokens in INP material data card, line {self.line}."
            case MCNPSyntaxCodes.TOOFEW_DATUM_WEIGHT:
                return f"Incomplete INP atomic weight data card, line {self.line}."
            case MCNPSyntaxCodes.TOOLONG_DATUM_WEIGHT:
                return f"Unexpected tokens in INP atomic weight data card, line {self.line}."
            case MCNPSyntaxCodes.KEYWORD_COMMENT_C:
                return f"Missing `c ` keyword in INP comment, line {self.line}."
            case MCNPSyntaxCodes.KEYWORD_HEADER_MINUS1:
                return f"Missing `=1` keyword in PTRAC header, line {self.line}."
            case MCNPSyntaxCodes.TOOFEW_HEADER:
                return f"Incomplete PTRAC header, line {self.line}."
            case MCNPSyntaxCodes.TOOMANY_HEADER:
                return f"Unexpected tokens in PTRAC header, line {self.line}."
            case MCNPSyntaxCodes.TOOFEW_EVENT:
                return f"Incomplete PTRAC event, line {self.line}."
            case MCNPSyntaxCodes.TOOLONG_EVENT:
                return f"Unexpected tokens in PTRAC event, line {self.line}."
            case MCNPSyntaxCodes.TOFEW_HISTORY:
                return f"Incomplete PTRAC history, line {self.line}."
            case MCNPSyntaxCodes.TOLONG_HISTORY:
                return f"Unexpected tokens in PTRAC history, line {self.line}."


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
            case MCNPSemanticCodes.INVALID_INP_MESSAGE:
                return f"Invalid INP message, line {self.line}."
            case MCNPSemanticCodes.INVALID_INP_TITLE:
                return f"Invalid INP title, line {self.line}."
            case MCNPSemanticCodes.INVALID_INP_CELLS:
                return f"Invalid INP cell card block, line {self.line}."
            case MCNPSemanticCodes.INVALID_INP_SURFACES:
                return f"Invalid INP surface card block, line {self.line}."
            case MCNPSemanticCodes.INVALID_INP_DATA:
                return f"Invalid INP data card block, line {self.line}."
            case MCNPSemanticCodes.INVALID_INP_OTHER:
                return f"Invalid INP other block, line {self.line}."
            case MCNPSemanticCodes.INVALID_CELL_NUMBER:
                return f"Invalid INP cell number, line {self.line}."
            case MCNPSemanticCodes.INVALID_CELL_MATERIAL:
                return f"Invalid INP cell material, line {self.line}."
            case MCNPSemanticCodes.INVALID_CELL_DENSITY:
                return f"Invalid INP cell density, line {self.line}."
            case MCNPSemanticCodes.INVALID_CELL_GEOMETRY:
                return f"Invalid INP cell geometry, line {self.line}."
            case MCNPSemanticCodes.INVALID_CELL_OPTION:
                return f"Invalid INP cell option, line {self.line}."
            case MCNPSemanticCodes.INVALID_CELL_OPTION_DESIGNATOR:
                return f"Invalid INP cell option designator, line {self.line}."
            case MCNPSemanticCodes.INVALID_CELL_OPTION_SUFFIX:
                return f"Invalid INP cell option suffix, line {self.line}."
            case MCNPSemanticCodes.INVALID_CELL_OPTION_KEYWORD:
                return f"Invalid INP cell option keyword, line {self.line}."
            case MCNPSemanticCodes.INVALID_CELL_OPTION_VALUE:
                return f"Invalid INP cell option value, line {self.line}."
            case MCNPSemanticCodes.INVALID_SURFACE_NUMBER:
                return f"Invalid INP surface name, line {self.line}."
            case MCNPSemanticCodes.INVALID_SURFACE_MNEMONIC:
                return f"Invalid INP surface mnemonic, line {self.line}."
            case MCNPSemanticCodes.INVALID_SURFACE_TRANSFORMPERIODIC:
                return f"Invalid INP surface transform/periodic number, line {self.line}."
            case MCNPSemanticCodes.INVALID_SURFACE_PARAMETER:
                return f"Invalid INP surface parameter, line {self.line}."
            case MCNPSemanticCodes.INVALID_DATUM_MNEMONIC:
                return f"Invalid INP data card mnemonic, line {self.line}."
            case MCNPSemanticCodes.INVALID_DATUM_DESIGNATOR:
                return f"Invalid INP data card designator, line {self.line}."
            case MCNPSemanticCodes.INVALID_DATUM_SUFFIX:
                return f"Invalid INP data card suffix, line {self.line}."
            case MCNPSemanticCodes.INVALID_DATUM_PARAMETERS:
                return f"Invalid INP data card parameter, line {self.line}."
            case MCNPSemanticCodes.INVALID_DATUM_DAWWG_KEYWORD:
                return f"Invalid INP data card DAWWG keyword, line {self.line}."
            case MCNPSemanticCodes.INVALID_DATUM_DAWWG_VALUE:
                return f"Invalid INP data card DAWWG value, line {self.line}."
            case MCNPSemanticCodes.INVALID_DATUM_EMBED_KEYWORD:
                return f"Invalid INP data card EMBED keyword, line {self.line}."
            case MCNPSemanticCodes.INVALID_DATUM_EMBED_VALUE:
                return f"Invalid INP data card EMBED value, line {self.line}."
            case MCNPSemanticCodes.INVALID_DATUM_EMBEE_KEYWORD:
                return f"Invalid INP data card EMBEE keyword, line {self.line}."
            case MCNPSemanticCodes.INVALID_DATUM_EMBEE_VALUE:
                return f"Invalid INP data card EMBEE value, line {self.line}."
            case MCNPSemanticCodes.INVALID_DATUM_MATERIAL_KEYWORD:
                return f"Invalid INP data card material keyword, line {self.line}."
            case MCNPSemanticCodes.INVALID_DATUM_MATERIAL_VALUE:
                return f"Invalid INP data card meterial value, line {self.line}."
            case MCNPSemanticCodes.INVALID_COMMENT_CONTENT:
                return f"Invalid INP comment content, line {self.line}."
            case MCNPSemanticCodes.INVALID_HEADER_CODE:
                return f"Invalid PTRAC header code, line {self.line}."
            case MCNPSemanticCodes.INVALID_HEADER_CODEDATE:
                return f"Invalid PTRAC header code date, line {self.line}."
            case MCNPSemanticCodes.INVALID_HEADER_VERSION:
                return f"Invalid PTRAC header version, line {self.line}."
            case MCNPSemanticCodes.INVALID_HEADER_RUNDATE:
                return f"Invalid PTRAC header run date, line {self.line}."
            case MCNPSemanticCodes.INVALID_HEADER_RUNTIME:
                return f"Invalid PTRAC header run time, line {self.line}."
            case MCNPSemanticCodes.INVALID_HEADER_TITLE:
                return f"Invalid PTRAC header title, line {self.line}."
            case MCNPSemanticCodes.INVALID_HEADER_SETTINGS:
                return f"Invalid PTRAC header settings, line {self.line}."
            case MCNPSemanticCodes.INVALID_HEADER_NUMBERS:
                return f"Invalid PTRAC header numbers, line {self.line}."
            case MCNPSemanticCodes.INVALID_EVENT_TYPE:
                return f"Invalid PTRAC event type variable, line {self.line}."
            case MCNPSemanticCodes.INVALID_EVENT_NTER:
                return f"Invalid PTRAC event nter variable, line {self.line}."
            case MCNPSemanticCodes.INVALID_EVENT_NODE:
                return f"Invalid PTRAC event node variable, line {self.line}."
            case MCNPSemanticCodes.INVALID_EVENT_NSR:
                return f"Invalid PTRAC event nsr variable, line {self.line}."
            case MCNPSemanticCodes.INVALID_EVENT_NXS:
                return f"Invalid PTRAC event nxs variable, line {self.line}."
            case MCNPSemanticCodes.INVALID_EVENT_NTYNMTP:
                return f"Invalid PTRAC event ntynmtp variable, line {self.line}."
            case MCNPSemanticCodes.INVALID_EVENT_NSF:
                return f"Invalid PTRAC event nsf variable, line {self.line}."
            case MCNPSemanticCodes.INVALID_EVENT_ANGLE:
                return f"Invalid PTRAC event angle variable, line {self.line}."
            case MCNPSemanticCodes.INVALID_EVENT_NTER:
                return f"Invalid PTRAC event nter variable, line {self.line}."
            case MCNPSemanticCodes.INVALID_EVENT_BRANCH:
                return f"Invalid PTRAC event branch variable, line {self.line}."
            case MCNPSemanticCodes.INVALID_EVENT_IPT:
                return f"Invalid PTRAC event ipt variable, line {self.line}."
            case MCNPSemanticCodes.INVALID_EVENT_NCL:
                return f"Invalid PTRAC event ncl variable, line {self.line}."
            case MCNPSemanticCodes.INVALID_EVENT_MAT:
                return f"Invalid PTRAC event mat variable, line {self.line}."
            case MCNPSemanticCodes.INVALID_EVENT_NCP:
                return f"Invalid PTRAC event ncp variable, line {self.line}."
            case MCNPSemanticCodes.INVALID_EVENT_XXX:
                return f"Invalid PTRAC event xxx variable, line {self.line}."
            case MCNPSemanticCodes.INVALID_EVENT_YYY:
                return f"Invalid PTRAC event yyy variable, line {self.line}."
            case MCNPSemanticCodes.INVALID_EVENT_ZZZ:
                return f"Invalid PTRAC event zzz variable, line {self.line}."
            case MCNPSemanticCodes.INVALID_EVENT_UUU:
                return f"Invalid PTRAC event uuu variable, line {self.line}."
            case MCNPSemanticCodes.INVALID_EVENT_VVV:
                return f"Invalid PTRAC event vvv variable, line {self.line}."
            case MCNPSemanticCodes.INVALID_EVENT_WWW:
                return f"Invalid PTRAC event www variable, line {self.line}."
            case MCNPSemanticCodes.INVALID_EVENT_ERG:
                return f"Invalid PTRAC event erg variable, line {self.line}."
            case MCNPSemanticCodes.INVALID_EVENT_WGT:
                return f"Invalid PTRAC event wgt variable, line {self.line}."
            case MCNPSemanticCodes.INVALID_EVENT_TME:
                return f"Invalid PTRAC event tme variable, line {self.line}."
            case MCNPSemanticCodes.INVALID_EVENT_NSR:
                return f"Invalid PTRAC event nsr variable, line {self.line}."
            case MCNPSemanticCodes.INVALID_HISTORY_NPS:
                return f"Invalid PTRAC history nps, line {self.line}."
            case MCNPSemanticCodes.INVALID_HISTORY_NCL:
                return f"Invalid PTRAC history ncl, line {self.line}."
            case MCNPSemanticCodes.INVALID_HISTORY_NSF:
                return f"Invalid PTRAC history nsf, line {self.line}."
            case MCNPSemanticCodes.INVALID_HISTORY_JPTAL:
                return f"Invalid PTRAC history jptal, line {self.line}."
            case MCNPSemanticCodes.INVALID_HISTORY_TAL:
                return f"Invalid PTRAC history tal, line {self.line}."
            case MCNPSemanticCodes.INVALID_HISTORY_NEXTTYPE:
                return f"Invalid PTRAC history event type, line {self.line}."
