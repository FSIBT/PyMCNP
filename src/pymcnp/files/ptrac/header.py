"""
``header`` contains classes representing PTRAC headers.

``header`` packages the ``Header`` class, providing an object-oriented,
importable interface for PTRAC headers.
"""

from __future__ import annotations
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

    def __init__(self):
        """
        ``__init__`` initializes ``Header``.
        """

        self.code: str = None
        self.code_date: str = None
        self.version: str = None
        self.run_date: str = None
        self.run_time: str = None
        self.title: str = None
        self.settings: dict[self.PtracKeywords, list[float]] = {
            self.PtracKeywords.BUFFER: None,
            self.PtracKeywords.CELL: None,
            self.PtracKeywords.EVENT: None,
            self.PtracKeywords.FILE: None,
            self.PtracKeywords.FILTER: None,
            self.PtracKeywords.MAX: None,
            self.PtracKeywords.MENP: None,
            self.PtracKeywords.NPS: None,
            self.PtracKeywords.SURFACE: None,
            self.PtracKeywords.TALLY: None,
            self.PtracKeywords.TYPE: None,
            self.PtracKeywords.VALUE: None,
            self.PtracKeywords.WRITE: None,
            self.PtracKeywords.UNKNOWN: None,
        }
        self.numbers: tuple[int] = None
        self.ids: tuple[int] = None

    def set_code(self, code: str) -> None:
        """
        ``set_code`` stores PTRAC header code variable.

        ``set_code`` checks given arguments before assigning the given value
        to ``code.code``. If given an unrecognized argument, it raises
        semantic errors.

        Parameters:
            code: Simulation name.

        Raises:
            MCNPSemanticError: INVALID_HEADER_CODE.
        """

        if code is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_HEADER_CODE)

        self.code = code

    def set_code_date(self, code_date: str) -> None:
        """
        ``set_code_date`` stores PTRAC header code date variable.

        ``set_code_date`` checks given arguments before assigning the given value
        to ``Header.code_date``. If given an unrecognized argument, it raises
        semantic errors.

        Parameters:
            code_date: Simulation compilation date.

        Raises:
            MCNPSemanticError: INVALID_HEADER_CODEDATE.
        """

        if code_date is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_HEADER_CODEDATE)

        self.code_date = code_date

    def set_version(self, version: str) -> None:
        """
        ``set_version`` stores PTRAC header version variable.

        set_version`` checks given arguments before assigning the given value
        to ``Header.version``. If given an unrecognized argument, it raises
        semantic errors.

        Parameters:
            version: Simulation version.

        Raises:
            MCNPSemanticError: INVALID_HEADER_VERSION.
        """

        if version is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_HEADER_VERSION)

        self.version = version

    def set_run_date(self, run_date: str) -> None:
        """
        ``set_run_date`` stores PTRAC header run date variable.

        ``set_run_date`` checks given arguments before assigning the given value
        to ``Header.run_date``. If given an unrecognized argument, it raises
        semantic errors.

        Parameters:
            run_date: Simulation run date.

        Raises:
            MCNPSemanticError: INVALID_HEADER_RUNDATE.
        """

        if run_date is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_HEADER_RUNDATE)

        self.run_date = run_date

    def set_run_time(self, run_time: str) -> None:
        """
        ``set_run_time`` stores PTRAC header run time variable.

        ``set_run_time`` checks given arguments before assigning the given value
        to ``Header.run_time``. If given an unrecognized argument, it raises
        semantic errors.

        Parameters:
            run_time: Simulation run time.

        Raises:
            MCNPSemanticError: INVALID_HEADER_RUNTIME.
        """

        if run_time is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_HEADER_RUNTIME)

        self.run_time = run_time

    def set_title(self, title: str) -> None:
        """
        ``set_title`` stores PTRAC header title variable.

        set_title`` checks given arguments before assigning the given value
        to ``title.code``. If given an unrecognized argument, it raises
        semantic errors.

        Parameters:
            title: Simulation title.

        Raises:
            MCNPSemanticError: INVALID_HEADER_TITLE.
        """

        if title is None or not (len(title) < 80):
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_HEADER_TITLE)

        self.title = title

    @classmethod
    def from_mcnp(cls, source: str) -> tuple[Header, str]:
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

        header = cls()

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
        header.set_code(tokens.popl())
        header.set_version(tokens.popl())
        header.set_code_date(tokens.popl())
        header.set_run_date(tokens.popl())
        header.set_run_time(tokens.popl())

        # Processing Title
        header.set_title(lines.popl())

        # Processing Settings Block
        tokens = _parser.Parser(
            lines.popl().strip().split(' '),
            errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.TOOFEW_HEADER),
        )
        if len(tokens) != 10:
            raise errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.TOOFEW_HEADER)

        m = types.cast_fortran_real(tokens.popl(), lambda f: f == 13 or f == 14)
        if m is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_HEADER_SETTINGS)

        for i in range(0, int(m)):
            if not tokens:
                tokens = _parser.Parser(
                    lines.popl().strip().split(' '),
                    errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.TOOFEW_HEADER),
                )

                if len(tokens) != 10:
                    raise errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.TOOFEW_HEADER)

            n = types.cast_fortran_real(tokens.popl(), lambda f: f >= 0)
            if n is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_HEADER_SETTINGS)

            values = [None] * int(n)
            for j in range(0, int(n)):
                if not tokens:
                    tokens = _parser.Parser(
                        lines.popl().strip().split(' '),
                        errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.TOOFEW_HEADER),
                    )

                    if len(tokens) != 10:
                        raise errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.TOOFEW_HEADER)

                values[j] = tokens.popl()

            header.settings[Header.PtracKeywords(i + 1)] = tuple(values)

        while tokens:
            if types.cast_fortran_real(tokens.popl(), lambda f: f == 0) is None:
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
            n = types.cast_fortran_integer(tokens.peekl(), lambda i: i >= 0)
            if n is None:
                raise errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.TOOFEW_HEADER)

            numbers.append(n)
            tokens.popl()

        header.numbers = tuple(numbers)

        if numbers[1:11] not in [
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

        total = sum(header.numbers[:10])
        header.ids = [None] * total

        for i in range(0, total):
            if not tokens:
                tokens = _parser.Parser(
                    lines.popl().strip().split(' '),
                    errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.TOOFEW_HEADER),
                )
                if len(tokens) > 30:
                    raise errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.TOOMANY_HEADER)

            header.ids[i] = tokens.popl()

        return header, '\n'.join(list(lines.deque))

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
