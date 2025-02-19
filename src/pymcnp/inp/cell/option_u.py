import re
import typing

from . import _option
from ...utils import types
from ...utils import errors
from ...utils import _parser


class CellOption_U(_option.CellOption_, keyword='u'):
    """
    Represents INP cell card u options.

    Attributes:
        number: Cell universe number.
    """

    _REGEX = re.compile(r'\Au( \S+)\Z')

    def __init__(self, number: types.Integer):
        """
        Initializes ``CellOption_U``.

        Parameters:
            number: Cell universe number.

        Returns:
            ``CellOption_U``.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if number is None or not (-99_999_999 <= number <= 99_999_999):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, number)

        self.value: typing.Final[tuple[any]] = types._Tuple([number])
        self.number: typing.Final[types.Integer] = number

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``CellOption_U`` from INP.

        Parameters:
            source: INP cell card option.

        Returns:
            ``CellOption_U``.

        Raises:
            InpError: SYNTAX_CELL_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = CellOption_U._REGEX.match(source)

        if not tokens:
            raise errors.InpError(errors.InpCode.SYNTAX_OPTION, source)

        number = types.Integer.from_mcnp(tokens[1])

        return CellOption_U(number)
