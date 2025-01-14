"""
Contains the ``Dxc`` subclass of ``Data``.
"""

import re
from typing import Final

from ..data import Data
from ..data_mnemonic import DataMnemonic
from ...utils import types
from ...utils import errors
from ...utils import _parser


class Dxc(Data):
    """
    Represents INP dxc data cards.

    ``Dxc`` implements ``Data``.

    Attributes:
        probabilities: Probability of contribution to DXTRAN.
        suffix: Data card suffix.
        designator: Data card particle designator.
    """

    def __init__(
        self,
        probabilities: tuple[types.McnpReal],
        suffix: types.McnpInteger,
        designator: types.Designator,
    ):
        """
        Initializes ``Dxc``.

        Parameters:
            probabilities: Probability of contribution to DXTRAN.
            suffix: Data card suffix.
            designator: Data card particle designator.

        Raises:
            McnpError: INVALID_DATUM_PARAMETERS.
        """

        if probabilities is None:
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS, str(probabilities))

        for entry in probabilities:
            if entry is None or not (0 <= entry <= 1):
                raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS, str(probabilities))

        if suffix is None or not (suffix <= 99_999_999):
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS, str(suffix))

        if designator is None:
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS, str(designator))

        self.mnemonic: Final[DataMnemonic] = DataMnemonic.DXC
        self.parameters: Final[tuple[any]] = tuple(list(probabilities) + [suffix] + [designator])
        self.probabilities: Final[tuple[types.McnpReal]] = probabilities
        self.suffix: Final[types.McnpInteger] = suffix
        self.designator: Final[types.Designator] = designator
        self.ident: Final[str] = f'dxc{self.suffix}:{self.designator}'

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``Dxc`` objects from INP.

        ``from_mcnp`` translates from INP to PyMCNP; it parses INP.

        Parameters:
            source: INP for dxc data cards.

        Returns:
            ``Dxc`` object.

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
        if mnemonic != 'dxc':
            raise errors.McnpError(errors.McnpCode.KEYWORD_DATUM_MNEMONIC)

        designator = types.Designator.from_mcnp(tokens.popl())
        suffix = types.McnpInteger.from_mcnp(tokens.popl()[3:])

        probabilities = [types.McnpReal.from_mcnp(tokens.popl()) for _ in range(0, len(tokens))]

        data = Dxc(probabilities, suffix, designator)
        data.comment = comments

        return data

    def to_mcnp(self) -> str:
        """
        Generates INP from ``Dxc`` objects.

        ``to_mcnp`` translates from PyMCNP to INP.

        Returns:
            INP for ``Dxc``.
        """

        return _parser.Postprocessor.add_continuation_lines(
            f"{self.mnemonic.to_mcnp()}{self.suffix.to_mcnp()}:{self.designator.to_mcnp()} {' '.join(entry.to_mcnp() for entry in self.probabilities)}"
        )
