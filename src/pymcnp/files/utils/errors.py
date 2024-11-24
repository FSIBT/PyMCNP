"""
Contains classes representing errors for INP & PTRAC.
"""

import enum
from typing import Final


class McnpCode(enum.Enum):
    """
    Represents ``McnpError`` error codes.

    Notes:
        10X: Syntax.
        20X: Semantic, ``types.McnpInteger`` & ``types.McnpReal``.
        21X: Semantic, ``types.Designator``.
        22X: Semantic, ``types.Zaid``.
        23X: Semantic, ``types.DistributionNumber``.
        30X: Semantic, ``inp.inp``.
        31X: Semantic, ``inp.cell``.
        32X: Semantic, ``inp.surface``.
        33X: Semantic, ``inp.data``.
        34X: Semantic, ``inp.comment``.
        40X: Semantic, ``ptrac.ptrac``.
        41X: Semantic, ``ptrac.header``.
        42X: Semantic, ``ptrac.event``.
        44X: Semantic, ``ptrac.history``.
    """

    UNEXPECTED_TOKEN = 101
    EXPECTED_TOKEN = 102
    UNRECOGNIZED_KEYWORD = 103

    INVALID_TYPES_INTEGER = 200
    INVALID_TYPES_REAL = 201
    INVALID_TYPES_DESIGNATOR = 212
    INVALID_TYPES_ZAID = 223
    INVALID_TYPES_ZAID_Z = 224
    INVALID_TYPES_ZAID_A = 225
    INVALID_TYPES_ZAID_ABX = 226
    INVALID_TYPES_DN = 237

    INVALID_INP_MESSAGE = 301
    INVALID_INP_TITLE = 302
    INVALID_INP_CELLS = 303
    INVALID_INP_SURFACES = 304
    INVALID_INP_DATA = 305
    INVALID_INP_OTHER = 306
    INVALID_CELL_NUMBER = 310
    INVALID_CELL_MATERIAL = 311
    INVALID_CELL_DENSITY = 312
    INVALID_CELL_GEOMETRY = 313
    INVALID_CELL_OPTION = 314
    INVALID_CELL_OPTION_DESIGNATOR = 315
    INVALID_CELL_OPTION_SUFFIX = 316
    INVALID_CELL_OPTION_KEYWORD = 317
    INVALID_CELL_OPTION_VALUE = 318
    INVALID_SURFACE_NUMBER = 320
    INVALID_SURFACE_MNEMONIC = 321
    INVALID_SURFACE_TRANSFORMPERIODIC = 322
    INVALID_SURFACE_PARAMETER = 323
    INVALID_DATUM_MNEMONIC = 330
    INVALID_DATUM_DESIGNATOR = 331
    INVALID_DATUM_SUFFIX = 332
    INVALID_DATUM_PARAMETERS = 333
    INVALID_DATUM_OPTION_KEYWORD = 334
    INVALID_DATUM_OPTION_VALUE = 335
    INVALID_COMMENT_CONTENT = 340

    INVALID_PTRAC_HEADER = 400
    INVALID_PTRAC_HISTORIES = 401
    INVALID_HEADER_CODE = 402
    INVALID_HEADER_CODEDATE = 403
    INVALID_HEADER_VERSION = 404
    INVALID_HEADER_RUNDATE = 405
    INVALID_HEADER_RUNTIME = 406
    INVALID_HEADER_TITLE = 407
    INVALID_HEADER_SETTINGS = 408
    INVALID_HEADER_NUMBERS = 409
    INVALID_EVENT_TYPE = 410
    INVALID_EVENT_NTER = 411
    INVALID_EVENT_NODE = 412
    INVALID_EVENT_NSR = 413
    INVALID_EVENT_NXS = 414
    INVALID_EVENT_NTYNMTP = 415
    INVALID_EVENT_NSF = 416
    INVALID_EVENT_ANGLE = 417
    INVALID_EVENT_BRANCH = 419
    INVALID_EVENT_IPT = 419
    INVALID_EVENT_NCL = 420
    INVALID_EVENT_MAT = 421
    INVALID_EVENT_NCP = 422
    INVALID_EVENT_XXX = 423
    INVALID_EVENT_YYY = 424
    INVALID_EVENT_ZZZ = 425
    INVALID_EVENT_UUU = 426
    INVALID_EVENT_VVV = 427
    INVALID_EVENT_WWW = 428
    INVALID_EVENT_ERG = 429
    INVALID_EVENT_WGT = 430
    INVALID_EVENT_TME = 431
    INVALID_HISTORY_NPS = 440
    INVALID_HISTORY_NCL = 441
    INVALID_HISTORY_NSF = 442
    INVALID_HISTORY_JPTAL = 443
    INVALID_HISTORY_TAL = 444
    INVALID_HISTORY_NEXTTYPE = 445


