import re
import typing
import dataclasses


from ._option import SdefOption
from ....utils import types
from ....utils import errors


class X(SdefOption, keyword='x'):
    """
    Represents INP x elements.

    Attributes:
        x_coordinate: X-cordinate of position.
    """

    _ATTRS = {
        'x_coordinate': types.RealOrJump,
    }

    _REGEX = re.compile(rf'\Ax( {types.RealOrJump._REGEX.pattern})\Z')

    def __init__(self, x_coordinate: types.RealOrJump):
        """
        Initializes ``X``.

        Parameters:
            x_coordinate: X-cordinate of position.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if x_coordinate is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, x_coordinate)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                x_coordinate,
            ]
        )

        self.x_coordinate: typing.Final[types.RealOrJump] = x_coordinate


@dataclasses.dataclass
class XBuilder:
    """
    Builds ``X``.

    Attributes:
        x_coordinate: X-cordinate of position.
    """

    x_coordinate: str | float | types.RealOrJump

    def build(self):
        """
        Builds ``XBuilder`` into ``X``.

        Returns:
            ``X`` for ``XBuilder``.
        """

        if isinstance(self.x_coordinate, types.Real):
            x_coordinate = self.x_coordinate
        elif isinstance(self.x_coordinate, float) or isinstance(self.x_coordinate, int):
            x_coordinate = types.RealOrJump(self.x_coordinate)
        elif isinstance(self.x_coordinate, str):
            x_coordinate = types.RealOrJump.from_mcnp(self.x_coordinate)

        return X(
            x_coordinate=x_coordinate,
        )
