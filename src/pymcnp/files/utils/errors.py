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
    TOOFEW_DATUM_RAND = -39
    TOOLONG_DATUM_RAND = 39

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
    INVALID_DN = 224

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
    INVALID_DATUM_RAND_KEYWORD = 46
    INVALID_DATUM_RAND_VALUE = 47

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
                return 'Missing `message:` keyword in INP message block.'
            case MCNPSyntaxCodes.TOOFEW_INP:
                return 'Incomplete INP file.'
            case MCNPSyntaxCodes.TOOLONG_INP:
                return 'Unexpected tokens in INP file.'
            case MCNPSyntaxCodes.TOOFEW_CELL:
                return 'Incomplete INP cell card.'
            case MCNPSyntaxCodes.TOOLONG_CELL:
                return 'Unexpected tokens in INP cell card.'
            case MCNPSyntaxCodes.TOOFEW_CELL_GEOMETRY:
                return 'Incomplete INP cell card geometry.'
            case MCNPSyntaxCodes.TOOLONG_CELL_GEOMETRY:
                return 'Unexpected tokens in INP cell card geometry.'
            case MCNPSyntaxCodes.TOOFEW_CELL_OPTION:
                return 'Incomplete INP cell card option.'
            case MCNPSyntaxCodes.TOOLONG_CELL_OPTION:
                return 'Unexpected tokens in INP cell card option.'
            case MCNPSyntaxCodes.TOOFEW_SURFACE:
                return 'Incomplete INP surface car.'
            case MCNPSyntaxCodes.TOOLONG_SURFACE:
                return 'Unexpected tokens in INP surface car.'
            case MCNPSyntaxCodes.TOOFEW_SURFACE_ENTRIES:
                return 'Incomplete INP surface card entries.'
            case MCNPSyntaxCodes.TOOMANY_SURFACE_ENTRIES:
                return 'Unexpected tokens in INP surface card entries.'
            case MCNPSyntaxCodes.TOOFEW_DATUM:
                return 'Incomplete INP data card.'
            case MCNPSyntaxCodes.TOOLONG_DATUM:
                return 'Unexpected tokens in INP data card.'
            case MCNPSyntaxCodes.TOOFEW_DATUM_URAN:
                return 'Incomplete INP URAN card.'
            case MCNPSyntaxCodes.TOOLONG_DATUM_URAN:
                return 'Unexpected tokens in INP URAN card.'
            case MCNPSyntaxCodes.TOOFEW_DATUM_DAWWG:
                return 'Incomplete INP DAWWG card.'
            case MCNPSyntaxCodes.TOOLONG_DATUM_DAWWG:
                return 'Unexpected tokens in INP DAWWG card.'
            case MCNPSyntaxCodes.TOOFEW_DATUM_EMBED:
                return 'Incomplete INP EMBED card.'
            case MCNPSyntaxCodes.TOOLONG_DATUM_EMBED:
                return 'Unexpected tokens in INP EMBED card.'
            case MCNPSyntaxCodes.TOOFEW_DATUM_EMBEE:
                return 'Incomplete INP EMBEE card.'
            case MCNPSyntaxCodes.TOOLONG_DATUM_EMBEE:
                return 'Unexpected tokens in INP EMBEE card.'
            case MCNPSyntaxCodes.TOOFEW_DATUM_MATERIAL:
                return 'Incomplete INP material data card.'
            case MCNPSyntaxCodes.TOOLONG_DATUM_MATERIAL:
                return 'Unexpected tokens in INP material data card.'
            case MCNPSyntaxCodes.TOOFEW_DATUM_WEIGHT:
                return 'Incomplete INP atomic weight data card.'
            case MCNPSyntaxCodes.TOOLONG_DATUM_WEIGHT:
                return 'Unexpected tokens in INP atomic weight data card.'
            case MCNPSyntaxCodes.KEYWORD_COMMENT_C:
                return 'Missing `c ` keyword in INP comment.'
            case MCNPSyntaxCodes.KEYWORD_HEADER_MINUS1:
                return 'Missing `=1` keyword in PTRAC header.'
            case MCNPSyntaxCodes.TOOFEW_HEADER:
                return 'Incomplete PTRAC header.'
            case MCNPSyntaxCodes.TOOMANY_HEADER:
                return 'Unexpected tokens in PTRAC header.'
            case MCNPSyntaxCodes.TOOFEW_EVENT:
                return 'Incomplete PTRAC event.'
            case MCNPSyntaxCodes.TOOLONG_EVENT:
                return 'Unexpected tokens in PTRAC event.'
            case MCNPSyntaxCodes.TOFEW_HISTORY:
                return 'Incomplete PTRAC history.'
            case MCNPSyntaxCodes.TOLONG_HISTORY:
                return 'Unexpected tokens in PTRAC history.'


