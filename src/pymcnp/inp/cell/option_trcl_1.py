import re
import typing

from . import trcl_1
from . import _option
from ...utils import types
from ...utils import errors
from ...utils import _parser


class CellOption_Trcl1(_option.CellOption_, keyword='trcl'):
    """
    Represents INP cell card trcl_1 options.

    Attributes:
        transformation: Cell transformation..
    """

    _REGEX = re.compile(
        r'\Atrcl( ( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+))\Z'
    )

    def __init__(self, transformation: trcl_1.Trcl1Entry_Transformation):
        """
        Initializes ``CellOption_Trcl1``.

        Parameters:
            transformation: Cell transformation..

        Returns:
            ``CellOption_Trcl1``.

        Raises:
            McnpError: SEMANTICS_CELL_OPTION_VALUE.
        """

        if transformation is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_CELL_OPTION_VALUE, transformation)

        self.value: typing.Final[tuple[any]] = types._Tuple([transformation])
        self.transformation: typing.Final[trcl_1.Trcl1Entry_Transformation] = transformation

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``CellOption_Trcl1`` from INP.

        Parameters:
            source: INP cell card option.

        Returns:
            ``CellOption_Trcl1``.

        Raises:
            McnpError: SYNTAX_CELL_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = CellOption_Trcl1._REGEX.match(source)

        if not tokens:
            raise errors.McnpError(errors.McnpCode.SYNTAX_CELL_OPTION, source)

        transformation = trcl_1.Trcl1Entry_Transformation.from_mcnp(tokens[1])

        return CellOption_Trcl1(transformation)
