import re
import typing
import dataclasses


from ._option import DataOption
from ...utils import types
from ...utils import errors


class Ksrc(DataOption, keyword='ksrc'):
    """
    Represents INP ksrc elements.

    Attributes:
        locations: Tuple of inital source points.
    """

    _ATTRS = {
        'locations': types.Tuple[types.Location],
    }

    _REGEX = re.compile(rf'\Aksrc((?: {types.Location._REGEX.pattern})+?)\Z')

    def __init__(self, locations: types.Tuple[types.Location]):
        """
        Initializes ``Ksrc``.

        Parameters:
            locations: Tuple of inital source points.

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

        self.locations: typing.Final[types.Tuple[types.Location]] = locations


@dataclasses.dataclass
class KsrcBuilder:
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

        locations = []
        for item in self.locations:
            if isinstance(item, types.Location):
                locations.append(item)
            elif isinstance(item, str):
                locations.append(types.Location.from_mcnp(item))
            else:
                locations.append(item.build())
        locations = types.Tuple(locations)

        return Ksrc(
            locations=locations,
        )
