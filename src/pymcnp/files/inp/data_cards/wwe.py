"""
Contains the ``Wwe`` subclass of ``Data``.
"""

import re
from typing import Final

from ..data import Data
from ..data_mnemonic import DataMnemonic
from ...utils import types
from ...utils import errors
from ...utils import _parser


class Wwe(Data):
    """
    Represents INP wwe data cards.

    ``Wwe`` implements ``Data``.

    Attributes:
        bounds: Upper energy/time bound.
        designator: Data card particle designator.
    """

    def __init__(self, bounds: tuple[types.McnpReal], designator: types.Designator):
        """
        Initializes ``Wwe``.

        Parameters:
            bounds: Upper energy/time bound.
            designator: Data card particle designator.

        Raises:
            McnpError: INVALID_DATUM_PARAMETERS.
        """

        if bounds is None:
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS, str(bounds))

        for entry in bounds:
            if entry is None:
                raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS, str(bounds))

        if designator is None:
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS, str(designator))

        self.mnemonic: Final[DataMnemonic] = DataMnemonic.WWE
        self.parameters: Final[tuple[any]] = tuple(list(bounds) + [designator])
        self.bounds: Final[tuple[types.McnpReal]] = bounds
        self.designator: Final[types.Designator] = designator
        self.ident: Final[str] = f'wwe:{self.designator}'

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``Wwe`` objects from INP.

        ``from_mcnp`` translates from INP to PyMCNP; it parses INP.

        Parameters:
            source: INP for wwe data cards.

        Returns:
            ``Wwe`` object.

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
        if mnemonic != 'wwe':
            raise errors.McnpError(errors.McnpCode.KEYWORD_DATUM_MNEMONIC)

        designator = types.Designator.from_mcnp(tokens.popl())
        tokens.popl()

        bounds = [types.McnpReal.from_mcnp(tokens.popl()) for _ in range(0, len(tokens))]

        data = Wwe(bounds, designator)
        data.comment = comments

        return data

    def to_mcnp(self) -> str:
        """
        Generates INP from ``Wwe`` objects.

        ``to_mcnp`` translates from PyMCNP to INP.

        Returns:
            INP for ``Wwe``.
        """

        return _parser.Postprocessor.add_continuation_lines(
            f"{self.mnemonic.to_mcnp()}:{self.designator.to_mcnp()} {' '.join(entry.to_mcnp() for entry in self.bounds)}"
        )
