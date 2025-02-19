import re
import typing

from . import _option
from ...utils import types
from ...utils import errors
from ...utils import _parser


class CellOption_Fill0(_option.CellOption_, keyword='fill'):
    """
    Represents INP cell card fill_0 options.

    Attributes:
        universe: Cell fill universe number.
        transformation: Cell fill transformation number.
    """

    _REGEX = re.compile(r'\Afill( \S+)( \S+)?\Z')

    def __init__(self, universe: types.Integer, transformation: types.Integer = None):
        """
        Initializes ``CellOption_Fill0``.

        Parameters:
            universe: Cell fill universe number.
            transformation: Cell fill transformation number.

        Returns:
            ``CellOption_Fill0``.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if universe is None or not (0 <= universe <= 99_999_999):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, universe)
        if transformation is not None and not (0 <= transformation <= 999):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, transformation)

        self.value: typing.Final[tuple[any]] = types._Tuple([universe, transformation])
        self.universe: typing.Final[types.Integer] = universe
        self.transformation: typing.Final[types.Integer] = transformation

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``CellOption_Fill0`` from INP.

        Parameters:
            source: INP cell card option.

        Returns:
            ``CellOption_Fill0``.

        Raises:
            InpError: SYNTAX_CELL_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = CellOption_Fill0._REGEX.match(source)

        if not tokens:
            raise errors.InpError(errors.InpCode.SYNTAX_OPTION, source)

        universe = types.Integer.from_mcnp(tokens[1])
        transformation = types.Integer.from_mcnp(tokens[2]) if tokens[2] else None

        return CellOption_Fill0(universe, transformation)
