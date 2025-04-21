import re
import typing
import dataclasses


from ._option import DataOption
from ...utils import types
from ...utils import errors


class Sd(DataOption, keyword='sd'):
    """
    Represents INP sd elements.

    Attributes:
        information: Area, volume, or mass by segmented, surface/cell.
    """

    _ATTRS = {
        'information': types.Tuple[types.RealOrJump],
    }

    _REGEX = re.compile(rf'\Asd((?: {types.RealOrJump._REGEX.pattern})+?)\Z')

    def __init__(self, information: types.Tuple[types.RealOrJump]):
        """
        Initializes ``Sd``.

        Parameters:
            information: Area, volume, or mass by segmented, surface/cell.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if information is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, information)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                information,
            ]
        )

        self.information: typing.Final[types.Tuple[types.RealOrJump]] = information


@dataclasses.dataclass
class SdBuilder:
    """
    Builds ``Sd``.

    Attributes:
        information: Area, volume, or mass by segmented, surface/cell.
    """

    information: list[str] | list[float] | list[types.RealOrJump]

    def build(self):
        """
        Builds ``SdBuilder`` into ``Sd``.

        Returns:
            ``Sd`` for ``SdBuilder``.
        """

        information = []
        for item in self.information:
            if isinstance(item, types.RealOrJump):
                information.append(item)
            elif isinstance(item, float) or isinstance(item, int):
                information.append(types.RealOrJump(item))
            elif isinstance(item, str):
                information.append(types.RealOrJump.from_mcnp(item))
        information = types.Tuple(information)

        return Sd(
            information=information,
        )
