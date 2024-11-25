"""
Contains the ``Unc`` subclass of ``CellOption``.
"""

import re
from typing import Final

from ..cell_option import CellOption, CellKeyword
from ...utils import types, errors, _parser


class Unc(CellOption):
    """
    Represents INP cell card unc options.

    ``Unc`` implements ``_card.CardOption``.

    Attributes:
        setting: Cell uncollided secondaries setting.
        designator: Cell option particle designator
    """

    def __init__(self, setting: types.McnpInteger, designator: types.Designator):
        """
        Initializes ``Unc``.

        Parameters:
            setting: Cell uncollided secondaries setting.
            designator: Cell option particle designator

        Raises:
            McnpError: INVALID_CELL_OPTION_VALUE.
            McnpError: INVALID_CELL_OPTION_DESIGNATOR.
        """

        if setting is None or setting not in {0, 1}:
            raise errors.McnpError(errors.McnpCode.INVALID_CELL_OPTION_VALUE, str(setting))
        if designator is None:
            raise errors.McnpError(errors.McnpCode.INVALID_CELL_OPTION_DESIGNATOR, str(designator))

        self.keyword: Final[CellKeyword] = CellKeyword.UNC
        self.value: Final[types.McnpInteger] = setting
        self.setting: Final[types.McnpInteger] = setting
        self.designator: Final[types.Designator] = designator

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``Unc`` objects from INP.

        ``from_mcnp`` translates from INP to PyMCNP; it parses INP.

        Parameters:
            source: INP for ``Unc``.

        Returns:
            ``Unc`` object.

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
        if keyword != 'unc':
            raise errors.McnpError(errors.McnpCode.UNRECOGNIZED_KEYWORD, str(keyword))

        tokens.popl()
        designator = types.Designator.from_mcnp(tokens.popl())
        setting = types.McnpInteger.from_mcnp(tokens.popl())

        return Unc(setting, designator)
