import re
import typing

from . import _option
from ...utils import types
from ...utils import errors
from ...utils import _parser


class DataOption_Wwp(_option.DataOption_, keyword='wwp'):
    """
    Represents INP data card wwp options.

    Attributes:
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
        designator: Data card particle designator.
    """

    _REGEX = re.compile(
        r'\Awwp:(\S+?)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)\Z'
    )

    def __init__(
        self,
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
        designator: types.Designator,
    ):
        """
        Initializes ``DataOption_Wwp``.

        Parameters:
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
            designator: Data card particle designator.

        Returns:
            ``DataOption_Wwp``.

        Raises:
            McnpError: SEMANTICS_DATA_OPTION_VALUE.
            McnpError: SEMANTICS_DATA_OPTION_VALUE.
            McnpError: SEMANTICS_DATA_OPTION_VALUE.
            McnpError: SEMANTICS_DATA_OPTION_VALUE.
            McnpError: SEMANTICS_DATA_OPTION_VALUE.
            McnpError: SEMANTICS_DATA_OPTION_VALUE.
            McnpError: SEMANTICS_DATA_OPTION_VALUE.
            McnpError: SEMANTICS_DATA_OPTION_VALUE.
            McnpError: SEMANTICS_DATA_OPTION_VALUE.
            McnpError: SEMANTICS_DATA_OPTION_VALUE.
            McnpError: SEMANTICS_DATA_OPTION_DESIGNATOR.
        """

        if wupn is None or not (wupn >= 2):
            raise errors.McnpError(errors.McnpCode.SEMANTICS_DATA_OPTION_VALUE, wupn)
        if wsurvn is None or not (1 < wsurvn):
            raise errors.McnpError(errors.McnpCode.SEMANTICS_DATA_OPTION_VALUE, wsurvn)
        if mxspln is None or not (1 < mxspln):
            raise errors.McnpError(errors.McnpCode.SEMANTICS_DATA_OPTION_VALUE, mxspln)
        if mwhere is None or mwhere.value not in {-1, 0, 1}:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_DATA_OPTION_VALUE, mwhere)
        if switchn is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_DATA_OPTION_VALUE, switchn)
        if mtime is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_DATA_OPTION_VALUE, mtime)
        if wnrom is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_DATA_OPTION_VALUE, wnrom)
        if etsplt is None or etsplt.value not in {0, 1}:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_DATA_OPTION_VALUE, etsplt)
        if wu is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_DATA_OPTION_VALUE, wu)
        if nmfp is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_DATA_OPTION_VALUE, nmfp)
        if designator is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_DATA_OPTION_DESIGNATOR, designator)

        self.value: typing.Final[tuple[any]] = types._Tuple(
            [wupn, wsurvn, mxspln, mwhere, switchn, mtime, wnrom, etsplt, wu, nmfp]
        )
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
        self.designator: typing.Final[types.Designator] = designator

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``DataOption_Wwp`` from INP.

        Parameters:
            source: INP data card option.

        Returns:
            ``DataOption_Wwp``.

        Raises:
            McnpError: SYNTAX_DATA_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = DataOption_Wwp._REGEX.match(source)

        if not tokens:
            raise errors.McnpError(errors.McnpCode.SYNTAX_DATA_OPTION, source)

        designator = types.Designator.from_mcnp(tokens[1])
        wupn = types.Real.from_mcnp(tokens[2])
        wsurvn = types.Real.from_mcnp(tokens[3])
        mxspln = types.Real.from_mcnp(tokens[4])
        mwhere = types.Integer.from_mcnp(tokens[5])
        switchn = types.Real.from_mcnp(tokens[6])
        mtime = types.Integer.from_mcnp(tokens[7])
        wnrom = types.Real.from_mcnp(tokens[8])
        etsplt = types.Integer.from_mcnp(tokens[9])
        wu = types.Real.from_mcnp(tokens[10])
        nmfp = types.Real.from_mcnp(tokens[11])

        return DataOption_Wwp(
            wupn, wsurvn, mxspln, mwhere, switchn, mtime, wnrom, etsplt, wu, nmfp, designator
        )
