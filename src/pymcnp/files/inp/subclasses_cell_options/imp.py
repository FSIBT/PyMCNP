"""
Contains the ``Imp`` subclass of ``CellOption``.
"""

import re
from typing import Final

from ..cell_option import CellOption, CellKeyword
from ...utils import types, errors, _parser


class Imp(CellOption):
    """
    Represents INP cell card imp options.

    ``Imp`` implements ``_card.CardOption``.

    Attributes:
        importance: Particle(s) importance in cell
        designator: Cell option particle designator
    """

    def __init__(self, importance: types.McnpReal, designator: types.Designator):
        """
        Initializes ``Imp``.

        Parameters:
            importance: Particle(s) importance in cell
            designator: Cell option particle designator

        Raises:
            McnpError: INVALID_CELL_OPTION_VALUE.
            McnpError: INVALID_CELL_OPTION_DESIGNATOR.
        """

        if importance is None:
            raise errors.McnpError(errors.McnpCode.INVALID_CELL_OPTION_VALUE, str(importance))
        if designator is None:
            raise errors.McnpError(errors.McnpCode.INVALID_CELL_OPTION_DESIGNATOR, str(designator))

        self.keyword: Final[CellKeyword] = CellKeyword.IMP
        self.value: Final[types.McnpReal] = importance
        self.importance: Final[types.McnpReal] = importance
        self.designator: Final[types.Designator] = designator

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``Imp`` objects from INP.

        ``from_mcnp`` translates from INP to PyMCNP; it parses INP.

        Parameters:
            source: INP for ``Imp``.

        Returns:
            ``Imp`` object.

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
        if keyword != 'imp':
            raise errors.McnpError(errors.McnpCode.UNRECOGNIZED_KEYWORD, str(keyword))

        tokens.popl()
        designator = types.Designator.from_mcnp(tokens.popl())
        importance = types.McnpReal.from_mcnp(tokens.popl())

        return Imp(importance, designator)