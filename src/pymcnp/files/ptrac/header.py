"""
Contains classes representing INP headers.
"""

from __future__ import annotations
from typing import Final

from ..utils import types
from ..utils import errors
from ..utils import _parser
from ..utils import _object


class PtracKeywords(_object.PyMcnpKeyword):
    """
    Represents PTRAC input format index keywords.

    ``PtracKeywords`` implements ``_object.PyMcnpKeyword``.
    """

    BUFFER = 1
    CELL = 2
    EVENT = 3
    FILE = 4
    FILTER = 5
    MAX = 6
    MENP = 7
    NPS = 8
    SURFACE = 9
    TALLY = 10
    TYPE = 11
    VALUE = 12
    WRITE = 13
    UNKNOWN = 14

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``PtracKeywords`` objects from PTRAC.

        ``from_mcnp`` translates from PTRAC to PyMCNP; it parses PTRAC.

        Parameters:
            source: PTRAC for ``PtracKeywords``.

        Returns:
            ``PtracKeywords`` object.

        Raises:
            McnpError: INVALID_EVENT_TYPE.
        """

        source = _parser.Preprocessor.process_ptrac(source)

        try:
            return PtracKeywords(int(source))
        except ValueError:
            raise errors.McnpError(errors.McnpCode.INVALID_EVENT_TYPE)


class Header(_object.PyMcnpObject):
    """
    Represents PTRAC headers.

    ``Header`` implements ``_object.PyMcnpObject``.

    Attributes:
        code: Simulation name.
        code_date: Simulation compilation date.
        version: Simulation version.
        run_date: Simulation run date.
        run_time: Simulation run time.
        title: Simulation title.
        settings: PTRAC input format.
        numbers: PTRAC event variable counts by type.
        ids: PTRAC event variable identifiers by type.
    """

    def __init__(
        self,
        code: str,
        code_date: str,
        version: str,
        run_date: str,
        run_time: str,
        title: str,
        settings: dict,
        numbers: tuple[int],
        ids: tuple[int],
    ):
        """
        Initializes ``Header``.

        Parameters:
            code: Simulation name.
            code_date: Simulation compilation date.
            version: Simulation version.
            run_date: Simulation run date.
            run_time: Simulation run time.
            title: Simulation title.
            settings: PTRAC input format.
            numbers: PTRAC event variable counts by type.
            ids: PTRAC event variable identifiers by type.

        Raises:
            McnpError: INVALID_HEADER_CODE.
            McnpError: INVALID_HEADER_CODEDATE.
            McnpError: INVALID_HEADER_VERSION.
            McnpError: INVALID_HEADER_RUNDATE.
            McnpError: INVALID_HEADER_RUNTIME.
            McnpError: INVALID_HEADER_TITLE.
        """

        if code is None:
            raise errors.McnpError(errors.McnpCode.INVALID_HEADER_CODE)

        if code_date is None:
            raise errors.McnpError(errors.McnpCode.INVALID_HEADER_CODEDATE)

        if version is None:
            raise errors.McnpError(errors.McnpCode.INVALID_HEADER_VERSION)

        if run_date is None:
            raise errors.McnpError(errors.McnpCode.INVALID_HEADER_RUNDATE)

        if run_time is None:
            raise errors.McnpError(errors.McnpCode.INVALID_HEADER_RUNTIME)

        if title is None:
            raise errors.McnpError(errors.McnpCode.INVALID_HEADER_TITLE)

        if settings is None:
            raise errors.McnpError(errors.McnpCode.INVALID_HEADER_SETTING)

        if numbers is None:
            raise errors.McnpError(errors.McnpCode.INVALID_HEADER_NUMBERS)

        for number in numbers:
            if number is None:
                raise errors.McnpError(errors.McnpCode.INVALID_HEADER_NUMBERS)

        if ids is None:
            raise errors.McnpError(errors.McnpCode.INVALID_HEADER_IDS)

        for id_ in ids:
            if id_ is None:
                raise errors.McnpError(errors.McnpCode.INVALID_HEADER_IDS)

        self.code: Final[str] = code
        self.code_date: Final[str] = code_date
        self.version: Final[str] = version
        self.run_date: Final[str] = run_date
        self.run_time: Final[str] = run_time
        self.title: Final[str] = title
        self.settings: Final[dict] = settings
        self.numbers: Final[tuple[int]] = numbers
        self.ids: Final[tuple[int]] = ids

    def __str__(self):
        out = f'  Program: {self.code} ; Version:({self.version} , {self.code_date}) ; Current Date:{self.run_date} {self.run_time}\n'
        out += f'  {self.title}\n'
        for k, v in self.settings.items():
            out += f"    {k.name}: {' '.join(str(val) for val in v)}\n"
        for k in self.ids:
            out += f'    IDS: {k}\n'
        for k in self.numbers:
            out += f'    Numbers: {k}\n'
        return out

    @staticmethod
    def from_mcnp(source: str) -> tuple[Header, str]:
        """
        Generates ``Header`` objects from PTRAC.

        ``from_mcnp`` translates from PTRAC to PyMCNP; it parses PTRAC.

        Parameters:
            source: PTRAC for ``Header``.

        Returns:
            ``Header`` object.

        Raises:
            MCNPSyntaxError: TOOFEW_HEADER, TOOLONG_HEADER, KEYWORD_HEADER_MINUS1
        """

        source = _parser.Preprocessor.process_ptrac(source)
        lines = _parser.Parser(
            source.split('\n'),
            errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.TOOFEW_HEADER),
        )

        # Processing Magic Number
        if lines.popl() != '   -1':
            raise errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.KEYWORD_HEADER_MINUS1)

        # Processing Header
        tokens = _parser.Parser.from_fortran(
            [4, 5, 32, 9, 10],
            lines.popl(),
            errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.TOOFEW_HEADER),
        )

        code = tokens.popl()
        version = tokens.popl()
        code_date = tokens.popl()
        run_date = tokens.popl()
        run_time = tokens.popl()
        title = lines.popl()

        # Processing Settings Block
        tokens = _parser.Parser.from_fortran(
            10 * [12],
            lines.popl()[1:],
            errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.TOOFEW_HEADER),
        )

        m = types.McnpReal.from_mcnp(tokens.popl())
        if not (m == 13 or m == 14):
            raise errors.McnpError(errors.McnpCode.INVALID_HEADER_SETTINGS)

        settings = {}
        for i in range(0, int(m.value)):
            if not tokens:
                tokens = _parser.Parser.from_fortran(
                    10 * [12],
                    lines.popl()[1:],
                    errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.TOOFEW_HEADER),
                )

            n = types.McnpReal.from_mcnp(tokens.popl())
            if not (n.value != 'j' and n.value >= 0):
                raise errors.McnpError(errors.McnpCode.INVALID_HEADER_SETTINGS)

            values = [None] * int(n.value)
            for j in range(0, int(n.value)):
                if not tokens:
                    tokens = _parser.Parser.from_fortran(
                        10 * [12],
                        lines.popl()[1:],
                        errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.TOOFEW_HEADER),
                    )

                values[j] = tokens.popl()

            settings[PtracKeywords(i + 1)] = tuple(values)

        while tokens:
            if types.McnpReal.from_mcnp(tokens.popl()) != 0:
                raise errors.McnpError(errors.McnpCode.INVALID_HEADER_SETTINGS)

        # Processing Numbers
        tokens = _parser.Parser.from_fortran(
            20 * [5],
            lines.popl()[1:],
            errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.TOOFEW_HEADER),
        )

        numbers = tuple([types.McnpInteger.from_mcnp(tokens.popl()) for _ in range(0, len(tokens))])

        # Processing Entry Counts
        tokens = _parser.Parser.from_fortran(
            30 * [4],
            lines.popl()[1:],
            errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.TOOFEW_HEADER),
        )

        total = sum([number.value for number in numbers[:11]])
        ids = [None] * total

        for i in range(0, total):
            if not tokens:
                tokens = _parser.Parser.from_fortran(
                    min(total - i, 30) * [4],
                    lines.popl()[1:],
                    errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.TOOFEW_HEADER),
                )

            ids[i] = types.McnpInteger.from_mcnp(tokens.popl())

        return Header(
            code, code_date, version, run_date, run_time, title, settings, numbers, ids
        ), '\n'.join(list(lines.deque))

    def to_mcnp(self):
        """
        Generates PTRAC from ``Header`` objects.

        ``to_mcnp`` translates from PTRAC to PyMCNP.

        Returns:
            INP for ``Header``.
        """

        assert False, 'NotImplemented'
