"""
Contains the ``Ext`` subclass of ``Data``.
"""

import re
from typing import Final

from ..data import Data
from ..data_mnemonic import DataMnemonic
from ...utils import types
from ...utils import errors
from ...utils import _parser


class Ext(Data):
    """
    Represents INP ext data cards.

    ``Ext`` implements ``Data``.

    Attributes:
        stretching: Stretching direction for the cell.
        designator: Data card particle designator.
    """

    def __init__(self, stretching: tuple[types.McnpReal], designator: types.Designator):
        """
        Initializes ``Ext``.

        Parameters:
            stretching: Stretching direction for the cell.
            designator: Data card particle designator.

        Raises:
            McnpError: INVALID_DATUM_PARAMETERS.
        """

        if stretching is None:
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS, str(stretching))

        for entry in stretching:
            if entry is None:
                raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS, str(stretching))

        if designator is None:
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS, str(designator))

        self.mnemonic: Final[DataMnemonic] = DataMnemonic.EXT
        self.parameters: Final[tuple[any]] = tuple(list(stretching) + [designator])
        self.stretching: Final[tuple[types.McnpReal]] = stretching
        self.designator: Final[types.Designator] = designator
        self.ident: Final[str] = f'ext:{self.designator}'

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``Ext`` objects from INP.

        ``from_mcnp`` translates from INP to PyMCNP; it parses INP.

        Parameters:
            source: INP for ext data cards.

        Returns:
            ``Ext`` object.

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
        if mnemonic != 'ext':
            raise errors.McnpError(errors.McnpCode.KEYWORD_DATUM_MNEMONIC)

        designator = types.Designator.from_mcnp(tokens.popl())
        tokens.popl()

        stretching = [types.McnpReal.from_mcnp(tokens.popl()) for _ in range(0, len(tokens))]

        data = Ext(stretching, designator)
        data.comment = comments

        return data

    def to_mcnp(self) -> str:
        """
        Generates INP from ``Ext`` objects.

        ``to_mcnp`` translates from PyMCNP to INP.

        Returns:
            INP for ``Ext``.
        """

        return _parser.Postprocessor.add_continuation_lines(
            f"{self.mnemonic.to_mcnp()}:{self.designator.to_mcnp()} {' '.join(entry.to_mcnp() for entry in self.stretching)}"
        )
