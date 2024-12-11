"""
Contains the ``Ext`` subclass of ``CellOption``.
"""

import re
from typing import Final

from ..cell_option import CellOption
from ..cell_keyword import CellKeyword
from ...utils import types
from ...utils import errors
from ...utils import _parser


class Ext(CellOption):
    """
    Represents INP cell card ext options.

    ``Ext`` implements ``_card.CardOption``.

    Attributes:
        stretch: Cell exponential transform stretching specifier
        designator: Cell option particle designator
    """

    def __init__(self, stretch: str, designator: types.Designator):
        """
        Initializes ``Ext``.

        Parameters:
            stretch: Cell exponential transform stretching specifier
            designator: Cell option particle designator

        Raises:
            McnpError: INVALID_CELL_OPTION_VALUE.
            McnpError: INVALID_CELL_OPTION_DESIGNATOR.
        """

        if stretch is None:
            raise errors.McnpError(errors.McnpCode.INVALID_CELL_OPTION_VALUE, str(stretch))
        if designator is None:
            raise errors.McnpError(errors.McnpCode.INVALID_CELL_OPTION_DESIGNATOR, str(designator))

        self.keyword: Final[CellKeyword] = CellKeyword.EXT
        self.value: Final[str] = stretch
        self.stretch: Final[str] = stretch
        self.designator: Final[types.Designator] = designator

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``Ext`` objects from INP.

        ``from_mcnp`` translates from INP to PyMCNP; it parses INP.

        Parameters:
            source: INP for ``Ext``.

        Returns:
            ``Ext`` object.

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
        if keyword != 'ext':
            raise errors.McnpError(errors.McnpCode.UNRECOGNIZED_KEYWORD, str(keyword))

        tokens.popl()
        designator = types.Designator.from_mcnp(tokens.popl())
        stretch = str.from_mcnp(tokens.popl())

        return Ext(stretch, designator)
