import re
import typing
import dataclasses


from ._option import SdefOption
from ....utils import types
from ....utils import errors


class Y(SdefOption):
    """
    Represents INP y elements.

    Attributes:
        y_coordinate: Y-cordinate of position.
    """

    _ATTRS = {
        'y_coordinate': types.RealOrJump,
    }

    _REGEX = re.compile(rf'\Ay( {types.RealOrJump._REGEX.pattern})\Z')

    def __init__(self, y_coordinate: types.RealOrJump):
        """
        Initializes ``Y``.

        Parameters:
            y_coordinate: Y-cordinate of position.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if y_coordinate is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, y_coordinate)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                y_coordinate,
            ]
        )

        self.y_coordinate: typing.Final[types.RealOrJump] = y_coordinate


@dataclasses.dataclass
class YBuilder:
    """
    Builds ``Y``.

    Attributes:
        y_coordinate: Y-cordinate of position.
    """

    y_coordinate: str | float | types.RealOrJump

    def build(self):
        """
        Builds ``YBuilder`` into ``Y``.

        Returns:
            ``Y`` for ``YBuilder``.
        """

        y_coordinate = self.y_coordinate
        if isinstance(self.y_coordinate, types.Real):
            y_coordinate = self.y_coordinate
        elif isinstance(self.y_coordinate, float) or isinstance(self.y_coordinate, int):
            y_coordinate = types.RealOrJump(self.y_coordinate)
        elif isinstance(self.y_coordinate, str):
            y_coordinate = types.RealOrJump.from_mcnp(self.y_coordinate)

        return Y(
            y_coordinate=y_coordinate,
        )
