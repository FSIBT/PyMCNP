import re
import typing
import dataclasses


from ._option import CellOption
from ...utils import types
from ...utils import errors


class Fill_4(CellOption, keyword='fill'):
    """
    Represents INP fill variation #4 elements.

    Attributes:
        universe: Cell fill universe number.
        transformation: Cell fill transformation.
    """

    _ATTRS = {
        'universe': types.Integer,
        'transformation': types.Transformation_3,
    }

    _REGEX = re.compile(
        rf'\Afill( {types.Integer._REGEX.pattern})( {types.Transformation_3._REGEX.pattern}| [(]{types.Transformation_3._REGEX.pattern}[)])?\Z'
    )

    def __init__(self, universe: types.Integer, transformation: types.Transformation_3 = None):
        """
        Initializes ``Fill_4``.

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
        self.transformation: typing.Final[types.Transformation_3] = transformation


@dataclasses.dataclass
class FillBuilder_4:
    """
    Builds ``Fill_4``.

    Attributes:
        universe: Cell fill universe number.
        transformation: Cell fill transformation.
    """

    universe: str | int | types.Integer
    transformation: str | types.Transformation_3 = None

    def build(self):
        """
        Builds ``FillBuilder_4`` into ``Fill_4``.

        Returns:
            ``Fill_4`` for ``FillBuilder_4``.
        """

        if isinstance(self.universe, types.Integer):
            universe = self.universe
        elif isinstance(self.universe, int):
            universe = types.Integer(self.universe)
        elif isinstance(self.universe, str):
            universe = types.Integer.from_mcnp(self.universe)

        transformation = None
        if isinstance(self.transformation, types.Transformation_3):
            transformation = self.transformation
        elif isinstance(self.transformation, str):
            transformation = types.Transformation_3.from_mcnp(self.transformation)

        return Fill_4(
            universe=universe,
            transformation=transformation,
        )
