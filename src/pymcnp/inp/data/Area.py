import re
import typing
import dataclasses


from ._option import DataOption
from ...utils import types
from ...utils import errors


class Area(DataOption):
    """
    Represents INP area elements.

    Attributes:
        areas: Tuple of surface areas.
    """

    _ATTRS = {
        'areas': types.Tuple[types.RealOrJump],
    }

    _REGEX = re.compile(rf'\Aarea((?: {types.RealOrJump._REGEX.pattern})+?)\Z')

    def __init__(self, areas: types.Tuple[types.RealOrJump]):
        """
        Initializes ``Area``.

        Parameters:
            areas: Tuple of surface areas.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if areas is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, areas)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                areas,
            ]
        )

        self.areas: typing.Final[types.Tuple[types.RealOrJump]] = areas


@dataclasses.dataclass
class AreaBuilder:
    """
    Builds ``Area``.

    Attributes:
        areas: Tuple of surface areas.
    """

    areas: list[str] | list[float] | list[types.RealOrJump]

    def build(self):
        """
        Builds ``AreaBuilder`` into ``Area``.

        Returns:
            ``Area`` for ``AreaBuilder``.
        """

        if self.areas:
            areas = []
            for item in self.areas:
                if isinstance(item, types.RealOrJump):
                    areas.append(item)
                elif isinstance(item, float) or isinstance(item, int):
                    areas.append(types.RealOrJump(item))
                elif isinstance(item, str):
                    areas.append(types.RealOrJump.from_mcnp(item))
            areas = types.Tuple(areas)
        else:
            areas = None

        return Area(
            areas=areas,
        )
