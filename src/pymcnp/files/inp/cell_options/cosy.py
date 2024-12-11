"""
Contains the ``Cosy`` subclass of ``CellOption``.
"""

import re
from typing import Final

from ..cell_option import CellOption
from ..cell_keyword import CellKeyword
from ...utils import types
from ...utils import errors
from ...utils import _parser


class Cosy(CellOption):
    """
    Represents INP cell card cosy options.

    ``Cosy`` implements ``_card.CardOption``.

    Attributes:
        number: Cell cosy map number.
    """

    def __init__(self, number: types.McnpInteger):
        """
        Initializes ``Cosy``.

        Parameters:
            number: Cell cosy map number.

        Raises:
            McnpError: INVALID_CELL_OPTION_VALUE.
        """

        if number is None or number.value not in {1, 2, 3, 4, 5, 6}:
            raise errors.McnpError(errors.McnpCode.INVALID_CELL_OPTION_VALUE, str(number))

        self.keyword: Final[CellKeyword] = CellKeyword.COSY
        self.value: Final[types.McnpInteger] = number
        self.number: Final[types.McnpInteger] = number

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``Cosy`` objects from INP.

        ``from_mcnp`` translates from INP to PyMCNP; it parses INP.

        Parameters:
            source: INP for ``Cosy``.

        Returns:
            ``Cosy`` object.

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
        if keyword != 'cosy':
            raise errors.McnpError(errors.McnpCode.UNRECOGNIZED_KEYWORD, str(keyword))

        tokens.popl()
        number = types.McnpInteger.from_mcnp(tokens.popl())

        return Cosy(number)
