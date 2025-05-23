import re
import copy
import typing
import dataclasses


from ._option import CellOption
from ...utils import types
from ...utils import errors


class Fill_3(CellOption):
    """
    Represents INP fill variation #3 elements.

    Attributes:
        universe: Cell fill universe number.
        transformation: Cell fill transformation.
    """

    _KEYWORD = 'fill'

    _ATTRS = {
        'universe': types.Integer,
        'transformation': types.Transformation_2,
    }

    _REGEX = re.compile(
        rf'\Afill( {types.Integer._REGEX.pattern})( {types.Transformation_2._REGEX.pattern}| [(]{types.Transformation_2._REGEX.pattern}[)])?\Z'
    )

    def __init__(self, universe: types.Integer, transformation: types.Transformation_2 = None):
        """
        Initializes ``Fill_3``.

        Parameters:
            universe: Cell fill universe number.
            transformation: Cell fill transformation.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if universe is None or not (0 <= universe.value <= 99_999_999):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, universe)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                universe,
                transformation,
            ]
        )

        self.universe: typing.Final[types.Integer] = universe
        self.transformation: typing.Final[types.Transformation_2] = transformation


@dataclasses.dataclass
class FillBuilder_3:
    """
    Builds ``Fill_3``.

    Attributes:
        universe: Cell fill universe number.
        transformation: Cell fill transformation.
    """

    universe: str | int | types.Integer
    transformation: str | types.Transformation_2 = None

    def build(self):
        """
        Builds ``FillBuilder_3`` into ``Fill_3``.

        Returns:
            ``Fill_3`` for ``FillBuilder_3``.
        """

        universe = self.universe
        if isinstance(self.universe, types.Integer):
            universe = self.universe
        elif isinstance(self.universe, int):
            universe = types.Integer(self.universe)
        elif isinstance(self.universe, str):
            universe = types.Integer.from_mcnp(self.universe)

        transformation = self.transformation
        if isinstance(self.transformation, types.Transformation_2):
            transformation = self.transformation
        elif isinstance(self.transformation, str):
            transformation = types.Transformation_2.from_mcnp(self.transformation)

        return Fill_3(
            universe=universe,
            transformation=transformation,
        )

    @staticmethod
    def unbuild(ast: Fill_3):
        """
        Unbuilds ``Fill_3`` into ``FillBuilder_3``

        Returns:
            ``FillBuilder_3`` for ``Fill_3``.
        """

        return Fill_3(
            universe=copy.deepcopy(ast.universe),
            transformation=copy.deepcopy(ast.transformation),
        )
