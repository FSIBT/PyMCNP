"""
Contains the ``Rdum`` subclass of ``Data``.
"""

import re
from typing import Final

from ..data import Data
from ..data_mnemonic import DataMnemonic
from ...utils import types
from ...utils import errors
from ...utils import _parser


class Rdum(Data):
    """
    Represents INP rdum data cards.

    ``Rdum`` implements ``Data``.

    Attributes:
        floats: Floating point array.
    """

    def __init__(self, floats: tuple[types.McnpReal]):
        """
        Initializes ``Rdum``.

        Parameters:
            floats: Floating point array.

        Raises:
            McnpError: INVALID_DATUM_PARAMETERS.
        """

        if floats is None:
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS, str(floats))

        for entry in floats:
            if entry is None:
                raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS, str(floats))

        self.mnemonic: Final[DataMnemonic] = DataMnemonic.RDUM
        self.parameters: Final[tuple[any]] = tuple(list(floats))
        self.floats: Final[tuple[types.McnpReal]] = floats
        self.ident: Final[str] = 'rdum'

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``Rdum`` objects from INP.

        ``from_mcnp`` translates from INP to PyMCNP; it parses INP.

        Parameters:
            source: INP for rdum data cards.

        Returns:
            ``Rdum`` object.

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
        if mnemonic != 'rdum':
            raise errors.McnpError(errors.McnpCode.KEYWORD_DATUM_MNEMONIC)

        tokens.popl()

        floats = [types.McnpReal.from_mcnp(tokens.popl()) for _ in range(0, len(tokens))]

        data = Rdum(floats)
        data.comment = comments

        return data

    def to_mcnp(self) -> str:
        """
        Generates INP from ``Rdum`` objects.

        ``to_mcnp`` translates from PyMCNP to INP.

        Returns:
            INP for ``Rdum``.
        """

        return _parser.Postprocessor.add_continuation_lines(
            f"{self.mnemonic.to_mcnp()} {' '.join(entry.to_mcnp() for entry in self.floats)}"
        )
