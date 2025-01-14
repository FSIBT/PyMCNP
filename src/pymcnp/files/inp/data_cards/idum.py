"""
Contains the ``Idum`` subclass of ``Data``.
"""

import re
from typing import Final

from ..data import Data
from ..data_mnemonic import DataMnemonic
from ...utils import types
from ...utils import errors
from ...utils import _parser


class Idum(Data):
    """
    Represents INP idum data cards.

    ``Idum`` implements ``Data``.

    Attributes:
        intergers: Integer array.
    """

    def __init__(self, intergers: tuple[types.McnpInteger]):
        """
        Initializes ``Idum``.

        Parameters:
            intergers: Integer array.

        Raises:
            McnpError: INVALID_DATUM_PARAMETERS.
        """

        if intergers is None:
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS, str(intergers))

        for entry in intergers:
            if entry is None:
                raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS, str(intergers))

        self.mnemonic: Final[DataMnemonic] = DataMnemonic.IDUM
        self.parameters: Final[tuple[any]] = tuple(list(intergers))
        self.intergers: Final[tuple[types.McnpInteger]] = intergers
        self.ident: Final[str] = 'idum'

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``Idum`` objects from INP.

        ``from_mcnp`` translates from INP to PyMCNP; it parses INP.

        Parameters:
            source: INP for idum data cards.

        Returns:
            ``Idum`` object.

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
        if mnemonic != 'idum':
            raise errors.McnpError(errors.McnpCode.KEYWORD_DATUM_MNEMONIC)

        tokens.popl()

        intergers = [types.McnpInteger.from_mcnp(tokens.popl()) for _ in range(0, len(tokens))]

        data = Idum(intergers)
        data.comment = comments

        return data

    def to_mcnp(self) -> str:
        """
        Generates INP from ``Idum`` objects.

        ``to_mcnp`` translates from PyMCNP to INP.

        Returns:
            INP for ``Idum``.
        """

        return _parser.Postprocessor.add_continuation_lines(
            f"{self.mnemonic.to_mcnp()} {' '.join(entry.to_mcnp() for entry in self.intergers)}"
        )
