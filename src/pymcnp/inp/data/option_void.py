import re
import typing

from . import _option
from ...utils import types
from ...utils import errors
from ...utils import _parser


class DataOption_Void(_option.DataOption_, keyword='void'):
    """
    Represents INP data card void options.

    Attributes:
        numbers: Tuple of cell numbers.
    """

    _REGEX = re.compile(r'\Avoid(( \S+)+)?\Z')

    def __init__(self, numbers: tuple[types.Integer] = None):
        """
        Initializes ``DataOption_Void``.

        Parameters:
            numbers: Tuple of cell numbers.

        Returns:
            ``DataOption_Void``.

        Raises:
            McnpError: SEMANTICS_DATA_OPTION_VALUE.
        """

        if numbers is not None and not (
            filter(lambda entry: not (1 <= entry <= 99_999_999), numbers)
        ):
            raise errors.McnpError(errors.McnpCode.SEMANTICS_DATA_OPTION_VALUE, numbers)

        self.value: typing.Final[tuple[any]] = types._Tuple([numbers])
        self.numbers: typing.Final[tuple[types.Integer]] = numbers

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``DataOption_Void`` from INP.

        Parameters:
            source: INP data card option.

        Returns:
            ``DataOption_Void``.

        Raises:
            McnpError: SYNTAX_DATA_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = DataOption_Void._REGEX.match(source)

        if not tokens:
            raise errors.McnpError(errors.McnpCode.SYNTAX_DATA_OPTION, source)

        numbers = (
            types._Tuple(
                [types.Integer.from_mcnp(token[0]) for token in re.finditer(r'( \S+)', tokens[1])]
            )
            if tokens[1]
            else None
        )

        return DataOption_Void(numbers)
