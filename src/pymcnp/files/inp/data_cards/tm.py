"""
Contains the ``Tm`` subclass of ``Data``.
"""

import re
from typing import Final

from ..data import Data
from ..data_mnemonic import DataMnemonic
from ...utils import types
from ...utils import errors
from ...utils import _parser


class Tm(Data):
    """
    Represents INP tm data cards.

    ``Tm`` implements ``Data``.

    Attributes:
        multipliers: Time bin multiplier to apply.
        suffix: Data card suffix.
    """

    def __init__(self, multipliers: tuple[types.McnpReal], suffix: types.McnpInteger):
        """
        Initializes ``Tm``.

        Parameters:
            multipliers: Time bin multiplier to apply.
            suffix: Data card suffix.

        Raises:
            McnpError: INVALID_DATUM_PARAMETERS.
        """

        if multipliers is None:
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS, str(multipliers))

        for entry in multipliers:
            if entry is None:
                raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS, str(multipliers))

        if suffix is None or not (suffix <= 99_999_999):
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS, str(suffix))

        self.mnemonic: Final[DataMnemonic] = DataMnemonic.TM
        self.parameters: Final[tuple[any]] = tuple(list(multipliers) + [suffix])
        self.multipliers: Final[tuple[types.McnpReal]] = multipliers
        self.suffix: Final[types.McnpInteger] = suffix
        self.ident: Final[str] = f'tm{self.suffix}'

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``Tm`` objects from INP.

        ``from_mcnp`` translates from INP to PyMCNP; it parses INP.

        Parameters:
            source: INP for tm data cards.

        Returns:
            ``Tm`` object.

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
        if mnemonic != 'tm':
            raise errors.McnpError(errors.McnpCode.KEYWORD_DATUM_MNEMONIC)

        suffix = types.McnpInteger.from_mcnp(tokens.popl()[2:])

        multipliers = [types.McnpReal.from_mcnp(tokens.popl()) for _ in range(0, len(tokens))]

        data = Tm(multipliers, suffix)
        data.comment = comments

        return data

    def to_mcnp(self) -> str:
        """
        Generates INP from ``Tm`` objects.

        ``to_mcnp`` translates from PyMCNP to INP.

        Returns:
            INP for ``Tm``.
        """

        return _parser.Postprocessor.add_continuation_lines(
            f"{self.mnemonic.to_mcnp()}{self.suffix.to_mcnp()} {' '.join(entry.to_mcnp() for entry in self.multipliers)}"
        )
