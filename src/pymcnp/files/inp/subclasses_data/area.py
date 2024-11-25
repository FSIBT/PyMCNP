"""
Contains the ``Area`` subclass of ``Data``.
"""

import re
from typing import Final

from ..data import Data
from ..data import DataMnemonic
from ...utils import types, errors, _parser


class Area(Data):
    """
    Represents INP area data cards.

    ``Area`` implements ``Data``.

    Attributes:
        areas: Tuple of surface areas.
    """

    def __init__(self, areas: tuple[types.McnpReal]):
        """
        Initializes ``Area``.

        Parameters:
            areas: Tuple of surface areas.

        Raises:
            McnpError: INVALID_DATUM_PARAMETERS.
        """

        if areas is None:
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS, str(areas))

        for entry in areas:
            if entry is None:
                raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS, str(areas))

        self.mnemonic: Final[DataMnemonic] = DataMnemonic.AREA
        self.parameters: Final[tuple[any]] = tuple(list(areas))
        self.areas: Final[tuple[types.McnpReal]] = areas
        self.ident: Final[str] = 'area'

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``Area`` objects from INP.

        ``from_mcnp`` translates from INP to PyMCNP; it parses INP.

        Parameters:
            source: INP for area data cards.

        Returns:
            ``Area`` object.

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
        if mnemonic != 'area':
            raise errors.McnpError(errors.McnpCode.KEYWORD_DATUM_MNEMONIC)

        tokens.popl()

        areas = [types.McnpReal.from_mcnp(tokens.popl()) for _ in range(0, len(tokens))]

        data = Area(areas)
        data.comment = comments

        return data

    def to_mcnp(self) -> str:
        """
        Generates INP from ``Area`` objects.

        ``to_mcnp`` translates from PyMCNP to INP.

        Returns:
            INP for ``Area``.
        """

        return _parser.Postprocessor.add_continuation_lines(
            f"{self.mnemonic.to_mcnp()} {" ".join(entry.to_mcnp() for entry in self.areas)}"
        )
