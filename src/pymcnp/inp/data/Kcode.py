import re
import copy
import typing
import dataclasses


from . import _option
from ...utils import types
from ...utils import errors


class Kcode(_option.DataOption):
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

    _KEYWORD = 'kcode'

    _ATTRS = {
        'nsrck': types.Integer,
        'rkk': types.Real,
        'ikz': types.Integer,
        'kct': types.Integer,
        'msrk': types.Integer,
        'knrm': types.Integer,
        'mrkp': types.Integer,
        'kc8': types.Integer,
    }

    _REGEX = re.compile(
        rf'\Akcode( {types.Integer._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?\Z'
    )

    def __init__(
        self,
        nsrck: types.Integer = None,
        rkk: types.Real = None,
        ikz: types.Integer = None,
        kct: types.Integer = None,
        msrk: types.Integer = None,
        knrm: types.Integer = None,
        mrkp: types.Integer = None,
        kc8: types.Integer = None,
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

        if nsrck is not None and not (isinstance(nsrck.value, types.Jump) or nsrck >= 0):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, nsrck)
        if kct is not None and not (isinstance(kct.value, types.Jump) or kct > 0):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, kct)
        if msrk is not None and not (isinstance(msrk.value, types.Jump) or msrk < 40 * (1000 if not nsrck or isinstance(nsrck.value, types.Jump) else nsrck)):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, msrk)
        if knrm is not None and not (isinstance(knrm.value, types.Jump) or knrm in {0, 1}):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, knrm)
        if mrkp is not None and not (isinstance(mrkp.value, types.Jump) or mrkp > 0):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, mrkp)
        if kc8 is not None and not (isinstance(kc8.value, types.Jump) or kc8 in {0, 1}):
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

        self.nsrck: typing.Final[types.Integer] = nsrck
        self.rkk: typing.Final[types.Real] = rkk
        self.ikz: typing.Final[types.Integer] = ikz
        self.kct: typing.Final[types.Integer] = kct
        self.msrk: typing.Final[types.Integer] = msrk
        self.knrm: typing.Final[types.Integer] = knrm
        self.mrkp: typing.Final[types.Integer] = mrkp
        self.kc8: typing.Final[types.Integer] = kc8


@dataclasses.dataclass
class KcodeBuilder(_option.DataOptionBuilder):
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

    nsrck: str | int | types.Integer = None
    rkk: str | float | types.Real = None
    ikz: str | int | types.Integer = None
    kct: str | int | types.Integer = None
    msrk: str | int | types.Integer = None
    knrm: str | int | types.Integer = None
    mrkp: str | int | types.Integer = None
    kc8: str | int | types.Integer = None

    def build(self):
        """
        Builds ``KcodeBuilder`` into ``Kcode``.

        Returns:
            ``Kcode`` for ``KcodeBuilder``.
        """

        nsrck = self.nsrck
        if isinstance(self.nsrck, types.Integer):
            nsrck = self.nsrck
        elif isinstance(self.nsrck, int):
            nsrck = types.Integer(self.nsrck)
        elif isinstance(self.nsrck, str):
            nsrck = types.Integer.from_mcnp(self.nsrck)

        rkk = self.rkk
        if isinstance(self.rkk, types.Real):
            rkk = self.rkk
        elif isinstance(self.rkk, float) or isinstance(self.rkk, int):
            rkk = types.Real(self.rkk)
        elif isinstance(self.rkk, str):
            rkk = types.Real.from_mcnp(self.rkk)

        ikz = self.ikz
        if isinstance(self.ikz, types.Integer):
            ikz = self.ikz
        elif isinstance(self.ikz, int):
            ikz = types.Integer(self.ikz)
        elif isinstance(self.ikz, str):
            ikz = types.Integer.from_mcnp(self.ikz)

        kct = self.kct
        if isinstance(self.kct, types.Integer):
            kct = self.kct
        elif isinstance(self.kct, int):
            kct = types.Integer(self.kct)
        elif isinstance(self.kct, str):
            kct = types.Integer.from_mcnp(self.kct)

        msrk = self.msrk
        if isinstance(self.msrk, types.Integer):
            msrk = self.msrk
        elif isinstance(self.msrk, int):
            msrk = types.Integer(self.msrk)
        elif isinstance(self.msrk, str):
            msrk = types.Integer.from_mcnp(self.msrk)

        knrm = self.knrm
        if isinstance(self.knrm, types.Integer):
            knrm = self.knrm
        elif isinstance(self.knrm, int):
            knrm = types.Integer(self.knrm)
        elif isinstance(self.knrm, str):
            knrm = types.Integer.from_mcnp(self.knrm)

        mrkp = self.mrkp
        if isinstance(self.mrkp, types.Integer):
            mrkp = self.mrkp
        elif isinstance(self.mrkp, int):
            mrkp = types.Integer(self.mrkp)
        elif isinstance(self.mrkp, str):
            mrkp = types.Integer.from_mcnp(self.mrkp)

        kc8 = self.kc8
        if isinstance(self.kc8, types.Integer):
            kc8 = self.kc8
        elif isinstance(self.kc8, int):
            kc8 = types.Integer(self.kc8)
        elif isinstance(self.kc8, str):
            kc8 = types.Integer.from_mcnp(self.kc8)

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

    @staticmethod
    def unbuild(ast: Kcode):
        """
        Unbuilds ``Kcode`` into ``KcodeBuilder``

        Returns:
            ``KcodeBuilder`` for ``Kcode``.
        """

        return KcodeBuilder(
            nsrck=copy.deepcopy(ast.nsrck),
            rkk=copy.deepcopy(ast.rkk),
            ikz=copy.deepcopy(ast.ikz),
            kct=copy.deepcopy(ast.kct),
            msrk=copy.deepcopy(ast.msrk),
            knrm=copy.deepcopy(ast.knrm),
            mrkp=copy.deepcopy(ast.mrkp),
            kc8=copy.deepcopy(ast.kc8),
        )
