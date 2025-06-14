import re
import copy
import typing
import dataclasses


from . import _option
from ....utils import types
from ....utils import errors


class X(_option.SdefOption):
    """
    Represents INP x elements.

    Attributes:
        x_coordinate: X-cordinate of position.
    """

    _KEYWORD = 'x'

    _ATTRS = {
        'x_coordinate': types.Real,
    }

    _REGEX = re.compile(rf'\Ax( {types.Real._REGEX.pattern[2:-2]})\Z')

    def __init__(self, x_coordinate: types.Real):
        """
        Initializes ``X``.

        Parameters:
            x_coordinate: X-cordinate of position.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if x_coordinate is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, x_coordinate)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                x_coordinate,
            ]
        )

        self.x_coordinate: typing.Final[types.Real] = x_coordinate


@dataclasses.dataclass
class XBuilder(_option.SdefOptionBuilder):
    """
    Builds ``X``.

    Attributes:
        x_coordinate: X-cordinate of position.
    """

    x_coordinate: str | float | types.Real

    def build(self):
        """
        Builds ``XBuilder`` into ``X``.

        Returns:
            ``X`` for ``XBuilder``.
        """

        x_coordinate = self.x_coordinate
        if isinstance(self.x_coordinate, types.Real):
            x_coordinate = self.x_coordinate
        elif isinstance(self.x_coordinate, float) or isinstance(self.x_coordinate, int):
            x_coordinate = types.Real(self.x_coordinate)
        elif isinstance(self.x_coordinate, str):
            x_coordinate = types.Real.from_mcnp(self.x_coordinate)

        return X(
            x_coordinate=x_coordinate,
        )

    @staticmethod
    def unbuild(ast: X):
        """
        Unbuilds ``X`` into ``XBuilder``

        Returns:
            ``XBuilder`` for ``X``.
        """

        return XBuilder(
            x_coordinate=copy.deepcopy(ast.x_coordinate),
        )
