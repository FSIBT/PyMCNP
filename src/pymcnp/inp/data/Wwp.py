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
        'wupn': types.Real,
        'wsurvn': types.Real,
        'mxspln': types.Real,
        'mwhere': types.Integer,
        'switchn': types.Real,
        'mtime': types.Integer,
        'wnrom': types.Real,
        'etsplt': types.Integer,
        'wu': types.Real,
        'nmfp': types.Real,
    }

    _REGEX = re.compile(r'wwp:(\S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)')

    def __init__(
        self,
        designator: types.Designator,
        wupn: types.Real,
        wsurvn: types.Real,
        mxspln: types.Real,
        mwhere: types.Integer,
        switchn: types.Real,
        mtime: types.Integer,
        wnrom: types.Real,
        etsplt: types.Integer,
        wu: types.Real,
        nmfp: types.Real,
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
        self.wupn: typing.Final[types.Real] = wupn
        self.wsurvn: typing.Final[types.Real] = wsurvn
        self.mxspln: typing.Final[types.Real] = mxspln
        self.mwhere: typing.Final[types.Integer] = mwhere
        self.switchn: typing.Final[types.Real] = switchn
        self.mtime: typing.Final[types.Integer] = mtime
        self.wnrom: typing.Final[types.Real] = wnrom
        self.etsplt: typing.Final[types.Integer] = etsplt
        self.wu: typing.Final[types.Real] = wu
        self.nmfp: typing.Final[types.Real] = nmfp
