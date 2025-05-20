import re
import typing
import dataclasses


from ._option import SdefOption
from ....utils import types
from ....utils import errors


class Ara(SdefOption):
    """
    Represents INP ara elements.

    Attributes:
        area: Area of surface.
    """

    _ATTRS = {
        'area': types.Real,
    }

    _REGEX = re.compile(rf'\Aara( {types.Real._REGEX.pattern})\Z')

    def __init__(self, area: types.Real):
        """
        Initializes ``Ara``.

        Parameters:
            area: Area of surface.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if area is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, area)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                area,
            ]
        )

        self.area: typing.Final[types.Real] = area


@dataclasses.dataclass
class AraBuilder:
    """
    Builds ``Ara``.

    Attributes:
        area: Area of surface.
    """

    area: str | float | types.Real

    def build(self):
        """
        Builds ``AraBuilder`` into ``Ara``.

        Returns:
            ``Ara`` for ``AraBuilder``.
        """

        area = self.area
        if isinstance(self.area, types.Real):
            area = self.area
        elif isinstance(self.area, float) or isinstance(self.area, int):
            area = types.Real(self.area)
        elif isinstance(self.area, str):
            area = types.Real.from_mcnp(self.area)

        return Ara(
            area=area,
        )
