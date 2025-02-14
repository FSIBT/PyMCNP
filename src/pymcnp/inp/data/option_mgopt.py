import re
import typing

from . import _option
from ...utils import types
from ...utils import errors
from ...utils import _parser


class DataOption_Mgopt(_option.DataOption_, keyword='mgopt'):
    """
    Represents INP data card mgopt options.

    Attributes:
        mcal: Problem type setting.
        igm: Total number of energy groups for all kinds of particle.
        iplt: Weight windows usage indicator.
        iab: Adjoint biasing for adjoint problems contorls.
        icw: Name of the reference cell for generated weight windows.
        fnw: Normalization value for generated weight windows.
        rim: Generated weight windows compression limit.
    """

    _REGEX = re.compile(r'\Amgopt( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)\Z')

    def __init__(
        self,
        mcal: types.String,
        igm: types.Integer,
        iplt: types.Integer,
        iab: types.Integer,
        icw: types.Integer,
        fnw: types.Real,
        rim: types.Real,
    ):
        """
        Initializes ``DataOption_Mgopt``.

        Parameters:
            mcal: Problem type setting.
            igm: Total number of energy groups for all kinds of particle.
            iplt: Weight windows usage indicator.
            iab: Adjoint biasing for adjoint problems contorls.
            icw: Name of the reference cell for generated weight windows.
            fnw: Normalization value for generated weight windows.
            rim: Generated weight windows compression limit.

        Returns:
            ``DataOption_Mgopt``.

        Raises:
            McnpError: SEMANTICS_DATA_OPTION_VALUE.
            McnpError: SEMANTICS_DATA_OPTION_VALUE.
            McnpError: SEMANTICS_DATA_OPTION_VALUE.
            McnpError: SEMANTICS_DATA_OPTION_VALUE.
            McnpError: SEMANTICS_DATA_OPTION_VALUE.
            McnpError: SEMANTICS_DATA_OPTION_VALUE.
            McnpError: SEMANTICS_DATA_OPTION_VALUE.
        """

        if mcal is None or mcal not in {'f', 'a'}:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_DATA_OPTION_VALUE, mcal)
        if igm is None or not (igm >= 0):
            raise errors.McnpError(errors.McnpCode.SEMANTICS_DATA_OPTION_VALUE, igm)
        if iplt is None or not (iplt == 0 or iplt == 1 or iplt == 2):
            raise errors.McnpError(errors.McnpCode.SEMANTICS_DATA_OPTION_VALUE, iplt)
        if iab is None or not (iab == 0 or iab == 1 or iab == 2):
            raise errors.McnpError(errors.McnpCode.SEMANTICS_DATA_OPTION_VALUE, iab)
        if icw is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_DATA_OPTION_VALUE, icw)
        if fnw is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_DATA_OPTION_VALUE, fnw)
        if rim is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_DATA_OPTION_VALUE, rim)

        self.value: typing.Final[tuple[any]] = types._Tuple([mcal, igm, iplt, iab, icw, fnw, rim])
        self.mcal: typing.Final[types.String] = mcal
        self.igm: typing.Final[types.Integer] = igm
        self.iplt: typing.Final[types.Integer] = iplt
        self.iab: typing.Final[types.Integer] = iab
        self.icw: typing.Final[types.Integer] = icw
        self.fnw: typing.Final[types.Real] = fnw
        self.rim: typing.Final[types.Real] = rim

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``DataOption_Mgopt`` from INP.

        Parameters:
            source: INP data card option.

        Returns:
            ``DataOption_Mgopt``.

        Raises:
            McnpError: SYNTAX_DATA_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = DataOption_Mgopt._REGEX.match(source)

        if not tokens:
            raise errors.McnpError(errors.McnpCode.SYNTAX_DATA_OPTION, source)

        mcal = types.String.from_mcnp(tokens[1])
        igm = types.Integer.from_mcnp(tokens[2])
        iplt = types.Integer.from_mcnp(tokens[3])
        iab = types.Integer.from_mcnp(tokens[4])
        icw = types.Integer.from_mcnp(tokens[5])
        fnw = types.Real.from_mcnp(tokens[6])
        rim = types.Real.from_mcnp(tokens[7])

        return DataOption_Mgopt(mcal, igm, iplt, iab, icw, fnw, rim)
