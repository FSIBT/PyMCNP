"""
Contains the ``Nonu`` subclass of ``CellOption``.
"""

import re
from typing import Final

from ..cell_option import CellOption, CellKeyword
from ...utils import types, errors, _parser


class Nonu(CellOption):
    """
    Represents INP cell card nonu options.

    ``Nonu`` implements ``_card.CardOption``.

    Attributes:
        setting: Cell fission setting.
    """

    def __init__(self, setting: types.McnpInteger):
        """
        Initializes ``Nonu``.

        Parameters:
            setting: Cell fission setting.

        Raises:
            McnpError: INVALID_CELL_OPTION_VALUE.
        """

        if setting is None or setting.value not in {0, 1, 2}:
            raise errors.McnpError(errors.McnpCode.INVALID_CELL_OPTION_VALUE, str(setting))

        self.keyword: Final[CellKeyword] = CellKeyword.NONU
        self.value: Final[types.McnpInteger] = setting
        self.setting: Final[types.McnpInteger] = setting

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``Nonu`` objects from INP.

        ``from_mcnp`` translates from INP to PyMCNP; it parses INP.

        Parameters:
            source: INP for ``Nonu``.

        Returns:
            ``Nonu`` object.

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
        if keyword != 'nonu':
            raise errors.McnpError(errors.McnpCode.UNRECOGNIZED_KEYWORD, str(keyword))

        tokens.popl()
        setting = types.McnpInteger.from_mcnp(tokens.popl())

        return Nonu(setting)
