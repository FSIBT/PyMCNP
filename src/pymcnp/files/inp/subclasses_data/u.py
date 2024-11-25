"""
Contains the ``U`` subclass of ``Data``.
"""

import re
from typing import Final

from ..data import Data
from ..data import DataMnemonic
from ...utils import types, errors, _parser


class U(Data):
    """
    Represents INP u data cards.

    ``U`` implements ``Data``.

    Attributes:
        numbers: Tuple of cell numbers.
    """

    def __init__(self, numbers: tuple[types.McnpInteger]):
        """
        Initializes ``U``.

        Parameters:
            numbers: Tuple of cell numbers.

        Raises:
            McnpError: INVALID_DATUM_PARAMETERS.
        """

        if numbers is None:
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS, str(numbers))

        for entry in numbers:
            if entry is None or not (1 <= entry <= 99_999_999):
                raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS, str(numbers))

        self.mnemonic: Final[DataMnemonic] = DataMnemonic.U
        self.parameters: Final[tuple[any]] = tuple(list(numbers))
        self.numbers: Final[tuple[types.McnpInteger]] = numbers
        self.ident: Final[str] = 'u'

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``U`` objects from INP.

        ``from_mcnp`` translates from INP to PyMCNP; it parses INP.

        Parameters:
            source: INP for u data cards.

        Returns:
            ``U`` object.

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
        if mnemonic != 'u':
            raise errors.McnpError(errors.McnpCode.KEYWORD_DATUM_MNEMONIC)

        tokens.popl()

        numbers = [types.McnpInteger.from_mcnp(tokens.popl()) for _ in range(0, len(tokens))]

        data = U(numbers)
        data.comment = comments

        return data

    def to_mcnp(self) -> str:
        """
        Generates INP from ``U`` objects.

        ``to_mcnp`` translates from PyMCNP to INP.

        Returns:
            INP for ``U``.
        """

        return _parser.Postprocessor.add_continuation_lines(
            f"{self.mnemonic.to_mcnp()} {" ".join(entry.to_mcnp() for entry in self.numbers)}"
        )
