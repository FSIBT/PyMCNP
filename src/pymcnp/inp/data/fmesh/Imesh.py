import re
import typing
import dataclasses


from ._option import FmeshOption
from ....utils import types
from ....utils import errors


class Imesh(FmeshOption, keyword='imesh'):
    """
    Represents INP imesh elements.

    Attributes:
        locations: Locations of mesh points x/r for rectangular/cylindrical geometry.
    """

    _ATTRS = {
        'locations': types.RealOrJump,
    }

    _REGEX = re.compile(rf'\Aimesh( {types.RealOrJump._REGEX.pattern})\Z')

    def __init__(self, locations: types.RealOrJump):
        """
        Initializes ``Imesh``.

        Parameters:
            locations: Locations of mesh points x/r for rectangular/cylindrical geometry.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if locations is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, locations)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                locations,
            ]
        )

        self.locations: typing.Final[types.RealOrJump] = locations


@dataclasses.dataclass
class ImeshBuilder:
    """
    Builds ``Imesh``.

    Attributes:
        locations: Locations of mesh points x/r for rectangular/cylindrical geometry.
    """

    locations: str | float | types.RealOrJump

    def build(self):
        """
        Builds ``ImeshBuilder`` into ``Imesh``.

        Returns:
            ``Imesh`` for ``ImeshBuilder``.
        """

        if isinstance(self.locations, types.Real):
            locations = self.locations
        elif isinstance(self.locations, float) or isinstance(self.locations, int):
            locations = types.RealOrJump(self.locations)
        elif isinstance(self.locations, str):
            locations = types.RealOrJump.from_mcnp(self.locations)

        return Imesh(
            locations=locations,
        )
