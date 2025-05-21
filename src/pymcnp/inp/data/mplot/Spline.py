import re
import copy
import typing
import dataclasses


from ._option import MplotOption
from ....utils import types


class Spline(MplotOption):
    """
    Represents INP spline elements.

    Attributes:
        x: Tension of rational splines.
    """

    _KEYWORD = 'spline'

    _ATTRS = {
        'x': types.Real,
    }

    _REGEX = re.compile(rf'\Aspline( {types.Real._REGEX.pattern})?\Z')

    def __init__(self, x: types.Real = None):
        """
        Initializes ``Spline``.

        Parameters:
            x: Tension of rational splines.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                x,
            ]
        )

        self.x: typing.Final[types.Real] = x


@dataclasses.dataclass
class SplineBuilder:
    """
    Builds ``Spline``.

    Attributes:
        x: Tension of rational splines.
    """

    x: str | float | types.Real = None

    def build(self):
        """
        Builds ``SplineBuilder`` into ``Spline``.

        Returns:
            ``Spline`` for ``SplineBuilder``.
        """

        x = self.x
        if isinstance(self.x, types.Real):
            x = self.x
        elif isinstance(self.x, float) or isinstance(self.x, int):
            x = types.Real(self.x)
        elif isinstance(self.x, str):
            x = types.Real.from_mcnp(self.x)

        return Spline(
            x=x,
        )

    @staticmethod
    def unbuild(ast: Spline):
        """
        Unbuilds ``Spline`` into ``SplineBuilder``

        Returns:
            ``SplineBuilder`` for ``Spline``.
        """

        return Spline(
            x=copy.deepcopy(ast.x),
        )
