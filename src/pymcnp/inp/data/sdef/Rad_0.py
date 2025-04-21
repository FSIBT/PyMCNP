import re
import typing
import dataclasses


from ._option import SdefOption
from ....utils import types
from ....utils import errors


class Rad_0(SdefOption, keyword='rad'):
    """
    Represents INP rad variation #0 elements.

    Attributes:
        radial_distance: Radial distance fo the position from POS or AXS.
    """

    _ATTRS = {
        'radial_distance': types.RealOrJump,
    }

    _REGEX = re.compile(rf'\Arad( {types.RealOrJump._REGEX.pattern})\Z')

    def __init__(self, radial_distance: types.RealOrJump):
        """
        Initializes ``Rad_0``.

        Parameters:
            radial_distance: Radial distance fo the position from POS or AXS.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if radial_distance is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, radial_distance)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                radial_distance,
            ]
        )

        self.radial_distance: typing.Final[types.RealOrJump] = radial_distance


@dataclasses.dataclass
class RadBuilder_0:
    """
    Builds ``Rad_0``.

    Attributes:
        radial_distance: Radial distance fo the position from POS or AXS.
    """

    radial_distance: str | float | types.RealOrJump

    def build(self):
        """
        Builds ``RadBuilder_0`` into ``Rad_0``.

        Returns:
            ``Rad_0`` for ``RadBuilder_0``.
        """

        if isinstance(self.radial_distance, types.Real):
            radial_distance = self.radial_distance
        elif isinstance(self.radial_distance, float) or isinstance(self.radial_distance, int):
            radial_distance = types.RealOrJump(self.radial_distance)
        elif isinstance(self.radial_distance, str):
            radial_distance = types.RealOrJump.from_mcnp(self.radial_distance)

        return Rad_0(
            radial_distance=radial_distance,
        )
