import re
import typing
import dataclasses


from ._option import DataOption
from ...utils import types
from ...utils import errors


class Kcode(DataOption, keyword='kcode'):
    """
    Represents INP kcode elements.

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

    _ATTRS = {
        'nsrck': types.IntegerOrJump,
        'rkk': types.RealOrJump,
        'ikz': types.IntegerOrJump,
        'kct': types.IntegerOrJump,
        'msrk': types.Integer,
        'knrm': types.IntegerOrJump,
        'mrkp': types.IntegerOrJump,
        'kc8': types.IntegerOrJump,
    }

    _REGEX = re.compile(
        rf'\Akcode( {types.IntegerOrJump._REGEX.pattern})?( {types.RealOrJump._REGEX.pattern})?( {types.IntegerOrJump._REGEX.pattern})?( {types.IntegerOrJump._REGEX.pattern})?( {types.Integer._REGEX.pattern})?( {types.IntegerOrJump._REGEX.pattern})?( {types.IntegerOrJump._REGEX.pattern})?( {types.IntegerOrJump._REGEX.pattern})?\Z'
    )

    def __init__(
        self,
        nsrck: types.IntegerOrJump = None,
        rkk: types.RealOrJump = None,
        ikz: types.IntegerOrJump = None,
        kct: types.IntegerOrJump = None,
        msrk: types.Integer = None,
        knrm: types.IntegerOrJump = None,
        mrkp: types.IntegerOrJump = None,
        kc8: types.IntegerOrJump = None,
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
            InpError: SEMANTICS_OPTION.
        """

        if nsrck is not None and not (isinstance(nsrck.value, types.Jump) or nsrck.value >= 0):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, nsrck)
        if kct is not None and not (isinstance(kct.value, types.Jump) or kct.value > 0):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, kct)
        if msrk is not None and not (
            isinstance(msrk.value, types.Jump)
            or isinstance(nsrck.value, types.Jump)
            or msrk.value < 40 * nsrck.value
        ):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, msrk)
        if knrm is not None and not (isinstance(knrm.value, types.Jump) or knrm.value in {0, 1}):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, knrm)
        if mrkp is not None and not (isinstance(mrkp.value, types.Jump) or mrkp.value > 0):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, mrkp)
        if kc8 is not None and not (isinstance(mrkp.value, types.Jump) or kc8.value in {0, 1}):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, kc8)

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
        self.msrk: typing.Final[types.Integer] = msrk
        self.knrm: typing.Final[types.IntegerOrJump] = knrm
        self.mrkp: typing.Final[types.IntegerOrJump] = mrkp
        self.kc8: typing.Final[types.IntegerOrJump] = kc8


@dataclasses.dataclass
class KcodeBuilder:
    """
    Builds ``Kcode``.

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

    nsrck: str | int | types.IntegerOrJump = None
    rkk: str | float | types.RealOrJump = None
    ikz: str | int | types.IntegerOrJump = None
    kct: str | int | types.IntegerOrJump = None
    msrk: str | int | types.Integer = None
    knrm: str | int | types.IntegerOrJump = None
    mrkp: str | int | types.IntegerOrJump = None
    kc8: str | int | types.IntegerOrJump = None

    def build(self):
        """
        Builds ``KcodeBuilder`` into ``Kcode``.

        Returns:
            ``Kcode`` for ``KcodeBuilder``.
        """

        nsrck = None
        if isinstance(self.nsrck, types.Integer):
            nsrck = self.nsrck
        elif isinstance(self.nsrck, int):
            nsrck = types.IntegerOrJump(self.nsrck)
        elif isinstance(self.nsrck, str):
            nsrck = types.IntegerOrJump.from_mcnp(self.nsrck)

        rkk = None
        if isinstance(self.rkk, types.Real):
            rkk = self.rkk
        elif isinstance(self.rkk, float) or isinstance(self.rkk, int):
            rkk = types.RealOrJump(self.rkk)
        elif isinstance(self.rkk, str):
            rkk = types.RealOrJump.from_mcnp(self.rkk)

        ikz = None
        if isinstance(self.ikz, types.Integer):
            ikz = self.ikz
        elif isinstance(self.ikz, int):
            ikz = types.IntegerOrJump(self.ikz)
        elif isinstance(self.ikz, str):
            ikz = types.IntegerOrJump.from_mcnp(self.ikz)

        kct = None
        if isinstance(self.kct, types.Integer):
            kct = self.kct
        elif isinstance(self.kct, int):
            kct = types.IntegerOrJump(self.kct)
        elif isinstance(self.kct, str):
            kct = types.IntegerOrJump.from_mcnp(self.kct)

        msrk = None
        if isinstance(self.msrk, types.Integer):
            msrk = self.msrk
        elif isinstance(self.msrk, int):
            msrk = types.Integer(self.msrk)
        elif isinstance(self.msrk, str):
            msrk = types.Integer.from_mcnp(self.msrk)

        knrm = None
        if isinstance(self.knrm, types.Integer):
            knrm = self.knrm
        elif isinstance(self.knrm, int):
            knrm = types.IntegerOrJump(self.knrm)
        elif isinstance(self.knrm, str):
            knrm = types.IntegerOrJump.from_mcnp(self.knrm)

        mrkp = None
        if isinstance(self.mrkp, types.Integer):
            mrkp = self.mrkp
        elif isinstance(self.mrkp, int):
            mrkp = types.IntegerOrJump(self.mrkp)
        elif isinstance(self.mrkp, str):
            mrkp = types.IntegerOrJump.from_mcnp(self.mrkp)

        kc8 = None
        if isinstance(self.kc8, types.Integer):
            kc8 = self.kc8
        elif isinstance(self.kc8, int):
            kc8 = types.IntegerOrJump(self.kc8)
        elif isinstance(self.kc8, str):
            kc8 = types.IntegerOrJump.from_mcnp(self.kc8)

        return Kcode(
            nsrck=nsrck,
            rkk=rkk,
            ikz=ikz,
            kct=kct,
            msrk=msrk,
            knrm=knrm,
            mrkp=mrkp,
            kc8=kc8,
        )
