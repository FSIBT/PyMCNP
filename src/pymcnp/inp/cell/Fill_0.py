import re
import typing


from .option_ import CellOption_
from ...utils import types
from ...utils import errors


class Fill_0(CellOption_, keyword='fill'):
    """
    Represents INP fill_0 elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'universe': types.Integer,
        'transformation': types.Integer,
    }

    _REGEX = re.compile(rf'fill( {types.Integer._REGEX.pattern})( {types.Integer._REGEX.pattern})?')

    def __init__(self, universe: types.Integer, transformation: types.Integer = None):
        """
        Initializes ``Fill_0``.

        Parameters:
            universe: Cell fill universe number.
            transformation: Cell fill transformation number.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if universe is None or not (0 <= universe <= 99_999_999):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, universe)
        if transformation is not None and not (0 <= transformation <= 999):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, transformation)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                universe,
                transformation,
            ]
        )

        self.universe: typing.Final[types.Integer] = universe
        self.transformation: typing.Final[types.Integer] = transformation
