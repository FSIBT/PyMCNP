import re
import typing

from . import _option
from ...utils import types
from ...utils import errors
from ...utils import _parser


class CellOption_Lat(_option.CellOption_, keyword='lat'):
    """
    Represents INP cell card lat options.

    Attributes:
        shape: Cell lattice shape.
    """

    _REGEX = re.compile(r'\Alat( \S+)\Z')

    def __init__(self, shape: types.Integer):
        """
        Initializes ``CellOption_Lat``.

        Parameters:
            shape: Cell lattice shape.

        Returns:
            ``CellOption_Lat``.

        Raises:
            McnpError: SEMANTICS_CELL_OPTION_VALUE.
        """

        if shape is None or shape.value not in {1, 2}:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_CELL_OPTION_VALUE, shape)

        self.value: typing.Final[tuple[any]] = types._Tuple([shape])
        self.shape: typing.Final[types.Integer] = shape

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``CellOption_Lat`` from INP.

        Parameters:
            source: INP cell card option.

        Returns:
            ``CellOption_Lat``.

        Raises:
            McnpError: SYNTAX_CELL_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = CellOption_Lat._REGEX.match(source)

        if not tokens:
            raise errors.McnpError(errors.McnpCode.SYNTAX_CELL_OPTION, source)

        shape = types.Integer.from_mcnp(tokens[1])

        return CellOption_Lat(shape)
