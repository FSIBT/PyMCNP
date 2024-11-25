"""
Contains the ``Fill`` subclass of ``CellOption``.
"""

import re
from typing import Final

from ..cell_option import CellOption, CellKeyword
from ...utils import types, errors, _parser


class Fill(CellOption):
    """
    Represents INP cell card fill options.

    ``Fill`` implements ``_card.CardOption``.

    Attributes:
        numbers: Fill cell option value or value(s) tuple.
    """

    def __init__(self, numbers: tuple[types.McnpInteger]):
        """
        Initializes ``Fill``.

        Parameters:
            numbers: Fill cell option value or value(s) tuple.

        Raises:
            McnpError: INVALID_CELL_OPTION_VALUE.
        """

        if numbers is None:
            raise errors.McnpError(errors.McnpCode.INVALID_CELL_OPTION_VALUE, str(numbers))

        for entry in numbers:
            if entry is None or not (0 <= entry <= 99_999_999):
                raise errors.McnpError(errors.McnpCode.INVALID_CELL_OPTION_VALUE, str(numbers))

        self.keyword: Final[CellKeyword] = CellKeyword.FILL
        self.value: Final[tuple[types.McnpInteger]] = numbers
        self.numbers: Final[tuple[types.McnpInteger]] = numbers

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``Fill`` objects from INP.

        ``from_mcnp`` translates from INP to PyMCNP; it parses INP.

        Parameters:
            source: INP for ``Fill``.

        Returns:
            ``Fill`` object.

        Raises:
            McnpError: EXPECTED_TOKEN, UNEXPECTED_TOKEN.
        """

        source = _parser.Preprocessor.process_inp(source)
        tokens = _parser.Parser(
            re.split(r'=| |:', source),
            errors.McnpError(errors.McnpCode.EXPECTED_TOKEN, source),
        )

        keyword = re.search(r'^[a-zA-Z*]+', tokens.peekl())
        keyword = keyword[0] if keyword else ''
        if keyword != 'fill':
            raise errors.McnpError(errors.McnpCode.UNRECOGNIZED_KEYWORD, str(keyword))

        tokens.popl()
        numbers = tuple([types.McnpInteger.from_mcnp(tokens.popl()) for _ in range(0, len(tokens))])

        return Fill(numbers)
