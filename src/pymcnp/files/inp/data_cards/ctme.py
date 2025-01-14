"""
Contains the ``Ctme`` subclass of ``Data``.
"""

import re
from typing import Final

from ..data import Data
from ..data_mnemonic import DataMnemonic
from ...utils import types
from ...utils import errors
from ...utils import _parser


class Ctme(Data):
    """
    Represents INP ctme data cards.

    ``Ctme`` implements ``Data``.

    Attributes:
        tme: maximum amount of minutes for Monte Carlo calculation.
    """

    def __init__(self, tme: types.McnpInteger):
        """
        Initializes ``Ctme``.

        Parameters:
            tme: maximum amount of minutes for Monte Carlo calculation.

        Raises:
            McnpError: INVALID_DATUM_PARAMETERS.
        """

        if tme is None or not (tme >= 0):
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS, str(tme))

        self.mnemonic: Final[DataMnemonic] = DataMnemonic.CTME
        self.parameters: Final[tuple[any]] = tuple([tme])
        self.tme: Final[types.McnpInteger] = tme
        self.ident: Final[str] = 'ctme'

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``Ctme`` objects from INP.

        ``from_mcnp`` translates from INP to PyMCNP; it parses INP.

        Parameters:
            source: INP for ctme data cards.

        Returns:
            ``Ctme`` object.

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
        if mnemonic != 'ctme':
            raise errors.McnpError(errors.McnpCode.KEYWORD_DATUM_MNEMONIC)

        tokens.popl()

        tme = types.McnpInteger.from_mcnp(tokens.popl())

        data = Ctme(tme)
        data.comment = comments

        return data

    def to_mcnp(self) -> str:
        """
        Generates INP from ``Ctme`` objects.

        ``to_mcnp`` translates from PyMCNP to INP.

        Returns:
            INP for ``Ctme``.
        """

        return _parser.Postprocessor.add_continuation_lines(
            f'{self.mnemonic.to_mcnp()} {self.tme.to_mcnp()}'
        )
