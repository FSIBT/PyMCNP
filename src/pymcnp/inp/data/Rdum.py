import re
import typing
import dataclasses


from ._option import DataOption
from ...utils import types
from ...utils import errors


class Rdum(DataOption, keyword='rdum'):
    """
    Represents INP rdum elements.

    Attributes:
        floats: Floating point array.
    """

    _ATTRS = {
        'floats': types.Tuple[types.RealOrJump],
    }

    _REGEX = re.compile(rf'\Ardum((?: {types.RealOrJump._REGEX.pattern})+?)\Z')

    def __init__(self, floats: types.Tuple[types.RealOrJump]):
        """
        Initializes ``Rdum``.

        Parameters:
            floats: Floating point array.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if floats is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, floats)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                floats,
            ]
        )

        self.floats: typing.Final[types.Tuple[types.RealOrJump]] = floats


@dataclasses.dataclass
class RdumBuilder:
    """
    Builds ``Rdum``.

    Attributes:
        floats: Floating point array.
    """

    floats: list[str] | list[float] | list[types.RealOrJump]

    def build(self):
        """
        Builds ``RdumBuilder`` into ``Rdum``.

        Returns:
            ``Rdum`` for ``RdumBuilder``.
        """

        floats = []
        for item in self.floats:
            if isinstance(item, types.RealOrJump):
                floats.append(item)
            elif isinstance(item, float) or isinstance(item, int):
                floats.append(types.RealOrJump(item))
            elif isinstance(item, str):
                floats.append(types.RealOrJump.from_mcnp(item))
        floats = types.Tuple(floats)

        return Rdum(
            floats=floats,
        )
