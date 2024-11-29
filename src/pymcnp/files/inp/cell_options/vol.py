"""
Contains the ``Vol`` subclass of ``CellOption``.
"""

import re
from typing import Final

from ..cell_option import CellOption
from ..cell_keyword import CellKeyword
from ...utils import types, errors, _parser


class Vol(CellOption):
    """
    Represents INP cell card vol options.

    ``Vol`` implements ``_card.CardOption``.

    Attributes:
        volume: Cell volume
    """

    def __init__(self, volume: types.McnpReal):
        """
        Initializes ``Vol``.

        Parameters:
            volume: Cell volume

        Raises:
            McnpError: INVALID_CELL_OPTION_VALUE.
        """

        if volume is None or not (volume >= 0):
            raise errors.McnpError(errors.McnpCode.INVALID_CELL_OPTION_VALUE, str(volume))

        self.keyword: Final[CellKeyword] = CellKeyword.VOL
        self.value: Final[types.McnpReal] = volume
        self.volume: Final[types.McnpReal] = volume

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``Vol`` objects from INP.

        ``from_mcnp`` translates from INP to PyMCNP; it parses INP.

        Parameters:
            source: INP for ``Vol``.

        Returns:
            ``Vol`` object.

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
        if keyword != 'vol':
            raise errors.McnpError(errors.McnpCode.UNRECOGNIZED_KEYWORD, str(keyword))

        tokens.popl()
        volume = types.McnpReal.from_mcnp(tokens.popl())

        return Vol(volume)
