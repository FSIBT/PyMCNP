import re
import typing

from . import _option
from ...utils import types
from ...utils import errors
from ...utils import _parser


class DataOption_Nps(_option.DataOption_, keyword='nps'):
    """
    Represents INP data card nps options.

    Attributes:
        npp: Total number of histories to run.
        npsmg: Number of history with direct source contributions.
    """

    _REGEX = re.compile(r'\Anps( \S+)( \S+)?\Z')

    def __init__(self, npp: types.Integer, npsmg: types.Integer = None):
        """
        Initializes ``DataOption_Nps``.

        Parameters:
            npp: Total number of histories to run.
            npsmg: Number of history with direct source contributions.

        Returns:
            ``DataOption_Nps``.

        Raises:
            McnpError: SEMANTICS_DATA_OPTION_VALUE.
            McnpError: SEMANTICS_DATA_OPTION_VALUE.
        """

        if npp is None or not (npp > 0):
            raise errors.McnpError(errors.McnpCode.SEMANTICS_DATA_OPTION_VALUE, npp)
        if npsmg is not None and not (npsmg > 0):
            raise errors.McnpError(errors.McnpCode.SEMANTICS_DATA_OPTION_VALUE, npsmg)

        self.value: typing.Final[tuple[any]] = types._Tuple([npp, npsmg])
        self.npp: typing.Final[types.Integer] = npp
        self.npsmg: typing.Final[types.Integer] = npsmg

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``DataOption_Nps`` from INP.

        Parameters:
            source: INP data card option.

        Returns:
            ``DataOption_Nps``.

        Raises:
            McnpError: SYNTAX_DATA_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = DataOption_Nps._REGEX.match(source)

        if not tokens:
            raise errors.McnpError(errors.McnpCode.SYNTAX_DATA_OPTION, source)

        npp = types.Integer.from_mcnp(tokens[1])
        npsmg = types.Integer.from_mcnp(tokens[2]) if tokens[2] else None

        return DataOption_Nps(npp, npsmg)
