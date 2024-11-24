"""
Contains the ``Cosy`` subclass of ``Data``.
"""

import re
from typing import Final

from ..data import Data
from ..data import DataMnemonic
from ....utils import types, errors, _parser


class Cosy(Data):
    """
    Represents INP cosy data cards.

    ``Cosy`` implements ``Data``.

    Attributes:
        numbers: Tuple of COSY map numbers.
    """

    def __init__(self, numbers: tuple[types.McnpInteger]):
        """
        Initializes ``Cosy``.

        Parameters:
            numbers: Tuple of COSY map numbers.

        Raises:
            McnpError: INVALID_DATUM_PARAMETERS.
        """

        if numbers is None:
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS, str(numbers))

        for entry in numbers:
            if entry is None:
                raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS, str(numbers))

        self.mnemonic: Final[DataMnemonic] = DataMnemonic.COSY
        self.parameters: Final[tuple[any]] = tuple(list(numbers))
        self.numbers: Final[tuple[types.McnpInteger]] = numbers
        self.ident: Final[str] = 'cosy'

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``Cosy`` objects from INP.

        ``from_mcnp`` translates from INP to PyMCNP; it parses INP.

        Parameters:
            source: INP for cosy data cards.

        Returns:
            ``Cosy`` object.

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
        if mnemonic != 'cosy':
            raise errors.McnpError(errors.McnpCode.KEYWORD_DATUM_MNEMONIC)

        tokens.popl()

        numbers = [types.McnpInteger.from_mcnp(tokens.popl()) for _ in range(0, len(tokens))]

        data = Cosy(numbers)
        data.comment = comments

        return data

    def to_mcnp(self) -> str:
        """
        Generates INP from ``Cosy`` objects.

        ``to_mcnp`` translates from PyMCNP to INP.

        Returns:
            INP for ``Cosy``.
        """

        return _parser.Postprocessor.add_continuation_lines(
            f"{self.mnemonic.to_mcnp()} {" ".join(entry.to_mcnp() for entry in self.numbers)}"
        )
