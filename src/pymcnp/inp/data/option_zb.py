import re
import typing

from . import _option
from ...utils import types
from ...utils import errors
from ...utils import _parser


class DataOption_Zb(_option.DataOption_, keyword='zb'):
    """
    Represents INP data card zb options.

    Attributes:
        anything: Any parameters.
    """

    _REGEX = re.compile(r'\Azb( \S+)?\Z')

    def __init__(self, anything: types.String = None):
        """
        Initializes ``DataOption_Zb``.

        Parameters:
            anything: Any parameters.

        Returns:
            ``DataOption_Zb``.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        self.value: typing.Final[tuple[any]] = types._Tuple([anything])
        self.anything: typing.Final[types.String] = anything

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``DataOption_Zb`` from INP.

        Parameters:
            source: INP data card option.

        Returns:
            ``DataOption_Zb``.

        Raises:
            InpError: SYNTAX_DATA_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = DataOption_Zb._REGEX.match(source)

        if not tokens:
            raise errors.InpError(errors.InpCode.SYNTAX_OPTION, source)

        anything = types.String.from_mcnp(tokens[1]) if tokens[1] else None

        return DataOption_Zb(anything)
