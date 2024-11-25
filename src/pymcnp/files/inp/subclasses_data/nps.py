"""
Contains the ``Nps`` subclass of ``Data``.
"""

import re
from typing import Final

from ..data import Data
from ..data import DataMnemonic
from ...utils import types, errors, _parser


class Nps(Data):
    """
    Represents INP nps data cards.

    ``Nps`` implements ``Data``.

    Attributes:
        npp: Total number of histories to run.
        npsmg: Number of history with direct source contributions.
    """

    def __init__(self, npp: types.McnpInteger, npsmg: types.McnpInteger):
        """
        Initializes ``Nps``.

        Parameters:
            npp: Total number of histories to run.
            npsmg: Number of history with direct source contributions.

        Raises:
            McnpError: INVALID_DATUM_PARAMETERS.
        """

        if npp is None or not (npp > 0):
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS, str(npp))

        if npsmg is None or not (npsmg > 0):
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS, str(npsmg))

        self.mnemonic: Final[DataMnemonic] = DataMnemonic.NPS
        self.parameters: Final[tuple[any]] = tuple([npp] + [npsmg])
        self.npp: Final[types.McnpInteger] = npp
        self.npsmg: Final[types.McnpInteger] = npsmg
        self.ident: Final[str] = 'nps'

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``Nps`` objects from INP.

        ``from_mcnp`` translates from INP to PyMCNP; it parses INP.

        Parameters:
            source: INP for nps data cards.

        Returns:
            ``Nps`` object.

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
        if mnemonic != 'nps':
            raise errors.McnpError(errors.McnpCode.KEYWORD_DATUM_MNEMONIC)

        tokens.popl()

        npp = types.McnpInteger.from_mcnp(tokens.popl())
        npsmg = types.McnpInteger.from_mcnp(tokens.popl())

        data = Nps(npp, npsmg)
        data.comment = comments

        return data

    def to_mcnp(self) -> str:
        """
        Generates INP from ``Nps`` objects.

        ``to_mcnp`` translates from PyMCNP to INP.

        Returns:
            INP for ``Nps``.
        """

        return _parser.Postprocessor.add_continuation_lines(
            f'{self.mnemonic.to_mcnp()} {self.npp.to_mcnp()} {self.npsmg.to_mcnp()}'
        )
