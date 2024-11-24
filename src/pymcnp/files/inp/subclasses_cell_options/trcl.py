"""
Contains the ``Trcl`` subclass of ``CellOption``."""

import re
from typing import Final

from ..cell import CellOption, CellKeyword
from ....utils import errors, _parser


class Trcl(CellOption):
    """
    Represents INP cell card trcl options.

    ``Trcl`` implements ``_card.CardOption``.

    Attributes:
        value: Cell coordinate transformation option value(s).
    """

    def __init__(self, value: int):
        """
        Initializes ``Trcl``.

        Parameters:
            value: Cell coordinate transformation option value(s).

        Raises:
            McnpError: INVALID_CELL_OPTION_VALUE.
        """

        if value is None or not (1 <= value <= 999):
            raise errors.McnpError(errors.McnpCode.INVALID_CELL_OPTION_VALUE, str(value))

        self.keyword: Final[CellKeyword] = CellKeyword.TRCL
        self.value: Final[int] = value
        self.value: Final[int] = value

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``Trcl`` objects from INP.

        ``from_mcnp`` translates from INP to PyMCNP; it parses INP.

        Parameters:
            source: INP for ``Trcl``.

        Returns:
            ``Trcl`` object.

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
        if keyword != 'trcl':
            raise errors.McnpError(errors.McnpCode.UNRECOGNIZED_KEYWORD, str(keyword))

        tokens.popl()
        value = int.from_mcnp(tokens.popl())

        return Trcl(value)
