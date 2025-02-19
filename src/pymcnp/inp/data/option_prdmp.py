import re
import typing

from . import _option
from ...utils import types
from ...utils import errors
from ...utils import _parser


class DataOption_Prdmp(_option.DataOption_, keyword='prdmp'):
    """
    Represents INP data card prdmp options.

    Attributes:
        ndp: Increment for printing tallies.
        ndm: Increment for dumping to RUNTPE file.
        mct: Controls printing of MCTAL file.
        ndmp: Maximum number of dumps on RUNTPE file.
        dmmp: Controls frequently of tally fluctuation chart.
    """

    _REGEX = re.compile(r'\Aprdmp( \S+)( \S+)( \S+)( \S+)( \S+)\Z')

    def __init__(
        self,
        ndp: types.Integer,
        ndm: types.Integer,
        mct: types.Integer,
        ndmp: types.Integer,
        dmmp: types.Integer,
    ):
        """
        Initializes ``DataOption_Prdmp``.

        Parameters:
            ndp: Increment for printing tallies.
            ndm: Increment for dumping to RUNTPE file.
            mct: Controls printing of MCTAL file.
            ndmp: Maximum number of dumps on RUNTPE file.
            dmmp: Controls frequently of tally fluctuation chart.

        Returns:
            ``DataOption_Prdmp``.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if ndp is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, ndp)
        if ndm is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, ndm)
        if mct is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, mct)
        if ndmp is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, ndmp)
        if dmmp is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, dmmp)

        self.value: typing.Final[tuple[any]] = types._Tuple([ndp, ndm, mct, ndmp, dmmp])
        self.ndp: typing.Final[types.Integer] = ndp
        self.ndm: typing.Final[types.Integer] = ndm
        self.mct: typing.Final[types.Integer] = mct
        self.ndmp: typing.Final[types.Integer] = ndmp
        self.dmmp: typing.Final[types.Integer] = dmmp

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``DataOption_Prdmp`` from INP.

        Parameters:
            source: INP data card option.

        Returns:
            ``DataOption_Prdmp``.

        Raises:
            InpError: SYNTAX_DATA_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = DataOption_Prdmp._REGEX.match(source)

        if not tokens:
            raise errors.InpError(errors.InpCode.SYNTAX_OPTION, source)

        ndp = types.Integer.from_mcnp(tokens[1])
        ndm = types.Integer.from_mcnp(tokens[2])
        mct = types.Integer.from_mcnp(tokens[3])
        ndmp = types.Integer.from_mcnp(tokens[4])
        dmmp = types.Integer.from_mcnp(tokens[5])

        return DataOption_Prdmp(ndp, ndm, mct, ndmp, dmmp)
