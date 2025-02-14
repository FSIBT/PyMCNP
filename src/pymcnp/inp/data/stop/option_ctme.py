import re
import typing

from . import _option
from ....utils import types
from ....utils import errors
from ....utils import _parser


class StopOption_Ctme(_option.StopOption_, keyword='ctme'):
    """
    Represents INP data card data option ctme options.

    Attributes:
        tme: Computer time before stop.
    """

    _REGEX = re.compile(r'\Actme( \S+)\Z')

    def __init__(self, tme: types.Real):
        """
        Initializes ``StopOption_Ctme``.

        Parameters:
            tme: Computer time before stop.

        Returns:
            ``StopOption_Ctme``.

        Raises:
            McnpError: SEMANTICS_DATA_OPTION_VALUE.
        """

        if tme is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_DATA_OPTION_VALUE, tme)

        self.value: typing.Final[tuple[any]] = types._Tuple([tme])
        self.tme: typing.Final[types.Real] = tme

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``StopOption_Ctme`` from INP.

        Parameters:
            source: INP data card data option option.

        Returns:
            ``StopOption_Ctme``.

        Raises:
            McnpError: SYNTAX_STOP_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = StopOption_Ctme._REGEX.match(source)

        if not tokens:
            raise errors.McnpError(errors.McnpCode.SYNTAX_STOP_OPTION, source)

        tme = types.Real.from_mcnp(tokens[1])

        return StopOption_Ctme(tme)
