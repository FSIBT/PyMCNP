"""
Contains the ``Lat`` subclass of ``Data``.
"""

import re
from typing import Final

from ..data import Data
from ..data import DataMnemonic
from ....utils import types, errors, _parser


class Lat(Data):
    """
    Represents INP lat data cards.

    ``Lat`` implements ``Data``.

    Attributes:
        types: Tuple of lattice types.
    """

    def __init__(self, types: tuple[types.McnpInteger]):
        """
        Initializes ``Lat``.

        Parameters:
            types: Tuple of lattice types.

        Raises:
            McnpError: INVALID_DATUM_PARAMETERS.
        """

        if types is None:
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS, str(types))

        for entry in types:
            if entry is None or not (entry == 1 or entry == 2):
                raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS, str(types))

        self.mnemonic: Final[DataMnemonic] = DataMnemonic.LAT
        self.parameters: Final[tuple[any]] = tuple(list(types))
        self.types: Final[tuple[types.McnpInteger]] = types
        self.ident: Final[str] = 'lat'

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``Lat`` objects from INP.

        ``from_mcnp`` translates from INP to PyMCNP; it parses INP.

        Parameters:
            source: INP for lat data cards.

        Returns:
            ``Lat`` object.

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
        if mnemonic != 'lat':
            raise errors.McnpError(errors.McnpCode.KEYWORD_DATUM_MNEMONIC)

        tokens.popl()

        types = [types.McnpInteger.from_mcnp(tokens.popl()) for _ in range(0, len(tokens))]

        data = Lat(types)
        data.comment = comments

        return data

    def to_mcnp(self) -> str:
        """
        Generates INP from ``Lat`` objects.

        ``to_mcnp`` translates from PyMCNP to INP.

        Returns:
            INP for ``Lat``.
        """

        return _parser.Postprocessor.add_continuation_lines(
            f"{self.mnemonic.to_mcnp()} {" ".join(entry.to_mcnp() for entry in self.types)}"
        )
