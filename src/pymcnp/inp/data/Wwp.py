import re
import copy
import typing
import dataclasses


from ._option import DataOption
from ...utils import types
from ...utils import errors


class Wwp(DataOption):
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

    _KEYWORD = 'wwp'

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

    _REGEX = re.compile(
        rf'\Awwp:(\S+)( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?\Z'
    )

    def __init__(
        self,
        designator: types.Designator,
        wupn: types.Real = None,
        wsurvn: types.Real = None,
        mxspln: types.Real = None,
        mwhere: types.Integer = None,
        switchn: types.Real = None,
        mtime: types.Integer = None,
        wnrom: types.Real = None,
        etsplt: types.Integer = None,
        wu: types.Real = None,
        nmfp: types.Real = None,
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
            InpError: SEMANTICS_OPTION.
        """

        if designator is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, designator)
        if wupn is not None and not (isinstance(wupn.value, types.Jump) or wupn.value >= 2):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, wupn)
        if wsurvn is not None and not (isinstance(wsurvn.value, types.Jump) or 1 < wsurvn.value):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, wsurvn)
        if mxspln is not None and not (isinstance(mxspln.value, types.Jump) or 1 < mxspln.value):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, mxspln)
        if mwhere is not None and not (
            isinstance(mwhere.value, types.Jump) or mwhere.value in {-1, 0, 1}
        ):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, mwhere)
        if etsplt is not None and not (
            isinstance(etsplt.value, types.Jump) or etsplt.value in {0, 1}
        ):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, etsplt)

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
    wupn: str | float | types.Real = None
    wsurvn: str | float | types.Real = None
    mxspln: str | float | types.Real = None
    mwhere: str | int | types.Integer = None
    switchn: str | float | types.Real = None
    mtime: str | int | types.Integer = None
    wnrom: str | float | types.Real = None
    etsplt: str | int | types.Integer = None
    wu: str | float | types.Real = None
    nmfp: str | float | types.Real = None

    def build(self):
        """
        Builds ``WwpBuilder`` into ``Wwp``.

        Returns:
            ``Wwp`` for ``WwpBuilder``.
        """

        designator = self.designator
        if isinstance(self.designator, types.Designator):
            designator = self.designator
        elif isinstance(self.designator, str):
            designator = types.Designator.from_mcnp(self.designator)

        wupn = self.wupn
        if isinstance(self.wupn, types.Real):
            wupn = self.wupn
        elif isinstance(self.wupn, float) or isinstance(self.wupn, int):
            wupn = types.Real(self.wupn)
        elif isinstance(self.wupn, str):
            wupn = types.Real.from_mcnp(self.wupn)

        wsurvn = self.wsurvn
        if isinstance(self.wsurvn, types.Real):
            wsurvn = self.wsurvn
        elif isinstance(self.wsurvn, float) or isinstance(self.wsurvn, int):
            wsurvn = types.Real(self.wsurvn)
        elif isinstance(self.wsurvn, str):
            wsurvn = types.Real.from_mcnp(self.wsurvn)

        mxspln = self.mxspln
        if isinstance(self.mxspln, types.Real):
            mxspln = self.mxspln
        elif isinstance(self.mxspln, float) or isinstance(self.mxspln, int):
            mxspln = types.Real(self.mxspln)
        elif isinstance(self.mxspln, str):
            mxspln = types.Real.from_mcnp(self.mxspln)

        mwhere = self.mwhere
        if isinstance(self.mwhere, types.Integer):
            mwhere = self.mwhere
        elif isinstance(self.mwhere, int):
            mwhere = types.Integer(self.mwhere)
        elif isinstance(self.mwhere, str):
            mwhere = types.Integer.from_mcnp(self.mwhere)

        switchn = self.switchn
        if isinstance(self.switchn, types.Real):
            switchn = self.switchn
        elif isinstance(self.switchn, float) or isinstance(self.switchn, int):
            switchn = types.Real(self.switchn)
        elif isinstance(self.switchn, str):
            switchn = types.Real.from_mcnp(self.switchn)

        mtime = self.mtime
        if isinstance(self.mtime, types.Integer):
            mtime = self.mtime
        elif isinstance(self.mtime, int):
            mtime = types.Integer(self.mtime)
        elif isinstance(self.mtime, str):
            mtime = types.Integer.from_mcnp(self.mtime)

        wnrom = self.wnrom
        if isinstance(self.wnrom, types.Real):
            wnrom = self.wnrom
        elif isinstance(self.wnrom, float) or isinstance(self.wnrom, int):
            wnrom = types.Real(self.wnrom)
        elif isinstance(self.wnrom, str):
            wnrom = types.Real.from_mcnp(self.wnrom)

        etsplt = self.etsplt
        if isinstance(self.etsplt, types.Integer):
            etsplt = self.etsplt
        elif isinstance(self.etsplt, int):
            etsplt = types.Integer(self.etsplt)
        elif isinstance(self.etsplt, str):
            etsplt = types.Integer.from_mcnp(self.etsplt)

        wu = self.wu
        if isinstance(self.wu, types.Real):
            wu = self.wu
        elif isinstance(self.wu, float) or isinstance(self.wu, int):
            wu = types.Real(self.wu)
        elif isinstance(self.wu, str):
            wu = types.Real.from_mcnp(self.wu)

        nmfp = self.nmfp
        if isinstance(self.nmfp, types.Real):
            nmfp = self.nmfp
        elif isinstance(self.nmfp, float) or isinstance(self.nmfp, int):
            nmfp = types.Real(self.nmfp)
        elif isinstance(self.nmfp, str):
            nmfp = types.Real.from_mcnp(self.nmfp)

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

    @staticmethod
    def unbuild(ast: Wwp):
        """
        Unbuilds ``Wwp`` into ``WwpBuilder``

        Returns:
            ``WwpBuilder`` for ``Wwp``.
        """

        return Wwp(
            designator=copy.deepcopy(ast.designator),
            wupn=copy.deepcopy(ast.wupn),
            wsurvn=copy.deepcopy(ast.wsurvn),
            mxspln=copy.deepcopy(ast.mxspln),
            mwhere=copy.deepcopy(ast.mwhere),
            switchn=copy.deepcopy(ast.switchn),
            mtime=copy.deepcopy(ast.mtime),
            wnrom=copy.deepcopy(ast.wnrom),
            etsplt=copy.deepcopy(ast.etsplt),
            wu=copy.deepcopy(ast.wu),
            nmfp=copy.deepcopy(ast.nmfp),
        )
