"""
'header'
"""


from typing import Self
from enum import Enum

from .._utils import parser
from .._utils import types


class PtracKeywords(Enum):
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


class Header:
    """
    'Header'
    """

    def __init__(self) -> Self:
        """
        '__init__'
        """

        self.code: str = None
        self.code_date: str = None
        self.version: str = None
        self.run_date: str = None
        self.run_time: str = None
        self.title: str = None
        self.settings: dict[PtracKeywords, list[float]] = {
            PtracKeywords.BUFFER: None,
            PtracKeywords.CELL: None,
            PtracKeywords.EVENT: None,
            PtracKeywords.FILE: None,
            PtracKeywords.FILTER: None,
            PtracKeywords.MAX: None,
            PtracKeywords.MENP: None,
            PtracKeywords.NPS: None,
            PtracKeywords.SURFACE: None,
            PtracKeywords.TALLY: None,
            PtracKeywords.TYPE: None,
            PtracKeywords.VALUE: None,
            PtracKeywords.WRITE: None,
            PtracKeywords.UNKNOWN: None,
        }
        self.numbers: tuple[int] = None
        self.ids: tuple[int] = None

    def set_code(self, code: str) -> None:
        """
        'set_code'
        """

        if code is None:
            raise ValueError

        self.code = code

    def set_code_date(self, code_date: str) -> None:
        """
        'set_code_date'
        """

        if code_date is None:
            raise ValueError

        self.code_date = code_date

    def set_version(self, version: str) -> None:
        """
        'set_version'
        """

        if version is None:
            raise ValueError

        self.version = version

    def set_run_date(self, run_date: str) -> None:
        """
        'set_run_date'
        """

        if run_date is None:
            raise ValueError

        self.run_date = run_date

    def set_run_time(self, run_time: str) -> None:
        """
        'set_run_time'
        """

        if run_time is None:
            raise ValueError

        self.run_time = run_time

    def set_title(self, title: str) -> None:
        """
        'set_title'
        """

        if title is None or not (len(title) < 80):
            raise ValueError

        self.title = title

    @classmethod
    def from_mcnp(cls, source: str) -> tuple[Self, str]:
        """
        'from_mcnp'
        """

        header = cls()

        source = parser.Preprocessor.process_ptrac(source)
        lines = parser.Parser(SyntaxError).from_string(source, "\n")

        # Processing Magic Number
        if lines.popl() != "-1":
            raise SyntaxError

        # Processing Header
        tokens = parser.Parser(SyntaxError).from_string(lines.popl(), " ")
        if len(tokens) != 5:
            raise SyntaxError

        header.set_code(tokens.popl())
        header.set_version(tokens.popl())
        header.set_code_date(tokens.popl())
        header.set_run_date(tokens.popl())
        header.set_run_time(tokens.popl())

        # Processing Title
        header.set_title(lines.popl())

        # Processing Settings Block
        tokens = parser.Parser(SyntaxError).from_string(lines.popl().strip(), " ")
        if len(tokens) != 10:
            raise SyntaxError

        m = types.cast_fortran_real(tokens.popl(), lambda f: f == 13 or f == 14)
        if m is None:
            raise ValueError

        for i in range(0, int(m)):
            if not tokens:
                tokens = parser.Parser(SyntaxError).from_string(
                    lines.popl().strip(), " "
                )
                if len(tokens) != 10:
                    raise SyntaxError

            n = types.cast_fortran_real(tokens.popl(), lambda f: f >= 0)
            if n is None:
                raise ValueError

            values = [None] * int(n)
            for j in range(0, int(n)):
                if not tokens:
                    tokens = parser.Parser(SyntaxError).from_string(
                        lines.popl().strip(), " "
                    )
                    if len(tokens) != 10:
                        raise SyntaxError

                values[j] = tokens.popl()

            header.settings[PtracKeywords(i + 1)] = tuple(values)

        while tokens:
            if types.cast_fortran_real(tokens.popl(), lambda f: f == 0) is None:
                raise ValueError

        # Processing Numbers
        tokens = parser.Parser(SyntaxError).from_string(lines.popl().strip(), " ")
        if len(tokens) != 20:
            raise SyntaxError

        numbers = []
        while tokens:
            n = types.cast_fortran_integer(tokens.peekl(), lambda i: i >= 0)
            if n is None:
                raise SyntaxError

            numbers.append(n)
            tokens.popl()

        header.numbers = tuple(numbers)

        if numbers[1:12] not in {
            [5, 3, 6, 3, 6, 3, 6, 3, 6, 3],
            [6, 3, 7, 3, 7, 3, 7, 3, 7, 3],
            [6, 9, 7, 9, 7, 9, 7, 9, 7, 9],
            [7, 9, 8, 9, 8, 9, 8, 9, 8, 9],
        }:
            raise SyntaxError

        # Processing Entry Counts
        tokens = parser.Parser(SyntaxError).from_string(lines.popl().strip(), " ")
        if len(tokens) > 30:
            raise SyntaxError

        total = sum(header.numbers[:10])
        header.ids = [None] * total

        for i in range(0, total):
            if not tokens:
                tokens = parser.Parser(SyntaxError).from_string(
                    lines.popl().strip(), " "
                )
                if len(tokens) > 30:
                    raise SyntaxError

            header.ids[i] = tokens.popl()

        return header, "\n".join(list(lines.deque))

    def to_arguments(self):
        """
        'to_arguments'
        """

        return {
            "code": self.code,
            "code_date": self.code_date,
            "version": self.version,
            "run_date": self.run_date,
            "run_time": self.run_time,
            "title": self.title,
            "settings": self.settings,
            "numbers": self.numbers,
            "ids": self.ids,
        }