class MCNPSemanticError(Exception):
    """
    ``MCNPSemanticError`` represents parser generated semantic errors.

    MCNP raises semantic errors when source code violates MCNP
    restrictions. MCNP handles value errors and type errors as
    semantic errros.

    Attributes:
        code: Error code.
        line: Line number of error.
        info: Error info.
    """

    def __init__(self, code: MCNPSemanticCodes, line: int = None, info: str = ''):
        """
        ``__init__`` initializes ``MCNPSemanticError``

        Parameters:
            code: Error code.
            line: Line number.
            info: Error info.
        """

        self.code: MCNPSemanticCodes = code
        self.line: int = line
        self.info: str = info

    def __str__(self) -> str:
        match self.code:
            case MCNPSemanticCodes.INVALID_MCNP_INTEGER:
                return f'Invalid Integer: {self.info}.'
            case MCNPSemanticCodes.INVALID_MCNP_REAL:
                return f'Invalid Real: {self.info}.'
            case MCNPSemanticCodes.INVALID_MCNP_DESIGNATOR:
                return f'Invalid Designator: {self.info}.'
            case MCNPSemanticCodes.INVALID_MCNP_ZAID:
                return f'Invalid Zaid: {self.info}.'
            case MCNPSemanticCodes.INVALID_ZAID_Z:
                return f'Invalid ZZZ: {self.info}.'
            case MCNPSemanticCodes.INVALID_ZAID_A:
                return f'Invalid AAA: {self.info}.'
            case MCNPSemanticCodes.INVALID_ZAID_ABX:
                return f'Invalid ABX: {self.info}.'
            case MCNPSemanticCodes.INVALID_DN:
                return f'Invalid Distribution Number: {self.info}.'
            case MCNPSemanticCodes.INVALID_INP_MESSAGE:
                return 'Invalid INP message.'
            case MCNPSemanticCodes.INVALID_INP_TITLE:
                return 'Invalid INP title.'
            case MCNPSemanticCodes.INVALID_INP_CELLS:
                return 'Invalid INP cell card block.'
            case MCNPSemanticCodes.INVALID_INP_SURFACES:
                return 'Invalid INP surface card block.'
            case MCNPSemanticCodes.INVALID_INP_DATA:
                return 'Invalid INP data card block.'
            case MCNPSemanticCodes.INVALID_INP_OTHER:
                return 'Invalid INP other block.'
            case MCNPSemanticCodes.INVALID_CELL_NUMBER:
                return 'Invalid INP cell number.'
            case MCNPSemanticCodes.INVALID_CELL_MATERIAL:
                return 'Invalid INP cell material.'
            case MCNPSemanticCodes.INVALID_CELL_DENSITY:
                return 'Invalid INP cell density.'
            case MCNPSemanticCodes.INVALID_CELL_GEOMETRY:
                return 'Invalid INP cell geometry.'
            case MCNPSemanticCodes.INVALID_CELL_OPTION:
                return 'Invalid INP cell option.'
            case MCNPSemanticCodes.INVALID_CELL_OPTION_DESIGNATOR:
                return 'Invalid INP cell option designator.'
            case MCNPSemanticCodes.INVALID_CELL_OPTION_SUFFIX:
                return 'Invalid INP cell option suffix.'
            case MCNPSemanticCodes.INVALID_CELL_OPTION_KEYWORD:
                return 'Invalid INP cell option keyword.'
            case MCNPSemanticCodes.INVALID_CELL_OPTION_VALUE:
                return 'Invalid INP cell option value.'
            case MCNPSemanticCodes.INVALID_SURFACE_NUMBER:
                return 'Invalid INP surface name.'
            case MCNPSemanticCodes.INVALID_SURFACE_MNEMONIC:
                return f'Invalid INP surface mnemonic. {self.info}'
            case MCNPSemanticCodes.INVALID_SURFACE_TRANSFORMPERIODIC:
                return 'Invalid INP surface transform/periodic number.'
            case MCNPSemanticCodes.INVALID_SURFACE_PARAMETER:
                return 'Invalid INP surface parameter.'
            case MCNPSemanticCodes.INVALID_DATUM_MNEMONIC:
                return 'Invalid INP data card mnemonic.'
            case MCNPSemanticCodes.INVALID_DATUM_DESIGNATOR:
                return 'Invalid INP data card designator.'
            case MCNPSemanticCodes.INVALID_DATUM_SUFFIX:
                return 'Invalid INP data card suffix.'
            case MCNPSemanticCodes.INVALID_DATUM_PARAMETERS:
                return 'Invalid INP data card parameter.'
            case MCNPSemanticCodes.INVALID_DATUM_DAWWG_KEYWORD:
                return 'Invalid INP data card DAWWG keyword.'
            case MCNPSemanticCodes.INVALID_DATUM_DAWWG_VALUE:
                return 'Invalid INP data card DAWWG value.'
            case MCNPSemanticCodes.INVALID_DATUM_EMBED_KEYWORD:
                return 'Invalid INP data card EMBED keyword.'
            case MCNPSemanticCodes.INVALID_DATUM_EMBED_VALUE:
                return 'Invalid INP data card EMBED value.'
            case MCNPSemanticCodes.INVALID_DATUM_EMBEE_KEYWORD:
                return 'Invalid INP data card EMBEE keyword.'
            case MCNPSemanticCodes.INVALID_DATUM_EMBEE_VALUE:
                return 'Invalid INP data card EMBEE value.'
            case MCNPSemanticCodes.INVALID_DATUM_MATERIAL_KEYWORD:
                return 'Invalid INP data card material keyword.'
            case MCNPSemanticCodes.INVALID_DATUM_MATERIAL_VALUE:
                return 'Invalid INP data card meterial value.'
            case MCNPSemanticCodes.INVALID_COMMENT_CONTENT:
                return 'Invalid INP comment content.'
            case MCNPSemanticCodes.INVALID_HEADER_CODE:
                return 'Invalid PTRAC header code.'
            case MCNPSemanticCodes.INVALID_HEADER_CODEDATE:
                return 'Invalid PTRAC header code date.'
            case MCNPSemanticCodes.INVALID_HEADER_VERSION:
                return 'Invalid PTRAC header version.'
            case MCNPSemanticCodes.INVALID_HEADER_RUNDATE:
                return 'Invalid PTRAC header run date.'
            case MCNPSemanticCodes.INVALID_HEADER_RUNTIME:
                return 'Invalid PTRAC header run time.'
            case MCNPSemanticCodes.INVALID_HEADER_TITLE:
                return 'Invalid PTRAC header title.'
            case MCNPSemanticCodes.INVALID_HEADER_SETTINGS:
                return 'Invalid PTRAC header settings.'
            case MCNPSemanticCodes.INVALID_HEADER_NUMBERS:
                return 'Invalid PTRAC header numbers.'
            case MCNPSemanticCodes.INVALID_EVENT_TYPE:
                return 'Invalid PTRAC event type variable.'
            case MCNPSemanticCodes.INVALID_EVENT_NTER:
                return 'Invalid PTRAC event nter variable.'
            case MCNPSemanticCodes.INVALID_EVENT_NODE:
                return 'Invalid PTRAC event node variable.'
            case MCNPSemanticCodes.INVALID_EVENT_NSR:
                return 'Invalid PTRAC event nsr variable.'
            case MCNPSemanticCodes.INVALID_EVENT_NXS:
                return 'Invalid PTRAC event nxs variable.'
            case MCNPSemanticCodes.INVALID_EVENT_NTYNMTP:
                return 'Invalid PTRAC event ntynmtp variable.'
            case MCNPSemanticCodes.INVALID_EVENT_NSF:
                return 'Invalid PTRAC event nsf variable.'
            case MCNPSemanticCodes.INVALID_EVENT_ANGLE:
                return 'Invalid PTRAC event angle variable.'
            case MCNPSemanticCodes.INVALID_EVENT_NTER:
                return 'Invalid PTRAC event nter variable.'
            case MCNPSemanticCodes.INVALID_EVENT_BRANCH:
                return 'Invalid PTRAC event branch variable.'
            case MCNPSemanticCodes.INVALID_EVENT_IPT:
                return 'Invalid PTRAC event ipt variable.'
            case MCNPSemanticCodes.INVALID_EVENT_NCL:
                return 'Invalid PTRAC event ncl variable.'
            case MCNPSemanticCodes.INVALID_EVENT_MAT:
                return 'Invalid PTRAC event mat variable.'
            case MCNPSemanticCodes.INVALID_EVENT_NCP:
                return 'Invalid PTRAC event ncp variable.'
            case MCNPSemanticCodes.INVALID_EVENT_XXX:
                return 'Invalid PTRAC event xxx variable.'
            case MCNPSemanticCodes.INVALID_EVENT_YYY:
                return 'Invalid PTRAC event yyy variable.'
            case MCNPSemanticCodes.INVALID_EVENT_ZZZ:
                return 'Invalid PTRAC event zzz variable.'
            case MCNPSemanticCodes.INVALID_EVENT_UUU:
                return 'Invalid PTRAC event uuu variable.'
            case MCNPSemanticCodes.INVALID_EVENT_VVV:
                return 'Invalid PTRAC event vvv variable.'
            case MCNPSemanticCodes.INVALID_EVENT_WWW:
                return 'Invalid PTRAC event www variable.'
            case MCNPSemanticCodes.INVALID_EVENT_ERG:
                return 'Invalid PTRAC event erg variable.'
            case MCNPSemanticCodes.INVALID_EVENT_WGT:
                return 'Invalid PTRAC event wgt variable.'
            case MCNPSemanticCodes.INVALID_EVENT_TME:
                return 'Invalid PTRAC event tme variable.'
            case MCNPSemanticCodes.INVALID_EVENT_NSR:
                return 'Invalid PTRAC event nsr variable.'
            case MCNPSemanticCodes.INVALID_HISTORY_NPS:
                return 'Invalid PTRAC history nps.'
            case MCNPSemanticCodes.INVALID_HISTORY_NCL:
                return 'Invalid PTRAC history ncl.'
            case MCNPSemanticCodes.INVALID_HISTORY_NSF:
                return 'Invalid PTRAC history nsf.'
            case MCNPSemanticCodes.INVALID_HISTORY_JPTAL:
                return 'Invalid PTRAC history jptal.'
            case MCNPSemanticCodes.INVALID_HISTORY_TAL:
                return 'Invalid PTRAC history tal.'
            case MCNPSemanticCodes.INVALID_HISTORY_NEXTTYPE:
                return 'Invalid PTRAC history event type.'
