"""
Contains the ``Leb`` subclass of ``Data``.
"""

import re
from typing import Final

from ..data import Data
from ..data_mnemonic import DataMnemonic
from ...utils import types
from ...utils import errors
from ...utils import _parser


class Leb(Data):
    """
    Represents INP leb data cards.

    ``Leb`` implements ``Data``.

    Attributes:
        yzere: Y0 parameter in level-density formula for Z≤70.
        bzere: B0 parameter in level-density formula for Z≤70.
        yzero: Y0 parameter in level-density formula for Z≥71.
        bzero: B0 parameter in level-density formula for Z≥70.
    """

    def __init__(
        self,
        yzere: types.McnpReal,
        bzere: types.McnpReal,
        yzero: types.McnpReal,
        bzero: types.McnpReal,
    ):
        """
        Initializes ``Leb``.

        Parameters:
            yzere: Y0 parameter in level-density formula for Z≤70.
            bzere: B0 parameter in level-density formula for Z≤70.
            yzero: Y0 parameter in level-density formula for Z≥71.
            bzero: B0 parameter in level-density formula for Z≥70.

        Raises:
            McnpError: INVALID_DATUM_PARAMETERS.
        """

        if yzere is None or not (yzere > 0):
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS, str(yzere))

        if bzere is None or not (bzere > 0):
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS, str(bzere))

        if yzero is None or not (yzero > 0):
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS, str(yzero))

        if bzero is None or not (bzero > 0):
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS, str(bzero))

        self.mnemonic: Final[DataMnemonic] = DataMnemonic.LEB
        self.parameters: Final[tuple[any]] = tuple([yzere] + [bzere] + [yzero] + [bzero])
        self.yzere: Final[types.McnpReal] = yzere
        self.bzere: Final[types.McnpReal] = bzere
        self.yzero: Final[types.McnpReal] = yzero
        self.bzero: Final[types.McnpReal] = bzero
        self.ident: Final[str] = 'leb'

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``Leb`` objects from INP.

        ``from_mcnp`` translates from INP to PyMCNP; it parses INP.

        Parameters:
            source: INP for leb data cards.

        Returns:
            ``Leb`` object.

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
        if mnemonic != 'leb':
            raise errors.McnpError(errors.McnpCode.KEYWORD_DATUM_MNEMONIC)

        tokens.popl()

        yzere = types.McnpReal.from_mcnp(tokens.popl())
        bzere = types.McnpReal.from_mcnp(tokens.popl())
        yzero = types.McnpReal.from_mcnp(tokens.popl())
        bzero = types.McnpReal.from_mcnp(tokens.popl())

        data = Leb(yzere, bzere, yzero, bzero)
        data.comment = comments

        return data

    def to_mcnp(self) -> str:
        """
        Generates INP from ``Leb`` objects.

        ``to_mcnp`` translates from PyMCNP to INP.

        Returns:
            INP for ``Leb``.
        """

        return _parser.Postprocessor.add_continuation_lines(
            f'{self.mnemonic.to_mcnp()} {self.yzere.to_mcnp()} {self.bzere.to_mcnp()} {self.yzero.to_mcnp()} {self.bzero.to_mcnp()}'
        )
