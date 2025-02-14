import re
import typing

from . import fill_1
from . import _option
from ...utils import types
from ...utils import errors
from ...utils import _parser


class CellOption_Fill1(_option.CellOption_, keyword='fill'):
    """
    Represents INP cell card fill_1 options.

    Attributes:
        universe: Cell fill universe number.
        transformation: Cell fill transformation.
    """

    _REGEX = re.compile(
        r'\Afill( \S+)( ( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+))?\Z'
    )

    def __init__(
        self, universe: types.Integer, transformation: fill_1.Fill1Entry_Transformation = None
    ):
        """
        Initializes ``CellOption_Fill1``.

        Parameters:
            universe: Cell fill universe number.
            transformation: Cell fill transformation.

        Returns:
            ``CellOption_Fill1``.

        Raises:
            McnpError: SEMANTICS_CELL_OPTION_VALUE.
            McnpError: SEMANTICS_CELL_OPTION_VALUE.
        """

        if universe is None or not (0 <= universe <= 99_999_999):
            raise errors.McnpError(errors.McnpCode.SEMANTICS_CELL_OPTION_VALUE, universe)

        self.value: typing.Final[tuple[any]] = types._Tuple([universe, transformation])
        self.universe: typing.Final[types.Integer] = universe
        self.transformation: typing.Final[fill_1.Fill1Entry_Transformation] = transformation

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``CellOption_Fill1`` from INP.

        Parameters:
            source: INP cell card option.

        Returns:
            ``CellOption_Fill1``.

        Raises:
            McnpError: SYNTAX_CELL_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = CellOption_Fill1._REGEX.match(source)

        if not tokens:
            raise errors.McnpError(errors.McnpCode.SYNTAX_CELL_OPTION, source)

        universe = types.Integer.from_mcnp(tokens[1])
        transformation = (
            fill_1.Fill1Entry_Transformation.from_mcnp(tokens[2]) if tokens[2] else None
        )

        return CellOption_Fill1(universe, transformation)
