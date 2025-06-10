import re
import copy
import typing
import dataclasses


from . import _option
from ...utils import types
from ...utils import errors


class Ksrc(_option.DataOption):
    """
    Represents INP ksrc elements.

    Attributes:
        locations: Tuple of inital source points.
    """

    _KEYWORD = 'ksrc'

    _ATTRS = {
        'locations': types.Tuple[types.Location],
    }

    _REGEX = re.compile(rf'\Aksrc((?: {types.Location._REGEX.pattern[2:-2]})+?)\Z')

    def __init__(self, locations: types.Tuple[types.Location]):
        """
        Initializes ``Ksrc``.

        Parameters:
            locations: Tuple of inital source points.

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

        self.locations: typing.Final[types.Tuple[types.Location]] = locations


@dataclasses.dataclass
class KsrcBuilder(_option.DataOptionBuilder):
    """
    Builds ``Ksrc``.

    Attributes:
        locations: Tuple of inital source points.
    """

    locations: list[str] | list[types.Location]

    def build(self):
        """
        Builds ``KsrcBuilder`` into ``Ksrc``.

        Returns:
            ``Ksrc`` for ``KsrcBuilder``.
        """

        if self.locations:
            locations = []
            for item in self.locations:
                if isinstance(item, types.Location):
                    locations.append(item)
                elif isinstance(item, str):
                    locations.append(types.Location.from_mcnp(item))
            locations = types.Tuple(locations)
        else:
            locations = None

        return Ksrc(
            locations=locations,
        )

    @staticmethod
    def unbuild(ast: Ksrc):
        """
        Unbuilds ``Ksrc`` into ``KsrcBuilder``

        Returns:
            ``KsrcBuilder`` for ``Ksrc``.
        """

        return KsrcBuilder(
            locations=copy.deepcopy(ast.locations),
        )
