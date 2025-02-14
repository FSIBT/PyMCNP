import re
import typing

from . import _option
from ...utils import types
from ...utils import errors
from ...utils import _parser


class CellOption_Cosy(_option.CellOption_, keyword='cosy'):
    """
    Represents INP cell card cosy options.

    Attributes:
        number: Cell cosy map number.
    """

    _REGEX = re.compile(r'\Acosy( \S+)\Z')

    def __init__(self, number: types.Integer):
        """
        Initializes ``CellOption_Cosy``.

        Parameters:
            number: Cell cosy map number.

        Returns:
            ``CellOption_Cosy``.

        Raises:
            McnpError: SEMANTICS_CELL_OPTION_VALUE.
        """

        if number is None or number.value not in {1, 2, 3, 4, 5, 6}:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_CELL_OPTION_VALUE, number)

        self.value: typing.Final[tuple[any]] = types._Tuple([number])
        self.number: typing.Final[types.Integer] = number

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``CellOption_Cosy`` from INP.

        Parameters:
            source: INP cell card option.

        Returns:
            ``CellOption_Cosy``.

        Raises:
            McnpError: SYNTAX_CELL_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = CellOption_Cosy._REGEX.match(source)

        if not tokens:
            raise errors.McnpError(errors.McnpCode.SYNTAX_CELL_OPTION, source)

        number = types.Integer.from_mcnp(tokens[1])

        return CellOption_Cosy(number)
