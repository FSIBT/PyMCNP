import re
import typing
import dataclasses


from ._option import KsenOption
from ....utils import types
from ....utils import errors


class Cos(KsenOption, keyword='cos'):
    """
    Represents INP cos elements.

    Attributes:
        cosines: Range of direction-change cosines.
    """

    _ATTRS = {
        'cosines': types.Tuple[types.RealOrJump],
    }

    _REGEX = re.compile(rf'\Acos((?: {types.RealOrJump._REGEX.pattern})+?)\Z')

    def __init__(self, cosines: types.Tuple[types.RealOrJump]):
        """
        Initializes ``Cos``.

        Parameters:
            cosines: Range of direction-change cosines.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if cosines is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, cosines)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                cosines,
            ]
        )

        self.cosines: typing.Final[types.Tuple[types.RealOrJump]] = cosines


@dataclasses.dataclass
class CosBuilder:
    """
    Builds ``Cos``.

    Attributes:
        cosines: Range of direction-change cosines.
    """

    cosines: list[str] | list[float] | list[types.RealOrJump]

    def build(self):
        """
        Builds ``CosBuilder`` into ``Cos``.

        Returns:
            ``Cos`` for ``CosBuilder``.
        """

        cosines = []
        for item in self.cosines:
            if isinstance(item, types.RealOrJump):
                cosines.append(item)
            elif isinstance(item, float) or isinstance(item, int):
                cosines.append(types.RealOrJump(item))
            elif isinstance(item, str):
                cosines.append(types.RealOrJump.from_mcnp(item))
        cosines = types.Tuple(cosines)

        return Cos(
            cosines=cosines,
        )
