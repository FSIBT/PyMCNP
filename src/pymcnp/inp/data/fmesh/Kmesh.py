import re
import copy
import typing
import dataclasses


from ._option import FmeshOption
from ....utils import types
from ....utils import errors


class Kmesh(FmeshOption):
    """
    Represents INP kmesh elements.

    Attributes:
        locations: Locations of mesh points z/theta for rectangular/cylindrical geometry.
    """

    _KEYWORD = 'kmesh'

    _ATTRS = {
        'locations': types.Real,
    }

    _REGEX = re.compile(rf'\Akmesh( {types.Real._REGEX.pattern[2:-2]})\Z')

    def __init__(self, locations: types.Real):
        """
        Initializes ``Kmesh``.

        Parameters:
            locations: Locations of mesh points z/theta for rectangular/cylindrical geometry.

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

        self.locations: typing.Final[types.Real] = locations


@dataclasses.dataclass
class KmeshBuilder:
    """
    Builds ``Kmesh``.

    Attributes:
        locations: Locations of mesh points z/theta for rectangular/cylindrical geometry.
    """

    locations: str | float | types.Real

    def build(self):
        """
        Builds ``KmeshBuilder`` into ``Kmesh``.

        Returns:
            ``Kmesh`` for ``KmeshBuilder``.
        """

        locations = self.locations
        if isinstance(self.locations, types.Real):
            locations = self.locations
        elif isinstance(self.locations, float) or isinstance(self.locations, int):
            locations = types.Real(self.locations)
        elif isinstance(self.locations, str):
            locations = types.Real.from_mcnp(self.locations)

        return Kmesh(
            locations=locations,
        )

    @staticmethod
    def unbuild(ast: Kmesh):
        """
        Unbuilds ``Kmesh`` into ``KmeshBuilder``

        Returns:
            ``KmeshBuilder`` for ``Kmesh``.
        """

        return Kmesh(
            locations=copy.deepcopy(ast.locations),
        )
