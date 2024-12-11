"""
Contains the ``Kcode`` subclass of ``Data``.
"""

import re
from typing import Final

from ..data import Data
from ..data_mnemonic import DataMnemonic
from ...utils import types
from ...utils import errors
from ...utils import _parser


class Kcode(Data):
    """
    Represents INP kcode data cards.

    ``Kcode`` implements ``Data``.

    Attributes:
        nsrck: Number of source histories per cycle.
        rkk: Initial guess of keff.
        ikz: Number of cycles to be skipped before beginning tally accumulation.
        kct: Total number of cycles to be done.
        msrk: Number of source points to allocate for..
        knrm: Normalization of tallies setting.
        mrkp: Maximum number of cycle values on MCTAL or RUNTPE files.
        kc8: Number of cylces for average setting.
    """

    def __init__(
        self,
        nsrck: types.McnpInteger,
        rkk: types.McnpReal,
        ikz: types.McnpInteger,
        kct: types.McnpInteger,
        msrk: types.McnpInteger,
        knrm: types.McnpInteger,
        mrkp: types.McnpInteger,
        kc8: types.McnpInteger,
    ):
        """
        Initializes ``Kcode``.

        Parameters:
            nsrck: Number of source histories per cycle.
            rkk: Initial guess of keff.
            ikz: Number of cycles to be skipped before beginning tally accumulation.
            kct: Total number of cycles to be done.
            msrk: Number of source points to allocate for..
            knrm: Normalization of tallies setting.
            mrkp: Maximum number of cycle values on MCTAL or RUNTPE files.
            kc8: Number of cylces for average setting.

        Raises:
            McnpError: INVALID_DATUM_PARAMETERS.
        """

        if nsrck is None or not (nsrck >= 0):
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS, str(nsrck))

        if rkk is None:
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS, str(rkk))

        if ikz is None:
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS, str(ikz))

        if kct is None or not (kct > 0):
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS, str(kct))

        if msrk is None or not (msrk < 40 * nsrck):
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS, str(msrk))

        if knrm is None or knrm.value not in {0, 1}:
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS, str(knrm))

        if mrkp is None or not (mrkp > 0):
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS, str(mrkp))

        if kc8 is None or kc8.value not in {0, 1}:
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS, str(kc8))

        self.mnemonic: Final[DataMnemonic] = DataMnemonic.KCODE
        self.parameters: Final[tuple[any]] = tuple(
            [nsrck] + [rkk] + [ikz] + [kct] + [msrk] + [knrm] + [mrkp] + [kc8]
        )
        self.nsrck: Final[types.McnpInteger] = nsrck
        self.rkk: Final[types.McnpReal] = rkk
        self.ikz: Final[types.McnpInteger] = ikz
        self.kct: Final[types.McnpInteger] = kct
        self.msrk: Final[types.McnpInteger] = msrk
        self.knrm: Final[types.McnpInteger] = knrm
        self.mrkp: Final[types.McnpInteger] = mrkp
        self.kc8: Final[types.McnpInteger] = kc8
        self.ident: Final[str] = 'kcode'

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``Kcode`` objects from INP.

        ``from_mcnp`` translates from INP to PyMCNP; it parses INP.

        Parameters:
            source: INP for kcode data cards.

        Returns:
            ``Kcode`` object.

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
        if mnemonic != 'kcode':
            raise errors.McnpError(errors.McnpCode.KEYWORD_DATUM_MNEMONIC)

        tokens.popl()

        nsrck = types.McnpInteger.from_mcnp(tokens.popl())
        rkk = types.McnpReal.from_mcnp(tokens.popl())
        ikz = types.McnpInteger.from_mcnp(tokens.popl())
        kct = types.McnpInteger.from_mcnp(tokens.popl())
        msrk = types.McnpInteger.from_mcnp(tokens.popl())
        knrm = types.McnpInteger.from_mcnp(tokens.popl())
        mrkp = types.McnpInteger.from_mcnp(tokens.popl())
        kc8 = types.McnpInteger.from_mcnp(tokens.popl())

        data = Kcode(nsrck, rkk, ikz, kct, msrk, knrm, mrkp, kc8)
        data.comment = comments

        return data

    def to_mcnp(self) -> str:
        """
        Generates INP from ``Kcode`` objects.

        ``to_mcnp`` translates from PyMCNP to INP.

        Returns:
            INP for ``Kcode``.
        """

        return _parser.Postprocessor.add_continuation_lines(
            f'{self.mnemonic.to_mcnp()} {self.nsrck.to_mcnp()} {self.rkk.to_mcnp()} {self.ikz.to_mcnp()} {self.kct.to_mcnp()} {self.msrk.to_mcnp()} {self.knrm.to_mcnp()} {self.mrkp.to_mcnp()} {self.kc8.to_mcnp()}'
        )
