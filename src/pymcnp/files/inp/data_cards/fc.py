"""
Contains the ``Fc`` subclass of ``Data``.
"""

import re
from typing import Final

from ..data import Data
from ..data_mnemonic import DataMnemonic
from ...utils import types
from ...utils import errors
from ...utils import _parser


class Fc(Data):
    """
    Represents INP fc data cards.

    ``Fc`` implements ``Data``.

    Attributes:
        info: Title for tally in output and MCTAL file.
        suffix: Data card suffix.
    """

    def __init__(self, info: str, suffix: types.McnpInteger):
        """
        Initializes ``Fc``.

        Parameters:
            info: Title for tally in output and MCTAL file.
            suffix: Data card suffix.

        Raises:
            McnpError: INVALID_DATUM_PARAMETERS.
        """

        if info is None:
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS, str(info))

        if suffix is None or not (suffix <= 99_999_999):
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS, str(suffix))

        self.mnemonic: Final[DataMnemonic] = DataMnemonic.FC
        self.parameters: Final[tuple[any]] = tuple([info] + [suffix])
        self.info: Final[str] = info
        self.suffix: Final[types.McnpInteger] = suffix
        self.ident: Final[str] = f'fc{self.suffix}'

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``Fc`` objects from INP.

        ``from_mcnp`` translates from INP to PyMCNP; it parses INP.

        Parameters:
            source: INP for fc data cards.

        Returns:
            ``Fc`` object.

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
        if mnemonic != 'fc':
            raise errors.McnpError(errors.McnpCode.KEYWORD_DATUM_MNEMONIC)

        suffix = types.McnpInteger.from_mcnp(tokens.popl()[2:])

        info = tokens.popl()

        data = Fc(info, suffix)
        data.comment = comments

        return data

    def to_mcnp(self) -> str:
        """
        Generates INP from ``Fc`` objects.

        ``to_mcnp`` translates from PyMCNP to INP.

        Returns:
            INP for ``Fc``.
        """

        return _parser.Postprocessor.add_continuation_lines(
            f'{self.mnemonic.to_mcnp()}{self.suffix.to_mcnp()} {self.info.to_mcnp()}'
        )
