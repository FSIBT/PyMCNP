import re
import typing

from . import _option
from ...utils import types
from ...utils import errors
from ...utils import _parser


class DataOption_Za(_option.DataOption_, keyword='za'):
    """
    Represents INP data card za options.

    Attributes:
        anything: Any parameters.
    """

    _REGEX = re.compile(r'\Aza( \S+)?\Z')

    def __init__(self, anything: types.String = None):
        """
        Initializes ``DataOption_Za``.

        Parameters:
            anything: Any parameters.

        Returns:
            ``DataOption_Za``.

        Raises:
            McnpError: SEMANTICS_DATA_OPTION_VALUE.
        """

        self.value: typing.Final[tuple[any]] = types._Tuple([anything])
        self.anything: typing.Final[types.String] = anything

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``DataOption_Za`` from INP.

        Parameters:
            source: INP data card option.

        Returns:
            ``DataOption_Za``.

        Raises:
            McnpError: SYNTAX_DATA_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = DataOption_Za._REGEX.match(source)

        if not tokens:
            raise errors.McnpError(errors.McnpCode.SYNTAX_DATA_OPTION, source)

        anything = types.String.from_mcnp(tokens[1]) if tokens[1] else None

        return DataOption_Za(anything)
