import re
import copy
import typing
import dataclasses


from ._option import FmeshOption
from ....utils import types
from ....utils import errors


class Imesh(FmeshOption):
    """
    Represents INP imesh elements.

    Attributes:
        locations: Locations of mesh points x/r for rectangular/cylindrical geometry.
    """

    _KEYWORD = 'imesh'

    _ATTRS = {
        'locations': types.Tuple[types.Real],
    }

    _REGEX = re.compile(rf'\Aimesh((?: {types.Real._REGEX.pattern[2:-2]})+?)\Z')

    def __init__(self, locations: types.Tuple[types.Real]):
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

        self.locations: typing.Final[types.Tuple[types.Real]] = locations


@dataclasses.dataclass
class ImeshBuilder:
    """
    Builds ``Imesh``.

    Attributes:
        locations: Locations of mesh points x/r for rectangular/cylindrical geometry.
    """

    locations: list[str] | list[float] | list[types.Real]

    def build(self):
        """
        Builds ``ImeshBuilder`` into ``Imesh``.

        Returns:
            ``Imesh`` for ``ImeshBuilder``.
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

        return Imesh(
            locations=locations,
        )

    @staticmethod
    def unbuild(ast: Imesh):
        """
        Unbuilds ``Imesh`` into ``ImeshBuilder``

        Returns:
            ``ImeshBuilder`` for ``Imesh``.
        """

        return Imesh(
            locations=copy.deepcopy(ast.locations),
        )
