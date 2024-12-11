"""
Contains the ``Lat`` subclass of ``CellOption``.
"""

import re
from typing import Final

from ..cell_option import CellOption
from ..cell_keyword import CellKeyword
from ...utils import types
from ...utils import errors
from ...utils import _parser


class Lat(CellOption):
    """
    Represents INP cell card lat options.

    ``Lat`` implements ``_card.CardOption``.

    Attributes:
        shape: Cell lattice shape.
    """

    def __init__(self, shape: types.McnpInteger):
        """
        Initializes ``Lat``.

        Parameters:
            shape: Cell lattice shape.

        Raises:
            McnpError: INVALID_CELL_OPTION_VALUE.
        """

        if shape is None or shape.value not in {1, 2}:
            raise errors.McnpError(errors.McnpCode.INVALID_CELL_OPTION_VALUE, str(shape))

        self.keyword: Final[CellKeyword] = CellKeyword.LAT
        self.value: Final[types.McnpInteger] = shape
        self.shape: Final[types.McnpInteger] = shape

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``Lat`` objects from INP.

        ``from_mcnp`` translates from INP to PyMCNP; it parses INP.

        Parameters:
            source: INP for ``Lat``.

        Returns:
            ``Lat`` object.

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
        if keyword != 'lat':
            raise errors.McnpError(errors.McnpCode.UNRECOGNIZED_KEYWORD, str(keyword))

        tokens.popl()
        shape = types.McnpInteger.from_mcnp(tokens.popl())

        return Lat(shape)
