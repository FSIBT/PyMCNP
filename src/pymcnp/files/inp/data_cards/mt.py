"""
Contains the ``Mt`` subclass of ``Data``.
"""

import re
from typing import Final

from ..data import Data
from ..data_mnemonic import DataMnemonic
from ...utils import types
from ...utils import errors
from ...utils import _parser


class Mt(Data):
    """
    Represents INP mt data cards.

    ``Mt`` implements ``Data``.

    Attributes:
        identifier: Corresponding S(α,β) identifier.
        suffix: Data card suffix..
    """

    def __init__(self, identifier: str, suffix: types.McnpInteger):
        """
        Initializes ``Mt``.

        Parameters:
            identifier: Corresponding S(α,β) identifier.
            suffix: Data card suffix..

        Raises:
            McnpError: INVALID_DATUM_PARAMETERS.
        """

        if identifier is None:
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS, str(identifier))

        if suffix is None:
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS, str(suffix))

        self.mnemonic: Final[DataMnemonic] = DataMnemonic.MT
        self.parameters: Final[tuple[any]] = tuple([identifier] + [suffix])
        self.identifier: Final[str] = identifier
        self.suffix: Final[types.McnpInteger] = suffix
        self.ident: Final[str] = f'mt{self.suffix}'

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``Mt`` objects from INP.

        ``from_mcnp`` translates from INP to PyMCNP; it parses INP.

        Parameters:
            source: INP for mt data cards.

        Returns:
            ``Mt`` object.

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
        if mnemonic != 'mt':
            raise errors.McnpError(errors.McnpCode.KEYWORD_DATUM_MNEMONIC)

        suffix = types.McnpInteger.from_mcnp(tokens.popl()[2:])

        identifier = tokens.popl()

        data = Mt(identifier, suffix)
        data.comment = comments

        return data

    def to_mcnp(self) -> str:
        """
        Generates INP from ``Mt`` objects.

        ``to_mcnp`` translates from PyMCNP to INP.

        Returns:
            INP for ``Mt``.
        """

        return _parser.Postprocessor.add_continuation_lines(
            f'{self.mnemonic.to_mcnp()}{self.suffix.to_mcnp()} {self.identifier.to_mcnp()}'
        )
