"""
Contains the ``Imp`` subclass of ``Data``.
"""

import re
from typing import Final

from ..data import Data
from ..data_mnemonic import DataMnemonic
from ...utils import types
from ...utils import errors
from ...utils import _parser


class Imp(Data):
    """
    Represents INP imp data cards.

    ``Imp`` implements ``Data``.

    Attributes:
        importances: Cell importance.
        designator: Data card particle designator.
    """

    def __init__(self, importances: tuple[types.McnpReal], designator: types.Designator):
        """
        Initializes ``Imp``.

        Parameters:
            importances: Cell importance.
            designator: Data card particle designator.

        Raises:
            McnpError: INVALID_DATUM_PARAMETERS.
        """

        if importances is None:
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS, str(importances))

        for entry in importances:
            if entry is None:
                raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS, str(importances))

        if designator is None:
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS, str(designator))

        self.mnemonic: Final[DataMnemonic] = DataMnemonic.IMP
        self.parameters: Final[tuple[any]] = tuple(list(importances) + [designator])
        self.importances: Final[tuple[types.McnpReal]] = importances
        self.designator: Final[types.Designator] = designator
        self.ident: Final[str] = f'imp:{self.designator}'

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``Imp`` objects from INP.

        ``from_mcnp`` translates from INP to PyMCNP; it parses INP.

        Parameters:
            source: INP for imp data cards.

        Returns:
            ``Imp`` object.

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
        if mnemonic != 'imp':
            raise errors.McnpError(errors.McnpCode.KEYWORD_DATUM_MNEMONIC)

        designator = types.Designator.from_mcnp(tokens.popl())
        tokens.popl()

        importances = [types.McnpReal.from_mcnp(tokens.popl()) for _ in range(0, len(tokens))]

        data = Imp(importances, designator)
        data.comment = comments

        return data

    def to_mcnp(self) -> str:
        """
        Generates INP from ``Imp`` objects.

        ``to_mcnp`` translates from PyMCNP to INP.

        Returns:
            INP for ``Imp``.
        """

        return _parser.Postprocessor.add_continuation_lines(
            f"{self.mnemonic.to_mcnp()}:{self.designator.to_mcnp()} {' '.join(entry.to_mcnp() for entry in self.importances)}"
        )
