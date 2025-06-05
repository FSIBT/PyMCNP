import re
import copy
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

    _KEYWORD = 'jmesh'

    _ATTRS = {
        'locations': types.Tuple[types.Real],
    }

    _REGEX = re.compile(rf'\Ajmesh((?: {types.Real._REGEX.pattern[2:-2]})+?)\Z')

    def __init__(self, locations: types.Tuple[types.Real]):
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

        self.locations: typing.Final[types.Tuple[types.Real]] = locations


@dataclasses.dataclass
class JmeshBuilder:
    """
    Builds ``Jmesh``.

    Attributes:
        locations: Locations of mesh points y/z for rectangular/cylindrical geometry.
    """

    locations: list[str] | list[float] | list[types.Real]

    def build(self):
        """
        Builds ``JmeshBuilder`` into ``Jmesh``.

        Returns:
            ``Jmesh`` for ``JmeshBuilder``.
        """

        if self.locations:
            locations = []
            for item in self.locations:
                if isinstance(item, types.Real):
                    locations.append(item)
                elif isinstance(item, float) or isinstance(item, int):
                    locations.append(types.Real(item))
                elif isinstance(item, str):
                    locations.append(types.Real.from_mcnp(item))
            locations = types.Tuple(locations)
        else:
            locations = None

        return Jmesh(
            locations=locations,
        )

    @staticmethod
    def unbuild(ast: Jmesh):
        """
        Unbuilds ``Jmesh`` into ``JmeshBuilder``

        Returns:
            ``JmeshBuilder`` for ``Jmesh``.
        """

        return Jmesh(
            locations=copy.deepcopy(ast.locations),
        )
