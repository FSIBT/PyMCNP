"""
Contains the ``Prdmp`` subclass of ``Data``.
"""

import re
from typing import Final

from ..data import Data
from ..data_mnemonic import DataMnemonic
from ...utils import types
from ...utils import errors
from ...utils import _parser


class Prdmp(Data):
    """
    Represents INP prdmp data cards.

    ``Prdmp`` implements ``Data``.

    Attributes:
        ndp: Increment for printing tallies.
        ndm: Increment for dumping to RUNTPE file.
        mct: Controls printing of MCTAL file.
        ndmp: Maximum number of dumps on RUNTPE file.
        dmmp: Controls frequently of tally fluctuation chart.
    """

    def __init__(
        self,
        ndp: types.McnpInteger,
        ndm: types.McnpInteger,
        mct: types.McnpInteger,
        ndmp: types.McnpInteger,
        dmmp: types.McnpInteger,
    ):
        """
        Initializes ``Prdmp``.

        Parameters:
            ndp: Increment for printing tallies.
            ndm: Increment for dumping to RUNTPE file.
            mct: Controls printing of MCTAL file.
            ndmp: Maximum number of dumps on RUNTPE file.
            dmmp: Controls frequently of tally fluctuation chart.

        Raises:
            McnpError: INVALID_DATUM_PARAMETERS.
        """

        if ndp is None:
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS, str(ndp))

        if ndm is None:
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS, str(ndm))

        if mct is None:
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS, str(mct))

        if ndmp is None:
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS, str(ndmp))

        if dmmp is None:
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS, str(dmmp))

        self.mnemonic: Final[DataMnemonic] = DataMnemonic.PRDMP
        self.parameters: Final[tuple[any]] = tuple([ndp] + [ndm] + [mct] + [ndmp] + [dmmp])
        self.ndp: Final[types.McnpInteger] = ndp
        self.ndm: Final[types.McnpInteger] = ndm
        self.mct: Final[types.McnpInteger] = mct
        self.ndmp: Final[types.McnpInteger] = ndmp
        self.dmmp: Final[types.McnpInteger] = dmmp
        self.ident: Final[str] = 'prdmp'

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``Prdmp`` objects from INP.

        ``from_mcnp`` translates from INP to PyMCNP; it parses INP.

        Parameters:
            source: INP for prdmp data cards.

        Returns:
            ``Prdmp`` object.

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
        if mnemonic != 'prdmp':
            raise errors.McnpError(errors.McnpCode.KEYWORD_DATUM_MNEMONIC)

        tokens.popl()

        ndp = types.McnpInteger.from_mcnp(tokens.popl())
        ndm = types.McnpInteger.from_mcnp(tokens.popl())
        mct = types.McnpInteger.from_mcnp(tokens.popl())
        ndmp = types.McnpInteger.from_mcnp(tokens.popl())
        dmmp = types.McnpInteger.from_mcnp(tokens.popl())

        data = Prdmp(ndp, ndm, mct, ndmp, dmmp)
        data.comment = comments

        return data

    def to_mcnp(self) -> str:
        """
        Generates INP from ``Prdmp`` objects.

        ``to_mcnp`` translates from PyMCNP to INP.

        Returns:
            INP for ``Prdmp``.
        """

        return _parser.Postprocessor.add_continuation_lines(
            f'{self.mnemonic.to_mcnp()} {self.ndp.to_mcnp()} {self.ndm.to_mcnp()} {self.mct.to_mcnp()} {self.ndmp.to_mcnp()} {self.dmmp.to_mcnp()}'
        )
