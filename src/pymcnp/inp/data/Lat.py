import re
import typing
import dataclasses


from ._option import DataOption
from ...utils import types
from ...utils import errors


class Lat(DataOption):
    """
    Represents INP lat elements.

    Attributes:
        type: Tuple of lattice types.
    """

    _ATTRS = {
        'type': types.Tuple[types.IntegerOrJump],
    }

    _REGEX = re.compile(rf'\Alat((?: {types.IntegerOrJump._REGEX.pattern})+?)\Z')

    def __init__(self, type: types.Tuple[types.IntegerOrJump]):
        """
        Initializes ``Lat``.

        Parameters:
            type: Tuple of lattice types.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if type is None or not (filter(lambda entry: not (entry == 1 or entry == 2), type)):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, type)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                type,
            ]
        )

        self.type: typing.Final[types.Tuple[types.IntegerOrJump]] = type


@dataclasses.dataclass
class LatBuilder:
    """
    Builds ``Lat``.

    Attributes:
        type: Tuple of lattice types.
    """

    type: list[str] | list[int] | list[types.IntegerOrJump]

    def build(self):
        """
        Builds ``LatBuilder`` into ``Lat``.

        Returns:
            ``Lat`` for ``LatBuilder``.
        """

        if self.type:
            type = []
            for item in self.type:
                if isinstance(item, types.IntegerOrJump):
                    type.append(item)
                elif isinstance(item, int):
                    type.append(types.IntegerOrJump(item))
                elif isinstance(item, str):
                    type.append(types.IntegerOrJump.from_mcnp(item))
            type = types.Tuple(type)
        else:
            type = None

        return Lat(
            type=type,
        )
