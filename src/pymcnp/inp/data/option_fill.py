import re
import typing

from . import _option
from ...utils import types
from ...utils import errors
from ...utils import _parser


class DataOption_Fill(_option.DataOption_, keyword='fill'):
    """
    Represents INP data card fill options.

    Attributes:
        numbers: Tuple of universe numbers.
    """

    _REGEX = re.compile(r'\Afill(( \S+)+)\Z')

    def __init__(self, numbers: tuple[types.Integer]):
        """
        Initializes ``DataOption_Fill``.

        Parameters:
            numbers: Tuple of universe numbers.

        Returns:
            ``DataOption_Fill``.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if numbers is None or not (filter(lambda entry: not (0 <= entry <= 99_999_999), numbers)):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, numbers)

        self.value: typing.Final[tuple[any]] = types._Tuple([numbers])
        self.numbers: typing.Final[tuple[types.Integer]] = numbers

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``DataOption_Fill`` from INP.

        Parameters:
            source: INP data card option.

        Returns:
            ``DataOption_Fill``.

        Raises:
            InpError: SYNTAX_DATA_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = DataOption_Fill._REGEX.match(source)

        if not tokens:
            raise errors.InpError(errors.InpCode.SYNTAX_OPTION, source)

        numbers = types._Tuple(
            [types.Integer.from_mcnp(token[0]) for token in re.finditer(r'( \S+)', tokens[1])]
        )

        return DataOption_Fill(numbers)
