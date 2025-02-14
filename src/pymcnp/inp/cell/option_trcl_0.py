import re
import typing

from . import _option
from ...utils import types
from ...utils import errors
from ...utils import _parser


class CellOption_Trcl0(_option.CellOption_, keyword='trcl'):
    """
    Represents INP cell card trcl_0 options.

    Attributes:
        transformation: Cell transformation number.
    """

    _REGEX = re.compile(r'\Atrcl( \S+)\Z')

    def __init__(self, transformation: types.Integer):
        """
        Initializes ``CellOption_Trcl0``.

        Parameters:
            transformation: Cell transformation number.

        Returns:
            ``CellOption_Trcl0``.

        Raises:
            McnpError: SEMANTICS_CELL_OPTION_VALUE.
        """

        if transformation is None or not (1 <= transformation <= 999):
            raise errors.McnpError(errors.McnpCode.SEMANTICS_CELL_OPTION_VALUE, transformation)

        self.value: typing.Final[tuple[any]] = types._Tuple([transformation])
        self.transformation: typing.Final[types.Integer] = transformation

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``CellOption_Trcl0`` from INP.

        Parameters:
            source: INP cell card option.

        Returns:
            ``CellOption_Trcl0``.

        Raises:
            McnpError: SYNTAX_CELL_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = CellOption_Trcl0._REGEX.match(source)

        if not tokens:
            raise errors.McnpError(errors.McnpCode.SYNTAX_CELL_OPTION, source)

        transformation = types.Integer.from_mcnp(tokens[1])

        return CellOption_Trcl0(transformation)
