import re
import copy
import typing
import dataclasses


from . import _option
from ...utils import types
from ...utils import errors


class Fill_2(_option.CellOption):
    """
    Represents INP fill variation #2 elements.

    Attributes:
        prefix: Star prefix.
        universe: Cell fill universe number.
        transformation: Cell fill transformation.
    """

    _KEYWORD = 'fill'

    _ATTRS = {
        'prefix': types.String,
        'universe': types.Integer,
        'transformation': types.Transformation_1,
    }

    _REGEX = re.compile(rf'\A([*])?fill( {types.Integer._REGEX.pattern[2:-2]})( {types.Transformation_1._REGEX.pattern[2:-2]}| [(]{types.Transformation_1._REGEX.pattern[2:-2]}[)])?\Z')

    def __init__(self, universe: types.Integer, prefix: types.String = None, transformation: types.Transformation_1 = None):
        """
        Initializes ``Fill_2``.

        Parameters:
            prefix: Star prefix.
            universe: Cell fill universe number.
            transformation: Cell fill transformation.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if prefix is not None and prefix not in {'*'}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, prefix)
        if universe is None or not (universe == 10000000000 or (universe >= 0 and universe <= 99_999_999)):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, universe)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                universe,
                transformation,
            ]
        )

        self.prefix: typing.Final[types.String] = prefix
        self.universe: typing.Final[types.Integer] = universe
        self.transformation: typing.Final[types.Transformation_1] = transformation


@dataclasses.dataclass
class FillBuilder_2(_option.CellOptionBuilder):
    """
    Builds ``Fill_2``.

    Attributes:
        prefix: Star prefix.
        universe: Cell fill universe number.
        transformation: Cell fill transformation.
    """

    universe: str | int | types.Integer
    prefix: str | types.String = None
    transformation: str | types.Transformation_1 = None

    def build(self):
        """
        Builds ``FillBuilder_2`` into ``Fill_2``.

        Returns:
            ``Fill_2`` for ``FillBuilder_2``.
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
        if isinstance(self.transformation, types.Transformation_1):
            transformation = self.transformation
        elif isinstance(self.transformation, str):
            transformation = types.Transformation_1.from_mcnp(self.transformation)

        return Fill_2(
            prefix=prefix,
            universe=universe,
            transformation=transformation,
        )

    @staticmethod
    def unbuild(ast: Fill_2):
        """
        Unbuilds ``Fill_2`` into ``FillBuilder_2``

        Returns:
            ``FillBuilder_2`` for ``Fill_2``.
        """

        return FillBuilder_2(
            prefix=copy.deepcopy(ast.prefix),
            universe=copy.deepcopy(ast.universe),
            transformation=copy.deepcopy(ast.transformation),
        )