class McnpError(Exception):
    """
    Represents errors in parsing/processing MCNP.

    PyMCNP raises ``McnpError`` while building PyMCNP objects. MCNP
    grammar violation and parameter restrictions trigger these errors.

    Attributes:
        code: Error code.
        info: Error string.
    """

    def __init__(self, code: McnpCode, info: str):
        """
        Initializes ``McnpError``

        Parameters:
            code: Error code.
            info: Error string.
        """

        self.code: Final[McnpCode] = code
        self.info: Final[str] = info

    def __str__(self) -> str:
        """
        Stringifies ``McnpError``.
        """

        head = ''
        hint = ''

        match self.code:
            case McnpCode.UNEXPECTED_TOKEN:
                head += 'Unexpected token found.'
                hint += ''
            case McnpCode.EXPECTED_TOKEN:
                head += 'Expected more token(s).'
                hint += ''
            case McnpCode.UNRECOGNIZED_KEYWORD:
                head += 'Incorrect literal/keyword.'
                hint += ''
            case McnpCode.INVALID_TYPES_INTEGER:
                head += 'Invalid integer.'
                hint += ''
            case McnpCode.INVALID_TYPES_REAL:
                head += 'Invalid real.'
                hint += ''
            case McnpCode.INVALID_TYPES_DESIGNATOR:
                head += 'Invalid designator.'
                hint += ''
            case McnpCode.INVALID_TYPES_ZAID:
                head += 'Invalid ZAID.'
                hint += ''
            case McnpCode.INVALID_TYPES_ZAID_Z:
                head += 'Invalid ZAID Z.'
                hint += ''
            case McnpCode.INVALID_TYPES_ZAID_A:
                head += 'Invalid ZAID A.'
                hint += ''
            case McnpCode.INVALID_TYPES_ZAID_ABX:
                head += 'Invalid ZAID ABX.'
                hint += ''
            case McnpCode.INVALID_TYPES_DN:
                head += 'Invalid distribution number.'
                hint += ''
            case McnpCode.INVALID_INP_MESSAGE:
                head += 'Invalid INP message.'
                hint += ''
            case McnpCode.INVALID_INP_TITLE:
                head += 'Invalid INP title.'
                hint += '``data`` cannot be ``None``.'
            case McnpCode.INVALID_INP_CELLS:
                head += 'Invalid INP cell(s).'
                hint += '``data`` cannot be ``None``.'
            case McnpCode.INVALID_INP_SURFACES:
                head += 'Invalid INP surface(s).'
                hint += '``data`` cannot be ``None``.'
            case McnpCode.INVALID_INP_DATA:
                head += 'Invalid INP data.'
                hint += '``data`` cannot be ``None``.'
            case McnpCode.INVALID_INP_OTHER:
                head += 'Invalid INP other.'
                hint += '``other`` cannot be ``None``.'
            case McnpCode.INVALID_CELL_NUMBER:
                head += 'Invalid INP cell number.'
                hint += '``1 <= cell.number <= 99_999_999``.'
            case McnpCode.INVALID_CELL_MATERIAL:
                head += 'Invalid INP cell material.'
                hint += '``0 <= cell.material <= 99_999_999``.'
            case McnpCode.INVALID_CELL_DENSITY:
                head += 'Invalid INP cell density.'
                hint += ''
            case McnpCode.INVALID_CELL_GEOMETRY:
                head += 'Invalid INP cell geometry.'
                hint += ''
            case McnpCode.INVALID_CELL_OPTION:
                head += 'Invalid INP cell option.'
                hint += ''
            case McnpCode.INVALID_CELL_OPTION_DESIGNATOR:
                head += 'Invalid INP cell option designator.'
                hint += ''
            case McnpCode.INVALID_CELL_OPTION_SUFFIX:
                head += 'Invalid INP cell option suffix.'
                hint += ''
            case McnpCode.INVALID_CELL_OPTION_KEYWORD:
                head += 'Invalid INP cell option keyword.'
                hint += ''
            case McnpCode.INVALID_CELL_OPTION_VALUE:
                head += 'Invalid INP cell option value.'
                hint += ''
            case McnpCode.INVALID_SURFACE_NUMBER:
                head += 'Invalid INP surface number.'
                hint += ''
            case McnpCode.INVALID_SURFACE_MNEMONIC:
                head += 'Invalid INP surface mnemonic.'
                hint += ''
            case McnpCode.INVALID_SURFACE_TRANSFORMPERIODIC:
                head += 'Invalid INP surface transform/periodic number.'
                hint += ''
            case McnpCode.INVALID_SURFACE_PARAMETER:
                head += 'Invalid INP surface parameter.'
                hint += ''
            case McnpCode.INVALID_DATUM_MNEMONIC:
                head += 'Invalid INP data mnemonic.'
                hint += ''
            case McnpCode.INVALID_DATUM_DESIGNATOR:
                head += 'Invalid INP data designator.'
                hint += ''
            case McnpCode.INVALID_DATUM_SUFFIX:
                head += 'Invalid INP data suffix.'
                hint += ''
            case McnpCode.INVALID_DATUM_PARAMETERS:
                head += 'Invalid INP data parameter.'
                hint += ''
            case McnpCode.INVALID_DATUM_OPTION_KEYWORD:
                head += 'Invalid INP data option keyword.'
                hint += ''
            case McnpCode.INVALID_DATUM_OPTION_VALUE:
                head += 'Invalid INP data option value.'
                hint += ''
            case McnpCode.INVALID_COMMENT_CONTENT:
                head += 'Invalid INP comment content.'
                hint += ''
            case _:
                head += "I'm working on it! :)"
                hint += ''

        if hint:
            return f'\n\033[31;4;1mMcnpError[{self.code.name}]\033[0m: {head}\n|\n| {repr(self.info)}\n|\n| \033[35;4mHint\033[0m: {hint}\n|'
        else:
            return f'\n\033[31;4;1mMcnpError[{self.code.name}]\033[0m: {head}\n|\n| {repr(self.info)}\n|'
