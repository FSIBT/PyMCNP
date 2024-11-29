"""
Contains the ``Pd`` subclass of ``CellOption``.
"""

import re
from typing import Final

from ..cell_option import CellOption
from ..cell_keyword import CellKeyword
from ...utils import types, errors, _parser


class Pd(CellOption):
    """
    Represents INP cell card pd options.

    ``Pd`` implements ``_card.CardOption``.

    Attributes:
        probability: Cell probability of DXTRAN contribution.
        suffix: Cell option suffix
    """

    def __init__(self, probability: types.McnpReal, suffix: types.McnpInteger):
        """
        Initializes ``Pd``.

        Parameters:
            probability: Cell probability of DXTRAN contribution.
            suffix: Cell option suffix

        Raises:
            McnpError: INVALID_CELL_OPTION_VALUE.
            McnpError: INVALID_CELL_OPTION_SUFFIX.
        """

        if probability is None or not (0 <= probability <= 1):
            raise errors.McnpError(errors.McnpCode.INVALID_CELL_OPTION_VALUE, str(probability))
        if suffix is None:
            raise errors.McnpError(errors.McnpCode.INVALID_CELL_OPTION_SUFFIX, str(suffix))

        self.keyword: Final[CellKeyword] = CellKeyword.PD
        self.value: Final[types.McnpReal] = probability
        self.probability: Final[types.McnpReal] = probability
        self.suffix: Final[types.McnpInteger] = suffix

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``Pd`` objects from INP.

        ``from_mcnp`` translates from INP to PyMCNP; it parses INP.

        Parameters:
            source: INP for ``Pd``.

        Returns:
            ``Pd`` object.

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
        if keyword != 'pd':
            raise errors.McnpError(errors.McnpCode.UNRECOGNIZED_KEYWORD, str(keyword))

        suffix = types.McnpInteger.from_mcnp(tokens.popl()[2:])
        probability = types.McnpReal.from_mcnp(tokens.popl())

        return Pd(probability, suffix)
