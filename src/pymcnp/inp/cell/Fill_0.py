import re
import copy
import typing
import dataclasses


from ._option import CellOption
from ...utils import types
from ...utils import errors


class Fill_0(CellOption):
    """
    Represents INP fill variation #0 elements.

    Attributes:
        universe: Cell fill universe number.
        transformation: Cell fill transformation number.
    """

    _KEYWORD = 'fill'

    _ATTRS = {
        'universe': types.Integer,
        'transformation': types.Integer,
    }

    _REGEX = re.compile(
        rf'\Afill( {types.Integer._REGEX.pattern})( {types.Integer._REGEX.pattern}| [(]{types.Integer._REGEX.pattern}[)])?\Z'
    )

    def __init__(self, universe: types.Integer, transformation: types.Integer = None):
        """
        Initializes ``Fill_0``.

        Parameters:
            universe: Cell fill universe number.
            transformation: Cell fill transformation number.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if universe is None or not (0 <= universe.value <= 99_999_999):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, universe)
        if transformation is not None and not (0 <= transformation.value <= 999):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, transformation)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                universe,
                transformation,
            ]
        )

        self.universe: typing.Final[types.Integer] = universe
        self.transformation: typing.Final[types.Integer] = transformation


@dataclasses.dataclass
class FillBuilder_0:
    """
    Builds ``Fill_0``.

    Attributes:
        universe: Cell fill universe number.
        transformation: Cell fill transformation number.
    """

    universe: str | int | types.Integer
    transformation: str | int | types.Integer = None

    def build(self):
        """
        Builds ``FillBuilder_0`` into ``Fill_0``.

        Returns:
            ``Fill_0`` for ``FillBuilder_0``.
        """

        universe = self.universe
        if isinstance(self.universe, types.Integer):
            universe = self.universe
        elif isinstance(self.universe, int):
            universe = types.Integer(self.universe)
        elif isinstance(self.universe, str):
            universe = types.Integer.from_mcnp(self.universe)

        transformation = self.transformation
        if isinstance(self.transformation, types.Integer):
            transformation = self.transformation
        elif isinstance(self.transformation, int):
            transformation = types.Integer(self.transformation)
        elif isinstance(self.transformation, str):
            transformation = types.Integer.from_mcnp(self.transformation)

        return Fill_0(
            universe=universe,
            transformation=transformation,
        )

    @staticmethod
    def unbuild(ast: Fill_0):
        """
        Unbuilds ``Fill_0`` into ``FillBuilder_0``

        Returns:
            ``FillBuilder_0`` for ``Fill_0``.
        """

        return Fill_0(
            universe=copy.deepcopy(ast.universe),
            transformation=copy.deepcopy(ast.transformation),
        )
