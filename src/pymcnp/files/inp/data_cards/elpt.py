"""
Contains the ``Elpt`` subclass of ``Data``.
"""

import re
from typing import Final

from ..data import Data
from ..data_mnemonic import DataMnemonic
from ...utils import types, errors, _parser


class Elpt(Data):
    """
    Represents INP elpt data cards.

    ``Elpt`` implements ``Data``.

    Attributes:
        cutoffs: Tuple of cell lower energy cutoffs.
    """

    def __init__(self, cutoffs: tuple[types.McnpReal]):
        """
        Initializes ``Elpt``.

        Parameters:
            cutoffs: Tuple of cell lower energy cutoffs.

        Raises:
            McnpError: INVALID_DATUM_PARAMETERS.
        """

        if cutoffs is None:
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS, str(cutoffs))

        for entry in cutoffs:
            if entry is None:
                raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS, str(cutoffs))

        self.mnemonic: Final[DataMnemonic] = DataMnemonic.ELPT
        self.parameters: Final[tuple[any]] = tuple(list(cutoffs))
        self.cutoffs: Final[tuple[types.McnpReal]] = cutoffs
        self.ident: Final[str] = 'elpt'

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``Elpt`` objects from INP.

        ``from_mcnp`` translates from INP to PyMCNP; it parses INP.

        Parameters:
            source: INP for elpt data cards.

        Returns:
            ``Elpt`` object.

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
        if mnemonic != 'elpt':
            raise errors.McnpError(errors.McnpCode.KEYWORD_DATUM_MNEMONIC)

        tokens.popl()

        cutoffs = [types.McnpReal.from_mcnp(tokens.popl()) for _ in range(0, len(tokens))]

        data = Elpt(cutoffs)
        data.comment = comments

        return data

    def to_mcnp(self) -> str:
        """
        Generates INP from ``Elpt`` objects.

        ``to_mcnp`` translates from PyMCNP to INP.

        Returns:
            INP for ``Elpt``.
        """

        return _parser.Postprocessor.add_continuation_lines(
            f"{self.mnemonic.to_mcnp()} {' '.join(entry.to_mcnp() for entry in self.cutoffs)}"
        )
