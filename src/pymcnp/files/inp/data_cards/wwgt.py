"""
Contains the ``Wwgt`` subclass of ``Data``.
"""

import re
from typing import Final

from ..data import Data
from ..data_mnemonic import DataMnemonic
from ...utils import types
from ...utils import errors
from ...utils import _parser


class Wwgt(Data):
    """
    Represents INP wwgt data cards.

    ``Wwgt`` implements ``Data``.

    Attributes:
        bounds: Upper time bound for weight-window group to be generated.
    """

    def __init__(self, bounds: tuple[types.McnpReal]):
        """
        Initializes ``Wwgt``.

        Parameters:
            bounds: Upper time bound for weight-window group to be generated.

        Raises:
            McnpError: INVALID_DATUM_PARAMETERS.
        """

        if bounds is None:
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS, str(bounds))

        for entry in bounds:
            if entry is None:
                raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS, str(bounds))

        self.mnemonic: Final[DataMnemonic] = DataMnemonic.WWGT
        self.parameters: Final[tuple[any]] = tuple(list(bounds))
        self.bounds: Final[tuple[types.McnpReal]] = bounds
        self.ident: Final[str] = 'wwgt'

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``Wwgt`` objects from INP.

        ``from_mcnp`` translates from INP to PyMCNP; it parses INP.

        Parameters:
            source: INP for wwgt data cards.

        Returns:
            ``Wwgt`` object.

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
        if mnemonic != 'wwgt':
            raise errors.McnpError(errors.McnpCode.KEYWORD_DATUM_MNEMONIC)

        tokens.popl()

        bounds = [types.McnpReal.from_mcnp(tokens.popl()) for _ in range(0, len(tokens))]

        data = Wwgt(bounds)
        data.comment = comments

        return data

    def to_mcnp(self) -> str:
        """
        Generates INP from ``Wwgt`` objects.

        ``to_mcnp`` translates from PyMCNP to INP.

        Returns:
            INP for ``Wwgt``.
        """

        return _parser.Postprocessor.add_continuation_lines(
            f"{self.mnemonic.to_mcnp()} {' '.join(entry.to_mcnp() for entry in self.bounds)}"
        )
