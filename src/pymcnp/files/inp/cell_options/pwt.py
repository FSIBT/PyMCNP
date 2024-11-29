"""
Contains the ``Pwt`` subclass of ``CellOption``.
"""

import re
from typing import Final

from ..cell_option import CellOption
from ..cell_keyword import CellKeyword
from ...utils import types, errors, _parser


class Pwt(CellOption):
    """
    Represents INP cell card pwt options.

    ``Pwt`` implements ``_card.CardOption``.

    Attributes:
        weight: Cell weight of photons produced at neutron collisions
    """

    def __init__(self, weight: types.McnpReal):
        """
        Initializes ``Pwt``.

        Parameters:
            weight: Cell weight of photons produced at neutron collisions

        Raises:
            McnpError: INVALID_CELL_OPTION_VALUE.
        """

        if weight is None:
            raise errors.McnpError(errors.McnpCode.INVALID_CELL_OPTION_VALUE, str(weight))

        self.keyword: Final[CellKeyword] = CellKeyword.PWT
        self.value: Final[types.McnpReal] = weight
        self.weight: Final[types.McnpReal] = weight

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``Pwt`` objects from INP.

        ``from_mcnp`` translates from INP to PyMCNP; it parses INP.

        Parameters:
            source: INP for ``Pwt``.

        Returns:
            ``Pwt`` object.

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
        if keyword != 'pwt':
            raise errors.McnpError(errors.McnpCode.UNRECOGNIZED_KEYWORD, str(keyword))

        tokens.popl()
        weight = types.McnpReal.from_mcnp(tokens.popl())

        return Pwt(weight)
