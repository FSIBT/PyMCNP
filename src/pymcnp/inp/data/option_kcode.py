import re
import typing

from . import _option
from ...utils import types
from ...utils import errors
from ...utils import _parser


class DataOption_Kcode(_option.DataOption_, keyword='kcode'):
    """
    Represents INP data card kcode options.

    Attributes:
        nsrck: Number of source histories per cycle.
        rkk: Initial guess of keff.
        ikz: Number of cycles to be skipped before beginning tally accumulation.
        kct: Total number of cycles to be done.
        msrk: Number of source points to allocate for.
        knrm: Normalization of tallies setting.
        mrkp: Maximum number of cycle values on MCTAL or RUNTPE files.
        kc8: Number of cylces for average setting.
    """

    _REGEX = re.compile(r'\Akcode( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)\Z')

    def __init__(
        self,
        nsrck: types.Integer,
        rkk: types.Real,
        ikz: types.Integer,
        kct: types.Integer,
        msrk: types.Integer,
        knrm: types.Integer,
        mrkp: types.Integer,
        kc8: types.Integer,
    ):
        """
        Initializes ``DataOption_Kcode``.

        Parameters:
            nsrck: Number of source histories per cycle.
            rkk: Initial guess of keff.
            ikz: Number of cycles to be skipped before beginning tally accumulation.
            kct: Total number of cycles to be done.
            msrk: Number of source points to allocate for.
            knrm: Normalization of tallies setting.
            mrkp: Maximum number of cycle values on MCTAL or RUNTPE files.
            kc8: Number of cylces for average setting.

        Returns:
            ``DataOption_Kcode``.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if nsrck is None or not (nsrck >= 0):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, nsrck)
        if rkk is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, rkk)
        if ikz is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, ikz)
        if kct is None or not (kct > 0):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, kct)
        if msrk is None or not (msrk < 40 * nsrck):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, msrk)
        if knrm is None or knrm.value not in {0, 1}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, knrm)
        if mrkp is None or not (mrkp > 0):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, mrkp)
        if kc8 is None or kc8.value not in {0, 1}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, kc8)

        self.value: typing.Final[tuple[any]] = types._Tuple(
            [nsrck, rkk, ikz, kct, msrk, knrm, mrkp, kc8]
        )
        self.nsrck: typing.Final[types.Integer] = nsrck
        self.rkk: typing.Final[types.Real] = rkk
        self.ikz: typing.Final[types.Integer] = ikz
        self.kct: typing.Final[types.Integer] = kct
        self.msrk: typing.Final[types.Integer] = msrk
        self.knrm: typing.Final[types.Integer] = knrm
        self.mrkp: typing.Final[types.Integer] = mrkp
        self.kc8: typing.Final[types.Integer] = kc8

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``DataOption_Kcode`` from INP.

        Parameters:
            source: INP data card option.

        Returns:
            ``DataOption_Kcode``.

        Raises:
            InpError: SYNTAX_DATA_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = DataOption_Kcode._REGEX.match(source)

        if not tokens:
            raise errors.InpError(errors.InpCode.SYNTAX_OPTION, source)

        nsrck = types.Integer.from_mcnp(tokens[1])
        rkk = types.Real.from_mcnp(tokens[2])
        ikz = types.Integer.from_mcnp(tokens[3])
        kct = types.Integer.from_mcnp(tokens[4])
        msrk = types.Integer.from_mcnp(tokens[5])
        knrm = types.Integer.from_mcnp(tokens[6])
        mrkp = types.Integer.from_mcnp(tokens[7])
        kc8 = types.Integer.from_mcnp(tokens[8])

        return DataOption_Kcode(nsrck, rkk, ikz, kct, msrk, knrm, mrkp, kc8)
