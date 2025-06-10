import re
import copy
import typing
import dataclasses


from . import _option
from ...utils import types
from ...utils import errors


class Fill_3(_option.CellOption):
    """
    Represents INP fill variation #3 elements.

    Attributes:
        prefix: Star prefix.
        universe: Cell fill universe number.
        transformation: Cell fill transformation.
    """

    _KEYWORD = 'fill'

    _ATTRS = {
        'prefix': types.String,
        'universe': types.Integer,
        'transformation': types.Transformation_2,
    }

    _REGEX = re.compile(rf'\A([*])?fill( {types.Integer._REGEX.pattern[2:-2]})( {types.Transformation_2._REGEX.pattern[2:-2]}| [(]{types.Transformation_2._REGEX.pattern[2:-2]}[)])?\Z')

    def __init__(self, universe: types.Integer, prefix: types.String = None, transformation: types.Transformation_2 = None):
        """
        Initializes ``Fill_3``.

        Parameters:
            prefix: Star prefix.
            universe: Cell fill universe number.
            transformation: Cell fill transformation.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if prefix is not None and prefix.value not in {'*'}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, prefix)
        if universe is None or not (0 <= universe.value <= 99_999_999):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, universe)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                universe,
                transformation,
            ]
        )

        self.prefix: typing.Final[types.String] = prefix
        self.universe: typing.Final[types.Integer] = universe
        self.transformation: typing.Final[types.Transformation_2] = transformation


@dataclasses.dataclass
class FillBuilder_3(_option.CellOptionBuilder):
    """
    Builds ``Fill_3``.

    Attributes:
        prefix: Star prefix.
        universe: Cell fill universe number.
        transformation: Cell fill transformation.
    """

    universe: str | int | types.Integer
    prefix: str | types.String = None
    transformation: str | types.Transformation_2 = None

    def build(self):
        """
        Builds ``FillBuilder_3`` into ``Fill_3``.

        Returns:
            ``Fill_3`` for ``FillBuilder_3``.
        """

        prefix = self.prefix
        if isinstance(self.prefix, types.String):
            prefix = self.prefix
        elif isinstance(self.prefix, str):
            prefix = types.String.from_mcnp(self.prefix)

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
            prefix=prefix,
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

        return FillBuilder_3(
            prefix=copy.deepcopy(ast.prefix),
            universe=copy.deepcopy(ast.universe),
            transformation=copy.deepcopy(ast.transformation),
        )
