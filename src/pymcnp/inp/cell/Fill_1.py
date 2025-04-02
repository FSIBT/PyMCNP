import re
import typing


from .option_ import CellOption_
from ...utils import types
from ...utils import errors


class Fill_1(CellOption_, keyword='fill'):
    """
    Represents INP fill_1 elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'universe': types.Integer,
        'transformation': types.Transformation,
    }

    _REGEX = re.compile(
        rf'\Afill( {types.Integer._REGEX.pattern})( {types.Transformation._REGEX.pattern})?\Z'
    )

    def __init__(self, universe: types.Integer, transformation: types.Transformation = None):
        """
        Initializes ``Fill_1``.

        Parameters:
            universe: Cell fill universe number.
            transformation: Cell fill transformation.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if universe is None or not (0 <= universe <= 99_999_999):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, universe)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                universe,
                transformation,
            ]
        )

        self.universe: typing.Final[types.Integer] = universe
        self.transformation: typing.Final[types.Transformation] = transformation
