import re
import typing
import dataclasses


from ._option import CellOption
from ...utils import types
from ...utils import errors


class Fill_1(CellOption):
    """
    Represents INP fill variation #1 elements.

    Attributes:
        universe: Cell fill universe number.
        transformation: Cell fill transformation.
    """

    _ATTRS = {
        'universe': types.Integer,
        'transformation': types.Transformation_0,
    }

    _REGEX = re.compile(
        rf'\Afill( {types.Integer._REGEX.pattern})( {types.Transformation_0._REGEX.pattern}| [(]{types.Transformation_0._REGEX.pattern}[)])?\Z'
    )

    def __init__(self, universe: types.Integer, transformation: types.Transformation_0 = None):
        """
        Initializes ``Fill_1``.

        Parameters:
            universe: Cell fill universe number.
            transformation: Cell fill transformation.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if universe is None or not (0 <= universe <= 99_999_999):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, universe)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                universe,
                transformation,
            ]
        )

        self.universe: typing.Final[types.Integer] = universe
        self.transformation: typing.Final[types.Transformation_0] = transformation


@dataclasses.dataclass
class FillBuilder_1:
    """
    Builds ``Fill_1``.

    Attributes:
        universe: Cell fill universe number.
        transformation: Cell fill transformation.
    """

    universe: str | int | types.Integer
    transformation: str | types.Transformation_0 = None

    def build(self):
        """
        Builds ``FillBuilder_1`` into ``Fill_1``.

        Returns:
            ``Fill_1`` for ``FillBuilder_1``.
        """

        if isinstance(self.universe, types.Integer):
            universe = self.universe
        elif isinstance(self.universe, int):
            universe = types.Integer(self.universe)
        elif isinstance(self.universe, str):
            universe = types.Integer.from_mcnp(self.universe)

        transformation = None
        if isinstance(self.transformation, types.Transformation_0):
            transformation = self.transformation
        elif isinstance(self.transformation, str):
            transformation = types.Transformation_0.from_mcnp(self.transformation)

        return Fill_1(
            universe=universe,
            transformation=transformation,
        )
