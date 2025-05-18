import re
import typing
import dataclasses


from ._option import FmeshOption
from ....utils import types
from ....utils import errors


class Jmesh(FmeshOption):
    """
    Represents INP jmesh elements.

    Attributes:
        locations: Locations of mesh points y/z for rectangular/cylindrical geometry.
    """

    _ATTRS = {
        'locations': types.RealOrJump,
    }

    _REGEX = re.compile(rf'\Ajmesh( {types.RealOrJump._REGEX.pattern})\Z')

    def __init__(self, locations: types.RealOrJump):
        """
        Initializes ``Jmesh``.

        Parameters:
            locations: Locations of mesh points y/z for rectangular/cylindrical geometry.

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
class JmeshBuilder:
    """
    Builds ``Jmesh``.

    Attributes:
        locations: Locations of mesh points y/z for rectangular/cylindrical geometry.
    """

    locations: str | float | types.RealOrJump

    def build(self):
        """
        Builds ``JmeshBuilder`` into ``Jmesh``.

        Returns:
            ``Jmesh`` for ``JmeshBuilder``.
        """

        locations = self.locations
        if isinstance(self.locations, types.Real):
            locations = self.locations
        elif isinstance(self.locations, float) or isinstance(self.locations, int):
            locations = types.RealOrJump(self.locations)
        elif isinstance(self.locations, str):
            locations = types.RealOrJump.from_mcnp(self.locations)

        return Jmesh(
            locations=locations,
        )
