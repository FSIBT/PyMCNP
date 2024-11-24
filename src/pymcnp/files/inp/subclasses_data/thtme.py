"""
Contains the ``Thtme`` subclass of ``Data``.
"""

import re
from typing import Final

from ..data import Data
from ..data import DataMnemonic
from ....utils import types, errors, _parser


class Thtme(Data):
    """
    Represents INP thtme data cards.

    ``Thtme`` implements ``Data``.

    Attributes:
        times: Tuple of times when thermal temperatures are specified.
    """

    def __init__(self, times: tuple[types.McnpReal]):
        """
        Initializes ``Thtme``.

        Parameters:
            times: Tuple of times when thermal temperatures are specified.

        Raises:
            McnpError: INVALID_DATUM_PARAMETERS.
        """

        if times is None:
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS, str(times))

        for entry in times:
            if entry is None or not (entry <= 99):
                raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS, str(times))

        self.mnemonic: Final[DataMnemonic] = DataMnemonic.THTME
        self.parameters: Final[tuple[any]] = tuple(list(times))
        self.times: Final[tuple[types.McnpReal]] = times
        self.ident: Final[str] = 'thtme'

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``Thtme`` objects from INP.

        ``from_mcnp`` translates from INP to PyMCNP; it parses INP.

        Parameters:
            source: INP for thtme data cards.

        Returns:
            ``Thtme`` object.

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
        if mnemonic != 'thtme':
            raise errors.McnpError(errors.McnpCode.KEYWORD_DATUM_MNEMONIC)

        tokens.popl()

        times = [types.McnpReal.from_mcnp(tokens.popl()) for _ in range(0, len(tokens))]

        data = Thtme(times)
        data.comment = comments

        return data

    def to_mcnp(self) -> str:
        """
        Generates INP from ``Thtme`` objects.

        ``to_mcnp`` translates from PyMCNP to INP.

        Returns:
            INP for ``Thtme``.
        """

        return _parser.Postprocessor.add_continuation_lines(
            f"{self.mnemonic.to_mcnp()} {" ".join(entry.to_mcnp() for entry in self.times)}"
        )
