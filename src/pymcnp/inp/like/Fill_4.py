import re
import copy
import typing
import dataclasses


from . import _option
from ...utils import types
from ...utils import errors


class Fill_4(_option.LikeOption):
    """
    Represents INP fill variation #4 elements.

    Attributes:
        prefix: Star prefix.
        universe: Like fill universe number.
        transformation: Like fill transformation.
    """

    _KEYWORD = 'fill'

    _ATTRS = {
        'prefix': types.String,
        'universe': types.Integer,
        'transformation': types.Transformation_3,
    }

    _REGEX = re.compile(rf'\A([*])?fill( {types.Integer._REGEX.pattern[2:-2]})( {types.Transformation_3._REGEX.pattern[2:-2]}| [(]{types.Transformation_3._REGEX.pattern[2:-2]}[)])?\Z')

    def __init__(self, universe: types.Integer, prefix: types.String = None, transformation: types.Transformation_3 = None):
        """
        Initializes ``Fill_4``.

        Parameters:
            prefix: Star prefix.
            universe: Like fill universe number.
            transformation: Like fill transformation.

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
        self.transformation: typing.Final[types.Transformation_3] = transformation


@dataclasses.dataclass
class FillBuilder_4(_option.LikeOptionBuilder):
    """
    Builds ``Fill_4``.

    Attributes:
        prefix: Star prefix.
        universe: Like fill universe number.
        transformation: Like fill transformation.
    """

    universe: str | int | types.Integer
    prefix: str | types.String = None
    transformation: str | types.Transformation_3 = None

    def build(self):
        """
        Builds ``FillBuilder_4`` into ``Fill_4``.

        Returns:
            ``Fill_4`` for ``FillBuilder_4``.
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
        if isinstance(self.transformation, types.Transformation_3):
            transformation = self.transformation
        elif isinstance(self.transformation, str):
            transformation = types.Transformation_3.from_mcnp(self.transformation)

        return Fill_4(
            prefix=prefix,
            universe=universe,
            transformation=transformation,
        )

    @staticmethod
    def unbuild(ast: Fill_4):
        """
        Unbuilds ``Fill_4`` into ``FillBuilder_4``

        Returns:
            ``FillBuilder_4`` for ``Fill_4``.
        """

        return FillBuilder_4(
            prefix=copy.deepcopy(ast.prefix),
            universe=copy.deepcopy(ast.universe),
            transformation=copy.deepcopy(ast.transformation),
        )
