import re
import typing


from .option_ import DataOption_
from ...utils import types
from ...utils import errors


class Wwp(DataOption_, keyword='wwp'):
    """
    Represents INP wwp elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
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
