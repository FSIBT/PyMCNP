"""
Contains the ``Pwt`` subclass of ``Data``.
"""

import re
from typing import Final

from ..data import Data
from ..data_mnemonic import DataMnemonic
from ...utils import types
from ...utils import errors
from ...utils import _parser


class Pwt(Data):
    """
    Represents INP pwt data cards.

    ``Pwt`` implements ``Data``.

    Attributes:
        weights: Relative threshold weight of photons produced at neutron collisions in cell.
    """

    def __init__(self, weights: tuple[types.McnpReal]):
        """
        Initializes ``Pwt``.

        Parameters:
            weights: Relative threshold weight of photons produced at neutron collisions in cell.

        Raises:
            McnpError: INVALID_DATUM_PARAMETERS.
        """

        if weights is None:
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS, str(weights))

        for entry in weights:
            if entry is None:
                raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS, str(weights))

        self.mnemonic: Final[DataMnemonic] = DataMnemonic.PWT
        self.parameters: Final[tuple[any]] = tuple(list(weights))
        self.weights: Final[tuple[types.McnpReal]] = weights
        self.ident: Final[str] = 'pwt'

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``Pwt`` objects from INP.

        ``from_mcnp`` translates from INP to PyMCNP; it parses INP.

        Parameters:
            source: INP for pwt data cards.

        Returns:
            ``Pwt`` object.

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
        if mnemonic != 'pwt':
            raise errors.McnpError(errors.McnpCode.KEYWORD_DATUM_MNEMONIC)

        tokens.popl()

        weights = [types.McnpReal.from_mcnp(tokens.popl()) for _ in range(0, len(tokens))]

        data = Pwt(weights)
        data.comment = comments

        return data

    def to_mcnp(self) -> str:
        """
        Generates INP from ``Pwt`` objects.

        ``to_mcnp`` translates from PyMCNP to INP.

        Returns:
            INP for ``Pwt``.
        """

        return _parser.Postprocessor.add_continuation_lines(
            f"{self.mnemonic.to_mcnp()} {' '.join(entry.to_mcnp() for entry in self.weights)}"
        )
