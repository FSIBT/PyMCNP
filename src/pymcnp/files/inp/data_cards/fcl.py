"""
Contains the ``Fcl`` subclass of ``Data``.
"""

import re
from typing import Final

from ..data import Data
from ..data_mnemonic import DataMnemonic
from ...utils import types
from ...utils import errors
from ...utils import _parser


class Fcl(Data):
    """
    Represents INP fcl data cards.

    ``Fcl`` implements ``Data``.

    Attributes:
        control: Forced-collision control for cell.
        designator: Data card particle designator.
    """

    def __init__(self, control: tuple[types.McnpReal], designator: types.Designator):
        """
        Initializes ``Fcl``.

        Parameters:
            control: Forced-collision control for cell.
            designator: Data card particle designator.

        Raises:
            McnpError: INVALID_DATUM_PARAMETERS.
        """

        if control is None:
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS, str(control))

        for entry in control:
            if entry is None:
                raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS, str(control))

        if designator is None:
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS, str(designator))

        self.mnemonic: Final[DataMnemonic] = DataMnemonic.FCL
        self.parameters: Final[tuple[any]] = tuple(list(control) + [designator])
        self.control: Final[tuple[types.McnpReal]] = control
        self.designator: Final[types.Designator] = designator
        self.ident: Final[str] = f'fcl:{self.designator}'

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``Fcl`` objects from INP.

        ``from_mcnp`` translates from INP to PyMCNP; it parses INP.

        Parameters:
            source: INP for fcl data cards.

        Returns:
            ``Fcl`` object.

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
        if mnemonic != 'fcl':
            raise errors.McnpError(errors.McnpCode.KEYWORD_DATUM_MNEMONIC)

        designator = types.Designator.from_mcnp(tokens.popl())
        tokens.popl()

        control = [types.McnpReal.from_mcnp(tokens.popl()) for _ in range(0, len(tokens))]

        data = Fcl(control, designator)
        data.comment = comments

        return data

    def to_mcnp(self) -> str:
        """
        Generates INP from ``Fcl`` objects.

        ``to_mcnp`` translates from PyMCNP to INP.

        Returns:
            INP for ``Fcl``.
        """

        return _parser.Postprocessor.add_continuation_lines(
            f"{self.mnemonic.to_mcnp()}:{self.designator.to_mcnp()} {' '.join(entry.to_mcnp() for entry in self.control)}"
        )