"""
Contains the ``Dxc`` subclass of ``CellOption``.
"""

import re
from typing import Final

from ..cell_option import CellOption
from ..cell_keyword import CellKeyword
from ...utils import types
from ...utils import errors
from ...utils import _parser


class Dxc(CellOption):
    """
    Represents INP cell card dxc options.

    ``Dxc`` implements ``_card.CardOption``.

    Attributes:
        probability: Cell probability of DXTRAN contribution.
        suffix: Cell option suffix
        designator: Cell option particle designator
    """

    def __init__(
        self, probability: types.McnpReal, suffix: types.McnpInteger, designator: types.Designator
    ):
        """
        Initializes ``Dxc``.

        Parameters:
            probability: Cell probability of DXTRAN contribution.
            suffix: Cell option suffix
            designator: Cell option particle designator

        Raises:
            McnpError: INVALID_CELL_OPTION_VALUE.
            McnpError: INVALID_CELL_OPTION_SUFFIX.
            McnpError: INVALID_CELL_OPTION_DESIGNATOR.
        """

        if probability is None or not (0 <= probability <= 1):
            raise errors.McnpError(errors.McnpCode.INVALID_CELL_OPTION_VALUE, str(probability))
        if suffix is None:
            raise errors.McnpError(errors.McnpCode.INVALID_CELL_OPTION_SUFFIX, str(suffix))
        if designator is None:
            raise errors.McnpError(errors.McnpCode.INVALID_CELL_OPTION_DESIGNATOR, str(designator))

        self.keyword: Final[CellKeyword] = CellKeyword.DXC
        self.value: Final[types.McnpReal] = probability
        self.probability: Final[types.McnpReal] = probability
        self.suffix: Final[types.McnpInteger] = suffix
        self.designator: Final[types.Designator] = designator

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``Dxc`` objects from INP.

        ``from_mcnp`` translates from INP to PyMCNP; it parses INP.

        Parameters:
            source: INP for ``Dxc``.

        Returns:
            ``Dxc`` object.

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
        if keyword != 'dxc':
            raise errors.McnpError(errors.McnpCode.UNRECOGNIZED_KEYWORD, str(keyword))

        suffix = types.McnpInteger.from_mcnp(tokens.popl()[3:])
        designator = types.Designator.from_mcnp(tokens.popl())
        probability = types.McnpReal.from_mcnp(tokens.popl())

        return Dxc(probability, suffix, designator)
