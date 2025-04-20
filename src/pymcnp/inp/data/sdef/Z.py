import re
import typing
import dataclasses


from .option_ import SdefOption_
from ....utils import types
from ....utils import errors


class Z(SdefOption_, keyword='z'):
    """
    Represents INP z elements.

    Attributes:
        z_coordinate: Z-cordinate of position.
    """

    _ATTRS = {
        'z_coordinate': types.RealOrJump,
    }

    _REGEX = re.compile(rf'\Az( {types.RealOrJump._REGEX.pattern})\Z')

    def __init__(self, z_coordinate: types.RealOrJump):
        """
        Initializes ``Z``.

        Parameters:
            z_coordinate: Z-cordinate of position.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if z_coordinate is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, z_coordinate)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                z_coordinate,
            ]
        )

        self.z_coordinate: typing.Final[types.RealOrJump] = z_coordinate


@dataclasses.dataclass
class ZBuilder:
    """
    Builds ``Z``.

    Attributes:
        z_coordinate: Z-cordinate of position.
    """

    z_coordinate: str | float | types.RealOrJump

    def build(self):
        """
        Builds ``ZBuilder`` into ``Z``.

        Returns:
            ``Z`` for ``ZBuilder``.
        """

        if isinstance(self.z_coordinate, types.Real):
            z_coordinate = self.z_coordinate
        elif isinstance(self.z_coordinate, float) or isinstance(self.z_coordinate, int):
            z_coordinate = types.RealOrJump(self.z_coordinate)
        elif isinstance(self.z_coordinate, str):
            z_coordinate = types.RealOrJump.from_mcnp(self.z_coordinate)

        return Z(
            z_coordinate=z_coordinate,
        )
