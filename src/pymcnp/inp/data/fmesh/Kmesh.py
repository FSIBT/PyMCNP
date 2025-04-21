import re
import typing
import dataclasses


from ._option import FmeshOption
from ....utils import types
from ....utils import errors


class Kmesh(FmeshOption, keyword='kmesh'):
    """
    Represents INP kmesh elements.

    Attributes:
        locations: Locations of mesh points z/theta for rectangular/cylindrical geometry.
    """

    _ATTRS = {
        'locations': types.RealOrJump,
    }

    _REGEX = re.compile(rf'\Akmesh( {types.RealOrJump._REGEX.pattern})\Z')

    def __init__(self, locations: types.RealOrJump):
        """
        Initializes ``Kmesh``.

        Parameters:
            locations: Locations of mesh points z/theta for rectangular/cylindrical geometry.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if locations is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, locations)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                locations,
            ]
        )

        self.locations: typing.Final[types.RealOrJump] = locations


@dataclasses.dataclass
class KmeshBuilder:
    """
    Builds ``Kmesh``.

    Attributes:
        locations: Locations of mesh points z/theta for rectangular/cylindrical geometry.
    """

    locations: str | float | types.RealOrJump

    def build(self):
        """
        Builds ``KmeshBuilder`` into ``Kmesh``.

        Returns:
            ``Kmesh`` for ``KmeshBuilder``.
        """

        if isinstance(self.locations, types.Real):
            locations = self.locations
        elif isinstance(self.locations, float) or isinstance(self.locations, int):
            locations = types.RealOrJump(self.locations)
        elif isinstance(self.locations, str):
            locations = types.RealOrJump.from_mcnp(self.locations)

        return Kmesh(
            locations=locations,
        )
