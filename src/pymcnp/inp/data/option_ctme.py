import re
import typing

from . import _option
from ...utils import types
from ...utils import errors
from ...utils import _parser


class DataOption_Ctme(_option.DataOption_, keyword='ctme'):
    """
    Represents INP data card ctme options.

    Attributes:
        tme: maximum amount of minutes for Monte Carlo calculation.
    """

    _REGEX = re.compile(r'\Actme( \S+)\Z')

    def __init__(self, tme: types.Integer):
        """
        Initializes ``DataOption_Ctme``.

        Parameters:
            tme: maximum amount of minutes for Monte Carlo calculation.

        Returns:
            ``DataOption_Ctme``.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if tme is None or not (tme >= 0):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, tme)

        self.value: typing.Final[tuple[any]] = types._Tuple([tme])
        self.tme: typing.Final[types.Integer] = tme

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``DataOption_Ctme`` from INP.

        Parameters:
            source: INP data card option.

        Returns:
            ``DataOption_Ctme``.

        Raises:
            InpError: SYNTAX_DATA_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = DataOption_Ctme._REGEX.match(source)

        if not tokens:
            raise errors.InpError(errors.InpCode.SYNTAX_OPTION, source)

        tme = types.Integer.from_mcnp(tokens[1])

        return DataOption_Ctme(tme)
