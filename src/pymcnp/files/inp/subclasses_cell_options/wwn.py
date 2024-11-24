"""
Contains the ``Wwn`` subclass of ``CellOption``."""

import re
from typing import Final

from ..cell import CellOption, CellKeyword
from ....utils import types, errors, _parser


class Wwn(CellOption):
    """
    Represents INP cell card wwn options.

    ``Wwn`` implements ``_card.CardOption``.

    Attributes:
        bound: Cell weight-window space, time, or energy lower bound.
        suffix: Cell option suffix
        designator: Cell option particle designator
    """

    def __init__(
        self, bound: types.McnpReal, suffix: types.McnpInteger, designator: types.Designator
    ):
        """
        Initializes ``Wwn``.

        Parameters:
            bound: Cell weight-window space, time, or energy lower bound.
            suffix: Cell option suffix
            designator: Cell option particle designator

        Raises:
            McnpError: INVALID_CELL_OPTION_VALUE.
            McnpError: INVALID_CELL_OPTION_SUFFIX.
            McnpError: INVALID_CELL_OPTION_DESIGNATOR.
        """

        if bound is None or not (bound == -1 or bound >= 0):
            raise errors.McnpError(errors.McnpCode.INVALID_CELL_OPTION_VALUE, str(bound))
        if suffix is None:
            raise errors.McnpError(errors.McnpCode.INVALID_CELL_OPTION_SUFFIX, str(suffix))
        if designator is None:
            raise errors.McnpError(errors.McnpCode.INVALID_CELL_OPTION_DESIGNATOR, str(designator))

        self.keyword: Final[CellKeyword] = CellKeyword.WWN
        self.value: Final[types.McnpReal] = bound
        self.bound: Final[types.McnpReal] = bound
        self.suffix: Final[types.McnpInteger] = suffix
        self.designator: Final[types.Designator] = designator

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``Wwn`` objects from INP.

        ``from_mcnp`` translates from INP to PyMCNP; it parses INP.

        Parameters:
            source: INP for ``Wwn``.

        Returns:
            ``Wwn`` object.

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
        if keyword != 'wwn':
            raise errors.McnpError(errors.McnpCode.UNRECOGNIZED_KEYWORD, str(keyword))

        suffix = types.McnpInteger.from_mcnp(tokens.popl()[3:])
        designator = types.Designator.from_mcnp(tokens.popl())
        bound = types.Designator.from_mcnp(tokens.popl())

        return Wwn(bound, suffix, designator)
