import re
import typing

from . import _option
from ...utils import types
from ...utils import errors
from ...utils import _parser


class DataOption_Cosy(_option.DataOption_, keyword='cosy'):
    """
    Represents INP data card cosy options.

    Attributes:
        numbers: Tuple of COSY map numbers.
    """

    _REGEX = re.compile(r'\Acosy(( \S+)+)\Z')

    def __init__(self, numbers: tuple[types.Integer]):
        """
        Initializes ``DataOption_Cosy``.

        Parameters:
            numbers: Tuple of COSY map numbers.

        Returns:
            ``DataOption_Cosy``.

        Raises:
            McnpError: SEMANTICS_DATA_OPTION_VALUE.
        """

        if numbers is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_DATA_OPTION_VALUE, numbers)

        self.value: typing.Final[tuple[any]] = types._Tuple([numbers])
        self.numbers: typing.Final[tuple[types.Integer]] = numbers

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``DataOption_Cosy`` from INP.

        Parameters:
            source: INP data card option.

        Returns:
            ``DataOption_Cosy``.

        Raises:
            McnpError: SYNTAX_DATA_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = DataOption_Cosy._REGEX.match(source)

        if not tokens:
            raise errors.McnpError(errors.McnpCode.SYNTAX_DATA_OPTION, source)

        numbers = types._Tuple(
            [types.Integer.from_mcnp(token[0]) for token in re.finditer(r'( \S+)', tokens[1])]
        )

        return DataOption_Cosy(numbers)
