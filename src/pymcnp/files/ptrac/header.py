"""
``header`` contains classes representing PTRAC headers.

``header`` packages the ``Header`` class, providing an object-oriented,
importable interface for PTRAC headers.
"""

from __future__ import annotations
from typing import Final
from enum import Enum

from ..utils import _parser
from ..utils import errors
from ..utils import types


class Header:
    """
    ``Header`` represents PTRAC headers.

    ``Header`` implements PTRAC headers as a Python class. Its attributes store
    PTRAC header parameters, and its methods provide entry points and endpoints
    for working with PTRAC. It represents the PTRAC header syntax element.

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

    class PtracKeywords(Enum):
        """
        ``PtracKeywords`` represents PTRAC input format index keywords.

        ``PtracKeywords`` implements PTRAC input format index keywords as a
        Python inner class. It enumerates input format index keywords. It
        represents the PTRAC input format index keywords syntax element, so
        ``Header`` depends on ``PtracKeywords`` as an enum.

        Notes:
            ``PtracKeywords`` does not currently implement a ``from_mcnp`
            method because ``Header`` does not currently require it.
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
        ``__init__`` initializes ``Header``.

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
            MCNPSemanticError: INVALID_HEADER_CODE.
            MCNPSemanticError: INVALID_HEADER_CODEDATE.
            MCNPSemanticError: INVALID_HEADER_VERSION.
            MCNPSemanticError: INVALID_HEADER_RUNDATE.
            MCNPSemanticError: INVALID_HEADER_RUNTIME.
            MCNPSemanticError: INVALID_HEADER_TITLE.
        """

        if code is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_HEADER_CODE)

        if code_date is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_HEADER_CODEDATE)

        if version is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_HEADER_VERSION)

        if run_date is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_HEADER_RUNDATE)

        if run_time is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_HEADER_RUNTIME)

        if title is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_HEADER_TITLE)

        if settings is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_HEADER_SETTING)

        if numbers is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_HEADER_NUMBERS)

        for number in numbers:
            if number is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_HEADER_NUMBERS)

        if ids is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_HEADER_IDS)

        for id_ in ids:
            if id_ is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_HEADER_IDS)

        self.code: Final[str] = code
        self.code_date: Final[str] = code_date
        self.version: Final[str] = version
        self.run_date: Final[str] = run_date
        self.run_time: Final[str] = run_time
        self.title: Final[str] = title
        self.settings: Final[dict] = settings
        self.numbers: Final[tuple[int]] = numbers
        self.ids: Final[tuple[int]] = ids

    @staticmethod
    def from_mcnp(source: str) -> tuple[Header, str]:
        """
        ``from_mcnp`` generates ``Header`` objects from PTRAC.

        ``from_mcnp`` constructs instances of ``Header`` from PTRAC source
        strings, so it operates as a class constructor method and PTRAC parser
        helper function.

        Parameters:
            source: PTRAC for header.

        Returns:
            ``Header`` object.

        Raises:
            MCNPSyntaxError: TOOFEW_HEADER, TOOLONG_HEADER, KEYWORD_HEADER_MINUS1
        """

        source = _parser.Preprocessor.process_ptrac(source)
        lines = _parser.Parser(
            source.split('\n'), errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.TOOFEW_HEADER)
        )

        # Processing Magic Number
        if lines.popl() != '-1':
            raise errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.KEYWORD_HEADER_MINUS1)

        # Processing Header
        tokens = _parser.Parser(
            lines.popl().split(' '), errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.TOOFEW_HEADER)
        )

        code = tokens.popl()
        version = tokens.popl()
        code_date = tokens.popl()
        run_date = tokens.popl()
        run_time = tokens.popl()
        title = lines.popl()

        # Processing Settings Block
        tokens = _parser.Parser(
            lines.popl().strip().split(' '),
            errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.TOOFEW_HEADER),
        )
        if len(tokens) != 10:
            raise errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.TOOFEW_HEADER)

        m = types.McnpReal.from_mcnp(tokens.popl())
        if not (m == 13 or m == 14):
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_HEADER_SETTINGS)

        settings = {}
        for i in range(0, int(m.value)):
            if not tokens:
                tokens = _parser.Parser(
                    lines.popl().strip().split(' '),
                    errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.TOOFEW_HEADER),
                )

                if len(tokens) != 10:
                    raise errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.TOOFEW_HEADER)

            n = types.McnpReal.from_mcnp(tokens.popl())
            if not (n.value != 'j' and n.value >= 0):
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_HEADER_SETTINGS)

            values = [None] * int(n.value)
            for j in range(0, int(n.value)):
                if not tokens:
                    tokens = _parser.Parser(
                        lines.popl().strip().split(' '),
                        errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.TOOFEW_HEADER),
                    )

                    if len(tokens) != 10:
                        raise errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.TOOFEW_HEADER)

                values[j] = tokens.popl()

            settings[Header.PtracKeywords(i + 1)] = tuple(values)

        while tokens:
            if types.McnpReal.from_mcnp(tokens.popl()) != 0:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_HEADER_SETTINGS)

        # Processing Numbers
        tokens = _parser.Parser(
            lines.popl().strip().split(' '),
            errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.TOOFEW_HEADER),
        )
        if len(tokens) != 20:
            raise errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.TOOFEW_HEADER)

        numbers = []
        while tokens:
            n = types.McnpInteger.from_mcnp(tokens.peekl())
            if not n >= 0:
                raise errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.TOOFEW_HEADER)

            numbers.append(n)
            tokens.popl()

        numbers = tuple(numbers)

        if [number.value for number in numbers][1:11] not in [
            [5, 3, 6, 3, 6, 3, 6, 3, 6, 3],
            [6, 3, 7, 3, 7, 3, 7, 3, 7, 3],
            [6, 9, 7, 9, 7, 9, 7, 9, 7, 9],
            [7, 9, 8, 9, 8, 9, 8, 9, 8, 9],
        ]:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_HEADER_NUMBERS)

        # Processing Entry Counts
        tokens = _parser.Parser(
            lines.popl().strip().split(' '),
            errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.TOOFEW_HEADER),
        )
        if len(tokens) > 30:
            raise errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.TOOMANY_HEADER)

        total = sum([number.value for number in numbers][:10])
        ids = [None] * total

        for i in range(0, total):
            if not tokens:
                tokens = _parser.Parser(
                    lines.popl().strip().split(' '),
                    errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.TOOFEW_HEADER),
                )
                if len(tokens) > 30:
                    raise errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.TOOMANY_HEADER)

            ids[i] = tokens.popl()

        return Header(
            code, code_date, version, run_date, run_time, title, settings, numbers, ids
        ), '\n'.join(list(lines.deque))

    def to_arguments(self):
        """
        ``to_arguments`` makes dictionaries from ``Header`` objects.

        ``to_arguments`` creates Python dictionaries from ``Header`` objects,
        so it provides an MCNP endpoint. The dictionary keys follow the MCNP
        manual.

        Returns:
            Dictionary for ``Header`` object.
        """

        return {
            'kod': self.code,
            'loddat': self.code_date,
            'ver': self.version,
            'idtm': (self.run_date, self.run_time),
            'aid': self.title,
            'm n v ... V ...': self.settings,
            'N1 ... N20': self.numbers,
            'L ... L': self.ids,
        }
