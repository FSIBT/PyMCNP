"""
Contains the ``U`` subclass of ``CellOption``.
"""

import re
from typing import Final

from ..cell_option import CellOption
from ..cell_keyword import CellKeyword
from ...utils import types, errors, _parser


class U(CellOption):
    """
    Represents INP cell card u options.

    ``U`` implements ``_card.CardOption``.

    Attributes:
        number: Cell universe number.
    """

    def __init__(self, number: types.McnpInteger):
        """
        Initializes ``U``.

        Parameters:
            number: Cell universe number.

        Raises:
            McnpError: INVALID_CELL_OPTION_VALUE.
        """

        if number is None or not (-99_999_999 <= number <= 99_999_999):
            raise errors.McnpError(errors.McnpCode.INVALID_CELL_OPTION_VALUE, str(number))

        self.keyword: Final[CellKeyword] = CellKeyword.U
        self.value: Final[types.McnpInteger] = number
        self.number: Final[types.McnpInteger] = number

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``U`` objects from INP.

        ``from_mcnp`` translates from INP to PyMCNP; it parses INP.

        Parameters:
            source: INP for ``U``.

        Returns:
            ``U`` object.

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
        if keyword != 'u':
            raise errors.McnpError(errors.McnpCode.UNRECOGNIZED_KEYWORD, str(keyword))

        tokens.popl()
        number = types.McnpInteger.from_mcnp(tokens.popl())

        return U(number)
