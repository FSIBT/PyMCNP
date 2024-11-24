"""
Contains the ``Tmp`` subclass of ``CellOption``."""

import re
from typing import Final

from ..cell import CellOption, CellKeyword
from ....utils import types, errors, _parser


class Tmp(CellOption):
    """
    Represents INP cell card tmp options.

    ``Tmp`` implements ``_card.CardOption``.

    Attributes:
        temperature: Cell temperature at suffix time index.
        suffix: Cell option suffix
    """

    def __init__(self, temperature: types.McnpReal, suffix: types.McnpInteger):
        """
        Initializes ``Tmp``.

        Parameters:
            temperature: Cell temperature at suffix time index.
            suffix: Cell option suffix

        Raises:
            McnpError: INVALID_CELL_OPTION_VALUE.
            McnpError: INVALID_CELL_OPTION_SUFFIX.
        """

        if temperature is None or not (temperature > 0):
            raise errors.McnpError(errors.McnpCode.INVALID_CELL_OPTION_VALUE, str(temperature))
        if suffix is None:
            raise errors.McnpError(errors.McnpCode.INVALID_CELL_OPTION_SUFFIX, str(suffix))

        self.keyword: Final[CellKeyword] = CellKeyword.TMP
        self.value: Final[types.McnpReal] = temperature
        self.temperature: Final[types.McnpReal] = temperature
        self.suffix: Final[types.McnpInteger] = suffix

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``Tmp`` objects from INP.

        ``from_mcnp`` translates from INP to PyMCNP; it parses INP.

        Parameters:
            source: INP for ``Tmp``.

        Returns:
            ``Tmp`` object.

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
        if keyword != 'tmp':
            raise errors.McnpError(errors.McnpCode.UNRECOGNIZED_KEYWORD, str(keyword))

        suffix = types.McnpInteger.from_mcnp(tokens.popl()[3:])
        temperature = types.McnpInteger.from_mcnp(tokens.popl())

        return Tmp(temperature, suffix)
