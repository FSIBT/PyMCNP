"""
Contains the ``Nonu`` subclass of ``Data``.
"""

import re
from typing import Final

from ..data import Data
from ..data import DataMnemonic
from ...utils import types, errors, _parser


class Nonu(Data):
    """
    Represents INP nonu data cards.

    ``Nonu`` implements ``Data``.

    Attributes:
        settings: Tuple of fission settings.
    """

    def __init__(self, settings: tuple[types.McnpInteger]):
        """
        Initializes ``Nonu``.

        Parameters:
            settings: Tuple of fission settings.

        Raises:
            McnpError: INVALID_DATUM_PARAMETERS.
        """

        if settings is None:
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS, str(settings))

        for entry in settings:
            if entry is None or not (entry == 0 or entry == 1 or entry == 2):
                raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS, str(settings))

        self.mnemonic: Final[DataMnemonic] = DataMnemonic.NONU
        self.parameters: Final[tuple[any]] = tuple(list(settings))
        self.settings: Final[tuple[types.McnpInteger]] = settings
        self.ident: Final[str] = 'nonu'

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``Nonu`` objects from INP.

        ``from_mcnp`` translates from INP to PyMCNP; it parses INP.

        Parameters:
            source: INP for nonu data cards.

        Returns:
            ``Nonu`` object.

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
        if mnemonic != 'nonu':
            raise errors.McnpError(errors.McnpCode.KEYWORD_DATUM_MNEMONIC)

        tokens.popl()

        settings = [types.McnpInteger.from_mcnp(tokens.popl()) for _ in range(0, len(tokens))]

        data = Nonu(settings)
        data.comment = comments

        return data

    def to_mcnp(self) -> str:
        """
        Generates INP from ``Nonu`` objects.

        ``to_mcnp`` translates from PyMCNP to INP.

        Returns:
            INP for ``Nonu``.
        """

        return _parser.Postprocessor.add_continuation_lines(
            f"{self.mnemonic.to_mcnp()} {" ".join(entry.to_mcnp() for entry in self.settings)}"
        )
