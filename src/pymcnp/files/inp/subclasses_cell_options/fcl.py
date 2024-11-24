"""
Contains the ``Fcl`` subclass of ``CellOption``."""

import re
from typing import Final

from ..cell import CellOption, CellKeyword
from ....utils import types, errors, _parser


class Fcl(CellOption):
    """
    Represents INP cell card fcl options.

    ``Fcl`` implements ``_card.CardOption``.

    Attributes:
        control: Cell forced-collision control.
        designator: Cell option particle designator
    """

    def __init__(self, control: types.McnpReal, designator: types.Designator):
        """
        Initializes ``Fcl``.

        Parameters:
            control: Cell forced-collision control.
            designator: Cell option particle designator

        Raises:
            McnpError: INVALID_CELL_OPTION_VALUE.
            McnpError: INVALID_CELL_OPTION_DESIGNATOR.
        """

        if control is None or not (-1 <= control <= 1):
            raise errors.McnpError(errors.McnpCode.INVALID_CELL_OPTION_VALUE, str(control))
        if designator is None:
            raise errors.McnpError(errors.McnpCode.INVALID_CELL_OPTION_DESIGNATOR, str(designator))

        self.keyword: Final[CellKeyword] = CellKeyword.FCL
        self.value: Final[types.McnpReal] = control
        self.control: Final[types.McnpReal] = control
        self.designator: Final[types.Designator] = designator

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``Fcl`` objects from INP.

        ``from_mcnp`` translates from INP to PyMCNP; it parses INP.

        Parameters:
            source: INP for ``Fcl``.

        Returns:
            ``Fcl`` object.

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
        if keyword != 'fcl':
            raise errors.McnpError(errors.McnpCode.UNRECOGNIZED_KEYWORD, str(keyword))

        tokens.popl()
        designator = types.Designator.from_mcnp(tokens.popl())
        control = types.Designator.from_mcnp(tokens.popl())

        return Fcl(control, designator)
