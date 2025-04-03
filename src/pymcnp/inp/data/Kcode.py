import re
import typing


from .option_ import DataOption_
from ...utils import types
from ...utils import errors


class Kcode(DataOption_, keyword='kcode'):
    """
    Represents INP kcode elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'nsrck': types.IntegerOrJump,
        'rkk': types.RealOrJump,
        'ikz': types.IntegerOrJump,
        'kct': types.IntegerOrJump,
        'msrk': types.IntegerOrJump,
        'knrm': types.IntegerOrJump,
        'mrkp': types.IntegerOrJump,
        'kc8': types.IntegerOrJump,
    }

    _REGEX = re.compile(
        rf'\Akcode( {types.IntegerOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})\Z'
    )

    def __init__(
        self,
        nsrck: types.IntegerOrJump,
        rkk: types.RealOrJump,
        ikz: types.IntegerOrJump,
        kct: types.IntegerOrJump,
        msrk: types.IntegerOrJump,
        knrm: types.IntegerOrJump,
        mrkp: types.IntegerOrJump,
        kc8: types.IntegerOrJump,
    ):
        """
        Initializes ``Kcode``.

        Parameters:
            nsrck: Number of source histories per cycle.
            rkk: Initial guess of keff.
            ikz: Number of cycles to be skipped before beginning tally accumulation.
            kct: Total number of cycles to be done.
            msrk: Number of source points to allocate for.
            knrm: Normalization of tallies setting.
            mrkp: Maximum number of cycle values on MCTAL or RUNTPE files.
            kc8: Number of cylces for average setting.

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

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                nsrck,
                rkk,
                ikz,
                kct,
                msrk,
                knrm,
                mrkp,
                kc8,
            ]
        )

        self.nsrck: typing.Final[types.IntegerOrJump] = nsrck
        self.rkk: typing.Final[types.RealOrJump] = rkk
        self.ikz: typing.Final[types.IntegerOrJump] = ikz
        self.kct: typing.Final[types.IntegerOrJump] = kct
        self.msrk: typing.Final[types.IntegerOrJump] = msrk
        self.knrm: typing.Final[types.IntegerOrJump] = knrm
        self.mrkp: typing.Final[types.IntegerOrJump] = mrkp
        self.kc8: typing.Final[types.IntegerOrJump] = kc8
