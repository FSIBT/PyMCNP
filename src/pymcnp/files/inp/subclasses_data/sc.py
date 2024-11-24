"""
Contains the ``Sc`` subclass of ``Data``.
"""

import re
from typing import Final

from ..data import Data
from ..data import DataMnemonic
from ....utils import types, errors, _parser


class Sc(Data):
    """
    Represents INP sc data cards.

    ``Sc`` implements ``Data``.

    Attributes:
        comment: source comment.
        suffix: Data card suffix..
    """

    def __init__(self, comment: tuple[str], suffix: types.McnpInteger):
        """
        Initializes ``Sc``.

        Parameters:
            comment: source comment.
            suffix: Data card suffix..

        Raises:
            McnpError: INVALID_DATUM_PARAMETERS.
        """

        if comment is None:
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS, str(comment))

        for entry in comment:
            if entry is None:
                raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS, str(comment))

        if suffix is None:
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS, str(suffix))

        self.mnemonic: Final[DataMnemonic] = DataMnemonic.SC
        self.parameters: Final[tuple[any]] = tuple(list(comment) + [suffix])
        self.comment: Final[tuple[str]] = comment
        self.suffix: Final[types.McnpInteger] = suffix
        self.ident: Final[str] = f'sc{self.suffix}'

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``Sc`` objects from INP.

        ``from_mcnp`` translates from INP to PyMCNP; it parses INP.

        Parameters:
            source: INP for sc data cards.

        Returns:
            ``Sc`` object.

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
        if mnemonic != 'sc':
            raise errors.McnpError(errors.McnpCode.KEYWORD_DATUM_MNEMONIC)

        suffix = types.McnpInteger.from_mcnp(tokens.popl()[2:])

        comment = [tokens.popl() for _ in range(0, len(tokens))]
        suffix = types.McnpInteger.from_mcnp(tokens.popl())

        data = Sc(comment, suffix)
        data.comment = comments

        return data

    def to_mcnp(self) -> str:
        """
        Generates INP from ``Sc`` objects.

        ``to_mcnp`` translates from PyMCNP to INP.

        Returns:
            INP for ``Sc``.
        """

        return _parser.Postprocessor.add_continuation_lines(
            f"{self.mnemonic.to_mcnp()}{self.suffix.to_mcnp()} {" ".join(entry.to_mcnp() for entry in self.comment)} {self.suffix.to_mcnp()}"
        )
