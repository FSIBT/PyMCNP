import re
import typing
import dataclasses


from .option_ import CellOption_
from ...utils import types
from ...utils import errors


class Fill_0(CellOption_, keyword='fill'):
    """
    Represents INP fill variation #0 elements.

    Attributes:
        universe: Cell fill universe number.
        transformation: Cell fill transformation number.
    """

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

        if isinstance(self.universe, types.Integer):
            universe = self.universe
        elif isinstance(self.universe, int):
            universe = types.Integer(self.universe)
        elif isinstance(self.universe, str):
            universe = types.Integer.from_mcnp(self.universe)

        transformation = None
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
