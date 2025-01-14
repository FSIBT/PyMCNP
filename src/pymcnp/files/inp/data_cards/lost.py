"""
Contains the ``Lost`` subclass of ``Data``.
"""

import re
from typing import Final

from ..data import Data
from ..data_mnemonic import DataMnemonic
from ...utils import types
from ...utils import errors
from ...utils import _parser


class Lost(Data):
    """
    Represents INP lost data cards.

    ``Lost`` implements ``Data``.

    Attributes:
        lost1: Number of particles which can be lost before job termination.
        lost2: Maximum number of debug prints for lost particles..
    """

    def __init__(self, lost1: types.McnpInteger, lost2: types.McnpInteger):
        """
        Initializes ``Lost``.

        Parameters:
            lost1: Number of particles which can be lost before job termination.
            lost2: Maximum number of debug prints for lost particles..

        Raises:
            McnpError: INVALID_DATUM_PARAMETERS.
        """

        if lost1 is None or not (lost1 >= 0):
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS, str(lost1))

        if lost2 is None or not (lost2 >= 0):
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS, str(lost2))

        self.mnemonic: Final[DataMnemonic] = DataMnemonic.LOST
        self.parameters: Final[tuple[any]] = tuple([lost1] + [lost2])
        self.lost1: Final[types.McnpInteger] = lost1
        self.lost2: Final[types.McnpInteger] = lost2
        self.ident: Final[str] = 'lost'

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``Lost`` objects from INP.

        ``from_mcnp`` translates from INP to PyMCNP; it parses INP.

        Parameters:
            source: INP for lost data cards.

        Returns:
            ``Lost`` object.

        Raises:
            McnpError: EXPECTED_TOKEN, UNEXPECTED_TOKEN, KEYWORD_DATUM_MNEMONIC.
        """

        source = _parser.Preprocessor.process_inp(source)
        source, comments = _parser.Preprocessor.process_inp_comments(source)
        tokens = _parser.Parser(
            re.split(r' |:|=', source),
            errors.McnpError(errors.McnpCode.EXPECTED_TOKEN, source),
        )

        mnemonic = re.search(r'^[a-zA-Z*]+', tokens.peekl())
        mnemonic = mnemonic[0] if mnemonic else ''
        if mnemonic != 'lost':
            raise errors.McnpError(errors.McnpCode.KEYWORD_DATUM_MNEMONIC)

        tokens.popl()

        lost1 = types.McnpInteger.from_mcnp(tokens.popl())
        lost2 = types.McnpInteger.from_mcnp(tokens.popl())

        data = Lost(lost1, lost2)
        data.comment = comments

        return data

    def to_mcnp(self) -> str:
        """
        Generates INP from ``Lost`` objects.

        ``to_mcnp`` translates from PyMCNP to INP.

        Returns:
            INP for ``Lost``.
        """

        return _parser.Postprocessor.add_continuation_lines(
            f'{self.mnemonic.to_mcnp()} {self.lost1.to_mcnp()} {self.lost2.to_mcnp()}'
        )
