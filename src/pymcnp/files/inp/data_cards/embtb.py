"""
Contains the ``Embtb`` subclass of ``Data``.
"""

import re
from typing import Final

from ..data import Data
from ..data_mnemonic import DataMnemonic
from ...utils import types, errors, _parser


class Embtb(Data):
    """
    Represents INP embtb data cards.

    ``Embtb`` implements ``Data``.

    Attributes:
        bounds: Tuple of upper time bounds.
        suffix: Data card suffix..
    """

    def __init__(self, bounds: tuple[types.McnpReal], suffix: types.McnpInteger):
        """
        Initializes ``Embtb``.

        Parameters:
            bounds: Tuple of upper time bounds.
            suffix: Data card suffix..

        Raises:
            McnpError: INVALID_DATUM_PARAMETERS.
        """

        if bounds is None:
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS, str(bounds))

        for entry in bounds:
            if entry is None:
                raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS, str(bounds))

        if suffix is None:
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS, str(suffix))

        self.mnemonic: Final[DataMnemonic] = DataMnemonic.EMBTB
        self.parameters: Final[tuple[any]] = tuple(list(bounds) + [suffix])
        self.bounds: Final[tuple[types.McnpReal]] = bounds
        self.suffix: Final[types.McnpInteger] = suffix
        self.ident: Final[str] = f'embtb{self.suffix}'

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``Embtb`` objects from INP.

        ``from_mcnp`` translates from INP to PyMCNP; it parses INP.

        Parameters:
            source: INP for embtb data cards.

        Returns:
            ``Embtb`` object.

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
        if mnemonic != 'embtb':
            raise errors.McnpError(errors.McnpCode.KEYWORD_DATUM_MNEMONIC)

        suffix = types.McnpInteger.from_mcnp(tokens.popl()[5:])

        bounds = [types.McnpReal.from_mcnp(tokens.popl()) for _ in range(0, len(tokens))]

        data = Embtb(bounds, suffix)
        data.comment = comments

        return data

    def to_mcnp(self) -> str:
        """
        Generates INP from ``Embtb`` objects.

        ``to_mcnp`` translates from PyMCNP to INP.

        Returns:
            INP for ``Embtb``.
        """

        return _parser.Postprocessor.add_continuation_lines(
            f"{self.mnemonic.to_mcnp()}{self.suffix.to_mcnp()} {' '.join(entry.to_mcnp() for entry in self.bounds)}"
        )
