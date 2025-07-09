import re
import copy
import typing
import dataclasses


from . import _option
from ...utils import types
from ...utils import errors


class Fill_6(_option.CellOption):
    """
    Represents INP fill variation #6 elements.

    Attributes:
        prefix: Star prefix.
        universe: Cell fill universe number.
        transformation: Cell fill transformation number.
    """

    _KEYWORD = 'fill'

    _ATTRS = {
        'prefix': types.String,
        'universe': types.Integer,
        'transformation': types.Integer,
    }

    _REGEX = re.compile(rf'\A([*])?fill( {types.Integer._REGEX.pattern[2:-2]})( {types.Integer._REGEX.pattern[2:-2]}| [(]{types.Integer._REGEX.pattern[2:-2]}[)])?\Z')

    def __init__(self, universe: types.Integer, prefix: types.String = None, transformation: types.Integer = None):
        """
        Initializes ``Fill_6``.

        Parameters:
            prefix: Star prefix.
            universe: Cell fill universe number.
            transformation: Cell fill transformation number.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if prefix is not None and prefix not in {'*'}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, prefix)
        if universe is None or not (universe >= 0 and universe <= 99_999_999):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, universe)
        if transformation is not None and not (transformation >= 0 and transformation <= 999):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, transformation)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                universe,
                transformation,
            ]
        )

        self.prefix: typing.Final[types.String] = prefix
        self.universe: typing.Final[types.Integer] = universe
        self.transformation: typing.Final[types.Integer] = transformation


@dataclasses.dataclass
class FillBuilder_6(_option.CellOptionBuilder):
    """
    Builds ``Fill_6``.

    Attributes:
        prefix: Star prefix.
        universe: Cell fill universe number.
        transformation: Cell fill transformation number.
    """

    universe: str | int | types.Integer
    prefix: str | types.String = None
    transformation: str | int | types.Integer = None

    def build(self):
        """
        Builds ``FillBuilder_6`` into ``Fill_6``.

        Returns:
            ``Fill_6`` for ``FillBuilder_6``.
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
        if isinstance(self.transformation, types.Integer):
            transformation = self.transformation
        elif isinstance(self.transformation, int):
            transformation = types.Integer(self.transformation)
        elif isinstance(self.transformation, str):
            transformation = types.Integer.from_mcnp(self.transformation)

        return Fill_6(
            prefix=prefix,
            universe=universe,
            transformation=transformation,
        )

    @staticmethod
    def unbuild(ast: Fill_6):
        """
        Unbuilds ``Fill_6`` into ``FillBuilder_6``

        Returns:
            ``FillBuilder_6`` for ``Fill_6``.
        """

        return FillBuilder_6(
            prefix=copy.deepcopy(ast.prefix),
            universe=copy.deepcopy(ast.universe),
            transformation=copy.deepcopy(ast.transformation),
        )
