import re
import copy
import typing
import dataclasses


from . import _option
from ....utils import types
from ....utils import errors


class Kmesh(_option.FmeshOption):
    """
    Represents INP kmesh elements.

    Attributes:
        locations: Locations of mesh points z/theta for rectangular/cylindrical geometry.
    """

    _KEYWORD = 'kmesh'

    _ATTRS = {
        'locations': types.Tuple[types.Real],
    }

    _REGEX = re.compile(rf'\Akmesh((?: {types.Real._REGEX.pattern[2:-2]})+?)\Z')

    def __init__(self, locations: types.Tuple[types.Real]):
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

        self.locations: typing.Final[types.Tuple[types.Real]] = locations


@dataclasses.dataclass
class KmeshBuilder(_option.FmeshOptionBuilder):
    """
    Builds ``Kmesh``.

    Attributes:
        locations: Locations of mesh points z/theta for rectangular/cylindrical geometry.
    """

    locations: list[str] | list[float] | list[types.Real]

    def build(self):
        """
        Builds ``KmeshBuilder`` into ``Kmesh``.

        Returns:
            ``Kmesh`` for ``KmeshBuilder``.
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

        return KmeshBuilder(
            locations=copy.deepcopy(ast.locations),
        )
