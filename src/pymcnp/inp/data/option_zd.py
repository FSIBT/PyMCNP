import re
import typing

from . import _option
from ...utils import types
from ...utils import errors
from ...utils import _parser


class DataOption_Zd(_option.DataOption_, keyword='zd'):
    """
    Represents INP data card zd options.

    Attributes:
        anything: Any parameters.
    """

    _REGEX = re.compile(r'\Azd( \S+)?\Z')

    def __init__(self, anything: types.String = None):
        """
        Initializes ``DataOption_Zd``.

        Parameters:
            anything: Any parameters.

        Returns:
            ``DataOption_Zd``.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        self.value: typing.Final[tuple[any]] = types._Tuple([anything])
        self.anything: typing.Final[types.String] = anything

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``DataOption_Zd`` from INP.

        Parameters:
            source: INP data card option.

        Returns:
            ``DataOption_Zd``.

        Raises:
            InpError: SYNTAX_DATA_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = DataOption_Zd._REGEX.match(source)

        if not tokens:
            raise errors.InpError(errors.InpCode.SYNTAX_OPTION, source)

        anything = types.String.from_mcnp(tokens[1]) if tokens[1] else None

        return DataOption_Zd(anything)
