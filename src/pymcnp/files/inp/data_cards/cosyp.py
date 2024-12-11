"""
Contains the ``Cosyp`` subclass of ``Data``.
"""

import re
from typing import Final

from ..data import Data
from ..data_mnemonic import DataMnemonic
from ...utils import types
from ...utils import errors
from ...utils import _parser


class Cosyp(Data):
    """
    Represents INP cosyp data cards.

    ``Cosyp`` implements ``Data``.

    Attributes:
        prefix: Prefix number of the COSY map files.
        axsh: Horiztonal axis orientation.
        axsv: Vertical axis orientation.
        emaps: Tuple of operating beam energies.
    """

    def __init__(
        self,
        prefix: types.McnpInteger,
        axsh: types.McnpInteger,
        axsv: types.McnpInteger,
        emaps: tuple[types.McnpReal],
    ):
        """
        Initializes ``Cosyp``.

        Parameters:
            prefix: Prefix number of the COSY map files.
            axsh: Horiztonal axis orientation.
            axsv: Vertical axis orientation.
            emaps: Tuple of operating beam energies.

        Raises:
            McnpError: INVALID_DATUM_PARAMETERS.
        """

        if prefix is None:
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS, str(prefix))

        if axsh is None or axsh.value not in {1, 2, 3}:
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS, str(axsh))

        if axsv is None or axsv.value not in {1, 2, 3}:
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS, str(axsv))

        if emaps is None:
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS, str(emaps))

        for entry in emaps:
            if entry is None:
                raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS, str(emaps))

        self.mnemonic: Final[DataMnemonic] = DataMnemonic.COSYP
        self.parameters: Final[tuple[any]] = tuple([prefix] + [axsh] + [axsv] + list(emaps))
        self.prefix: Final[types.McnpInteger] = prefix
        self.axsh: Final[types.McnpInteger] = axsh
        self.axsv: Final[types.McnpInteger] = axsv
        self.emaps: Final[tuple[types.McnpReal]] = emaps
        self.ident: Final[str] = 'cosyp'

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``Cosyp`` objects from INP.

        ``from_mcnp`` translates from INP to PyMCNP; it parses INP.

        Parameters:
            source: INP for cosyp data cards.

        Returns:
            ``Cosyp`` object.

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
        if mnemonic != 'cosyp':
            raise errors.McnpError(errors.McnpCode.KEYWORD_DATUM_MNEMONIC)

        tokens.popl()

        prefix = types.McnpInteger.from_mcnp(tokens.popl())
        axsh = types.McnpInteger.from_mcnp(tokens.popl())
        axsv = types.McnpInteger.from_mcnp(tokens.popl())
        emaps = [types.McnpReal.from_mcnp(tokens.popl()) for _ in range(0, len(tokens))]

        data = Cosyp(prefix, axsh, axsv, emaps)
        data.comment = comments

        return data

    def to_mcnp(self) -> str:
        """
        Generates INP from ``Cosyp`` objects.

        ``to_mcnp`` translates from PyMCNP to INP.

        Returns:
            INP for ``Cosyp``.
        """

        return _parser.Postprocessor.add_continuation_lines(
            f"{self.mnemonic.to_mcnp()} {self.prefix.to_mcnp()} {self.axsh.to_mcnp()} {self.axsv.to_mcnp()} {' '.join(entry.to_mcnp() for entry in self.emaps)}"
        )
