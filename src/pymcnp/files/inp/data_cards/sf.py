"""
Contains the ``Sf`` subclass of ``Data``.
"""

import re
from typing import Final

from ..data import Data
from ..data_mnemonic import DataMnemonic
from ...utils import types
from ...utils import errors
from ...utils import _parser


class Sf(Data):
    """
    Represents INP sf data cards.

    ``Sf`` implements ``Data``.

    Attributes:
        numbers: Tallies for problem surface numbers to flag.
        suffix: Data card suffix.
    """

    def __init__(self, numbers: tuple[types.McnpInteger], suffix: types.McnpInteger):
        """
        Initializes ``Sf``.

        Parameters:
            numbers: Tallies for problem surface numbers to flag.
            suffix: Data card suffix.

        Raises:
            McnpError: INVALID_DATUM_PARAMETERS.
        """

        if numbers is None:
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS, str(numbers))

        for entry in numbers:
            if entry is None or not (0 <= entry <= 99_999_999):
                raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS, str(numbers))

        if suffix is None or not (suffix <= 99_999_999):
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS, str(suffix))

        self.mnemonic: Final[DataMnemonic] = DataMnemonic.SF
        self.parameters: Final[tuple[any]] = tuple(list(numbers) + [suffix])
        self.numbers: Final[tuple[types.McnpInteger]] = numbers
        self.suffix: Final[types.McnpInteger] = suffix
        self.ident: Final[str] = f'sf{self.suffix}'

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``Sf`` objects from INP.

        ``from_mcnp`` translates from INP to PyMCNP; it parses INP.

        Parameters:
            source: INP for sf data cards.

        Returns:
            ``Sf`` object.

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
        if mnemonic != 'sf':
            raise errors.McnpError(errors.McnpCode.KEYWORD_DATUM_MNEMONIC)

        suffix = types.McnpInteger.from_mcnp(tokens.popl()[2:])

        numbers = [types.McnpInteger.from_mcnp(tokens.popl()) for _ in range(0, len(tokens))]

        data = Sf(numbers, suffix)
        data.comment = comments

        return data

    def to_mcnp(self) -> str:
        """
        Generates INP from ``Sf`` objects.

        ``to_mcnp`` translates from PyMCNP to INP.

        Returns:
            INP for ``Sf``.
        """

        return _parser.Postprocessor.add_continuation_lines(
            f"{self.mnemonic.to_mcnp()}{self.suffix.to_mcnp()} {' '.join(entry.to_mcnp() for entry in self.numbers)}"
        )
