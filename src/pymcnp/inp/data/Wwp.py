import re
import typing
import dataclasses


from .option_ import DataOption_
from ...utils import types
from ...utils import errors


class Wwp(DataOption_, keyword='wwp'):
    """
    Represents INP wwp elements.

    Attributes:
        designator: Data card particle designator.
        wupn: Multiplier to define the weight window upper limit.
        wsurvn: Multiplier to define the maximum Russian roulette survival weight within the window.
        mxspln: Maximum number of integer splits.
        mwhere: Controls where to check a particle’s weight.
        switchn: Controls where to get the lower weight-window bounds.
        mtime: Energy/time-dependent window setting.
        wnrom: Weight-window normalization factor.
        etsplt: ESLPT & TSPLT split/roulette on/off.
        wu: Limits the maximum lower weight-window bound for any particle, energy, or time.
        nmfp: Limits the maximum lower weight-window bound for any particle, energy, or time.
    """

    _ATTRS = {
        'designator': types.Designator,
        'wupn': types.RealOrJump,
        'wsurvn': types.RealOrJump,
        'mxspln': types.RealOrJump,
        'mwhere': types.IntegerOrJump,
        'switchn': types.RealOrJump,
        'mtime': types.IntegerOrJump,
        'wnrom': types.RealOrJump,
        'etsplt': types.IntegerOrJump,
        'wu': types.RealOrJump,
        'nmfp': types.RealOrJump,
    }

    _REGEX = re.compile(
        rf'\Awwp:(\S+)( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})\Z'
    )

    def __init__(
        self,
        designator: types.Designator,
        wupn: types.RealOrJump,
        wsurvn: types.RealOrJump,
        mxspln: types.RealOrJump,
        mwhere: types.IntegerOrJump,
        switchn: types.RealOrJump,
        mtime: types.IntegerOrJump,
        wnrom: types.RealOrJump,
        etsplt: types.IntegerOrJump,
        wu: types.RealOrJump,
        nmfp: types.RealOrJump,
    ):
        """
        Initializes ``Wwp``.

        Parameters:
            designator: Data card particle designator.
            wupn: Multiplier to define the weight window upper limit.
            wsurvn: Multiplier to define the maximum Russian roulette survival weight within the window.
            mxspln: Maximum number of integer splits.
            mwhere: Controls where to check a particle’s weight.
            switchn: Controls where to get the lower weight-window bounds.
            mtime: Energy/time-dependent window setting.
            wnrom: Weight-window normalization factor.
            etsplt: ESLPT & TSPLT split/roulette on/off.
            wu: Limits the maximum lower weight-window bound for any particle, energy, or time.
            nmfp: Limits the maximum lower weight-window bound for any particle, energy, or time.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if designator is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, designator)
        if wupn is None or not (wupn >= 2):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, wupn)
        if wsurvn is None or not (1 < wsurvn):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, wsurvn)
        if mxspln is None or not (1 < mxspln):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, mxspln)
        if mwhere is None or mwhere.value not in {-1, 0, 1}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, mwhere)
        if switchn is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, switchn)
        if mtime is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, mtime)
        if wnrom is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, wnrom)
        if etsplt is None or etsplt.value not in {0, 1}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, etsplt)
        if wu is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, wu)
        if nmfp is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, nmfp)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                wupn,
                wsurvn,
                mxspln,
                mwhere,
                switchn,
                mtime,
                wnrom,
                etsplt,
                wu,
                nmfp,
            ]
        )

        self.designator: typing.Final[types.Designator] = designator
        self.wupn: typing.Final[types.RealOrJump] = wupn
        self.wsurvn: typing.Final[types.RealOrJump] = wsurvn
        self.mxspln: typing.Final[types.RealOrJump] = mxspln
        self.mwhere: typing.Final[types.IntegerOrJump] = mwhere
        self.switchn: typing.Final[types.RealOrJump] = switchn
        self.mtime: typing.Final[types.IntegerOrJump] = mtime
        self.wnrom: typing.Final[types.RealOrJump] = wnrom
        self.etsplt: typing.Final[types.IntegerOrJump] = etsplt
        self.wu: typing.Final[types.RealOrJump] = wu
        self.nmfp: typing.Final[types.RealOrJump] = nmfp


@dataclasses.dataclass
class WwpBuilder:
    """
    Builds ``Wwp``.

    Attributes:
        designator: Data card particle designator.
        wupn: Multiplier to define the weight window upper limit.
        wsurvn: Multiplier to define the maximum Russian roulette survival weight within the window.
        mxspln: Maximum number of integer splits.
        mwhere: Controls where to check a particle’s weight.
        switchn: Controls where to get the lower weight-window bounds.
        mtime: Energy/time-dependent window setting.
        wnrom: Weight-window normalization factor.
        etsplt: ESLPT & TSPLT split/roulette on/off.
        wu: Limits the maximum lower weight-window bound for any particle, energy, or time.
        nmfp: Limits the maximum lower weight-window bound for any particle, energy, or time.
    """

    designator: str | types.Designator
    wupn: str | float | types.RealOrJump
    wsurvn: str | float | types.RealOrJump
    mxspln: str | float | types.RealOrJump
    mwhere: str | int | types.IntegerOrJump
    switchn: str | float | types.RealOrJump
    mtime: str | int | types.IntegerOrJump
    wnrom: str | float | types.RealOrJump
    etsplt: str | int | types.IntegerOrJump
    wu: str | float | types.RealOrJump
    nmfp: str | float | types.RealOrJump

    def build(self):
        """
        Builds ``WwpBuilder`` into ``Wwp``.

        Returns:
            ``Wwp`` for ``WwpBuilder``.
        """

        if isinstance(self.designator, types.Designator):
            designator = self.designator
        elif isinstance(self.designator, str):
            designator = types.Designator.from_mcnp(self.designator)

        if isinstance(self.wupn, types.Real):
            wupn = self.wupn
        elif isinstance(self.wupn, float) or isinstance(self.wupn, int):
            wupn = types.RealOrJump(self.wupn)
        elif isinstance(self.wupn, str):
            wupn = types.RealOrJump.from_mcnp(self.wupn)

        if isinstance(self.wsurvn, types.Real):
            wsurvn = self.wsurvn
        elif isinstance(self.wsurvn, float) or isinstance(self.wsurvn, int):
            wsurvn = types.RealOrJump(self.wsurvn)
        elif isinstance(self.wsurvn, str):
            wsurvn = types.RealOrJump.from_mcnp(self.wsurvn)

        if isinstance(self.mxspln, types.Real):
            mxspln = self.mxspln
        elif isinstance(self.mxspln, float) or isinstance(self.mxspln, int):
            mxspln = types.RealOrJump(self.mxspln)
        elif isinstance(self.mxspln, str):
            mxspln = types.RealOrJump.from_mcnp(self.mxspln)

        if isinstance(self.mwhere, types.Integer):
            mwhere = self.mwhere
        elif isinstance(self.mwhere, int):
            mwhere = types.IntegerOrJump(self.mwhere)
        elif isinstance(self.mwhere, str):
            mwhere = types.IntegerOrJump.from_mcnp(self.mwhere)

        if isinstance(self.switchn, types.Real):
            switchn = self.switchn
        elif isinstance(self.switchn, float) or isinstance(self.switchn, int):
            switchn = types.RealOrJump(self.switchn)
        elif isinstance(self.switchn, str):
            switchn = types.RealOrJump.from_mcnp(self.switchn)

        if isinstance(self.mtime, types.Integer):
            mtime = self.mtime
        elif isinstance(self.mtime, int):
            mtime = types.IntegerOrJump(self.mtime)
        elif isinstance(self.mtime, str):
            mtime = types.IntegerOrJump.from_mcnp(self.mtime)

        if isinstance(self.wnrom, types.Real):
            wnrom = self.wnrom
        elif isinstance(self.wnrom, float) or isinstance(self.wnrom, int):
            wnrom = types.RealOrJump(self.wnrom)
        elif isinstance(self.wnrom, str):
            wnrom = types.RealOrJump.from_mcnp(self.wnrom)

        if isinstance(self.etsplt, types.Integer):
            etsplt = self.etsplt
        elif isinstance(self.etsplt, int):
            etsplt = types.IntegerOrJump(self.etsplt)
        elif isinstance(self.etsplt, str):
            etsplt = types.IntegerOrJump.from_mcnp(self.etsplt)

        if isinstance(self.wu, types.Real):
            wu = self.wu
        elif isinstance(self.wu, float) or isinstance(self.wu, int):
            wu = types.RealOrJump(self.wu)
        elif isinstance(self.wu, str):
            wu = types.RealOrJump.from_mcnp(self.wu)

        if isinstance(self.nmfp, types.Real):
            nmfp = self.nmfp
        elif isinstance(self.nmfp, float) or isinstance(self.nmfp, int):
            nmfp = types.RealOrJump(self.nmfp)
        elif isinstance(self.nmfp, str):
            nmfp = types.RealOrJump.from_mcnp(self.nmfp)

        return Wwp(
            designator=designator,
            wupn=wupn,
            wsurvn=wsurvn,
            mxspln=mxspln,
            mwhere=mwhere,
            switchn=switchn,
            mtime=mtime,
            wnrom=wnrom,
            etsplt=etsplt,
            wu=wu,
            nmfp=nmfp,
        )
