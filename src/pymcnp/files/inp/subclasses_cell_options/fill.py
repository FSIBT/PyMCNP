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
        number: Fill cell option value or value(s) tuple.
    """

    def __init__(self, number: types.McnpInteger):
        """
        Initializes ``Fill``.

        Parameters:
            number: Fill cell option value or value(s) tuple.

        Raises:
            McnpError: INVALID_CELL_OPTION_VALUE.
        """

        if number is None or not (0 <= number <= 99_999_999):
            raise errors.McnpError(errors.McnpCode.INVALID_CELL_OPTION_VALUE, str(number))

        self.keyword: Final[CellKeyword] = CellKeyword.FILL
        self.value: Final[types.McnpInteger] = number
        self.number: Final[types.McnpInteger] = number

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
        number = types.McnpInteger.from_mcnp(tokens.popl())

        return Fill(number)
