import re
import typing
import dataclasses


from ._option import DawwgOption
from ....utils import types
from ....utils import errors


class Points(DawwgOption, keyword='points'):
    """
    Represents INP points elements.

    Attributes:
        name: Cross section library.
    """

    _ATTRS = {
        'name': types.String,
    }

    _REGEX = re.compile(rf'\Apoints( {types.String._REGEX.pattern})\Z')

    def __init__(self, name: types.String):
        """
        Initializes ``Points``.

        Parameters:
            name: Cross section library.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if name is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, name)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                name,
            ]
        )

        self.name: typing.Final[types.String] = name


@dataclasses.dataclass
class PointsBuilder:
    """
    Builds ``Points``.

    Attributes:
        name: Cross section library.
    """

    name: str | types.String

    def build(self):
        """
        Builds ``PointsBuilder`` into ``Points``.

        Returns:
            ``Points`` for ``PointsBuilder``.
        """

        if isinstance(self.name, types.String):
            name = self.name
        elif isinstance(self.name, str):
            name = types.String.from_mcnp(self.name)

        return Points(
            name=name,
        )
