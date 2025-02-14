import re
import typing

from . import _option
from ...utils import types
from ...utils import errors
from ...utils import _parser


class CellOption_Bflcl(_option.CellOption_, keyword='bflcl'):
    """
    Represents INP cell card bflcl options.

    Attributes:
        number: Cell magnetic field number.
    """

    _REGEX = re.compile(r'\Abflcl( \S+)\Z')

    def __init__(self, number: types.Integer):
        """
        Initializes ``CellOption_Bflcl``.

        Parameters:
            number: Cell magnetic field number.

        Returns:
            ``CellOption_Bflcl``.

        Raises:
            McnpError: SEMANTICS_CELL_OPTION_VALUE.
        """

        if number is None or not (number >= 0):
            raise errors.McnpError(errors.McnpCode.SEMANTICS_CELL_OPTION_VALUE, number)

        self.value: typing.Final[tuple[any]] = types._Tuple([number])
        self.number: typing.Final[types.Integer] = number

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``CellOption_Bflcl`` from INP.

        Parameters:
            source: INP cell card option.

        Returns:
            ``CellOption_Bflcl``.

        Raises:
            McnpError: SYNTAX_CELL_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = CellOption_Bflcl._REGEX.match(source)

        if not tokens:
            raise errors.McnpError(errors.McnpCode.SYNTAX_CELL_OPTION, source)

        number = types.Integer.from_mcnp(tokens[1])

        return CellOption_Bflcl(number)
