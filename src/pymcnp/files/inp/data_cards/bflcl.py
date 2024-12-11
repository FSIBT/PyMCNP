"""
Contains the ``Bflcl`` subclass of ``Data``.
"""

import re
from typing import Final

from ..data import Data
from ..data_mnemonic import DataMnemonic
from ...utils import types
from ...utils import errors
from ...utils import _parser


class Bflcl(Data):
    """
    Represents INP bflcl data cards.

    ``Bflcl`` implements ``Data``.

    Attributes:
        numbers: Tuple of BFLD map numbers.
    """

    def __init__(self, numbers: tuple[types.McnpInteger]):
        """
        Initializes ``Bflcl``.

        Parameters:
            numbers: Tuple of BFLD map numbers.

        Raises:
            McnpError: INVALID_DATUM_PARAMETERS.
        """

        if numbers is None:
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS, str(numbers))

        for entry in numbers:
            if entry is None:
                raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS, str(numbers))

        self.mnemonic: Final[DataMnemonic] = DataMnemonic.BFLCL
        self.parameters: Final[tuple[any]] = tuple(list(numbers))
        self.numbers: Final[tuple[types.McnpInteger]] = numbers
        self.ident: Final[str] = 'bflcl'

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``Bflcl`` objects from INP.

        ``from_mcnp`` translates from INP to PyMCNP; it parses INP.

        Parameters:
            source: INP for bflcl data cards.

        Returns:
            ``Bflcl`` object.

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
        if mnemonic != 'bflcl':
            raise errors.McnpError(errors.McnpCode.KEYWORD_DATUM_MNEMONIC)

        tokens.popl()

        numbers = [types.McnpInteger.from_mcnp(tokens.popl()) for _ in range(0, len(tokens))]

        data = Bflcl(numbers)
        data.comment = comments

        return data

    def to_mcnp(self) -> str:
        """
        Generates INP from ``Bflcl`` objects.

        ``to_mcnp`` translates from PyMCNP to INP.

        Returns:
            INP for ``Bflcl``.
        """

        return _parser.Postprocessor.add_continuation_lines(
            f"{self.mnemonic.to_mcnp()} {' '.join(entry.to_mcnp() for entry in self.numbers)}"
        )
