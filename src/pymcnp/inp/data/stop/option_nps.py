import re
import typing

from . import _option
from ....utils import types
from ....utils import errors
from ....utils import _parser


class StopOption_Nps(_option.StopOption_, keyword='nps'):
    """
    Represents INP data card data option nps options.

    Attributes:
        npp: Total number of histories before stop.
        npsmg: Number of histories before stop.
    """

    _REGEX = re.compile(r'\Anps( \S+)( \S+)?\Z')

    def __init__(self, npp: types.Integer, npsmg: types.Integer = None):
        """
        Initializes ``StopOption_Nps``.

        Parameters:
            npp: Total number of histories before stop.
            npsmg: Number of histories before stop.

        Returns:
            ``StopOption_Nps``.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if npp is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, npp)

        self.value: typing.Final[tuple[any]] = types._Tuple([npp, npsmg])
        self.npp: typing.Final[types.Integer] = npp
        self.npsmg: typing.Final[types.Integer] = npsmg

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``StopOption_Nps`` from INP.

        Parameters:
            source: INP data card data option option.

        Returns:
            ``StopOption_Nps``.

        Raises:
            InpError: SYNTAX_STOP_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = StopOption_Nps._REGEX.match(source)

        if not tokens:
            raise errors.InpError(errors.InpCode.SYNTAX_OPTION, source)

        npp = types.Integer.from_mcnp(tokens[1])
        npsmg = types.Integer.from_mcnp(tokens[2]) if tokens[2] else None

        return StopOption_Nps(npp, npsmg)
