"""
Contains the ``Elpt`` subclass of ``CellOption``.
"""

import re
from typing import Final

from ..cell_option import CellOption
from ..cell_keyword import CellKeyword
from ...utils import types, errors, _parser


class Elpt(CellOption):
    """
    Represents INP cell card elpt options.

    ``Elpt`` implements ``_card.CardOption``.

    Attributes:
        cutoff: Cell energy cutoff.
        designator: Cell option particle designator
    """

    def __init__(self, cutoff: types.McnpReal, designator: types.Designator):
        """
        Initializes ``Elpt``.

        Parameters:
            cutoff: Cell energy cutoff.
            designator: Cell option particle designator

        Raises:
            McnpError: INVALID_CELL_OPTION_VALUE.
            McnpError: INVALID_CELL_OPTION_DESIGNATOR.
        """

        if cutoff is None:
            raise errors.McnpError(errors.McnpCode.INVALID_CELL_OPTION_VALUE, str(cutoff))
        if designator is None:
            raise errors.McnpError(errors.McnpCode.INVALID_CELL_OPTION_DESIGNATOR, str(designator))

        self.keyword: Final[CellKeyword] = CellKeyword.ELPT
        self.value: Final[types.McnpReal] = cutoff
        self.cutoff: Final[types.McnpReal] = cutoff
        self.designator: Final[types.Designator] = designator

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``Elpt`` objects from INP.

        ``from_mcnp`` translates from INP to PyMCNP; it parses INP.

        Parameters:
            source: INP for ``Elpt``.

        Returns:
            ``Elpt`` object.

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
        if keyword != 'elpt':
            raise errors.McnpError(errors.McnpCode.UNRECOGNIZED_KEYWORD, str(keyword))

        tokens.popl()
        designator = types.Designator.from_mcnp(tokens.popl())
        cutoff = types.McnpReal.from_mcnp(tokens.popl())

        return Elpt(cutoff, designator)
