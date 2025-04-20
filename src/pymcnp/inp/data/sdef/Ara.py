import re
import typing
import dataclasses


from .option_ import SdefOption_
from ....utils import types
from ....utils import errors


class Ara(SdefOption_, keyword='ara'):
    """
    Represents INP ara elements.

    Attributes:
        area: Area of surface.
    """

    _ATTRS = {
        'area': types.RealOrJump,
    }

    _REGEX = re.compile(rf'\Aara( {types.RealOrJump._REGEX.pattern})\Z')

    def __init__(self, area: types.RealOrJump):
        """
        Initializes ``Ara``.

        Parameters:
            area: Area of surface.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if area is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, area)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                area,
            ]
        )

        self.area: typing.Final[types.RealOrJump] = area


@dataclasses.dataclass
class AraBuilder:
    """
    Builds ``Ara``.

    Attributes:
        area: Area of surface.
    """

    area: str | float | types.RealOrJump

    def build(self):
        """
        Builds ``AraBuilder`` into ``Ara``.

        Returns:
            ``Ara`` for ``AraBuilder``.
        """

        if isinstance(self.area, types.Real):
            area = self.area
        elif isinstance(self.area, float) or isinstance(self.area, int):
            area = types.RealOrJump(self.area)
        elif isinstance(self.area, str):
            area = types.RealOrJump.from_mcnp(self.area)

        return Ara(
            area=area,
        )
