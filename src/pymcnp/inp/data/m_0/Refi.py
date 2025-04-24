import re
import typing
import dataclasses


from ._option import MOption_0
from ....utils import types
from ....utils import errors


class Refi(MOption_0, keyword='refi'):
    """
    Represents INP refi elements.

    Attributes:
        refractive_index: Refractive index constant.
    """

    _ATTRS = {
        'refractive_index': types.RealOrJump,
    }

    _REGEX = re.compile(rf'\Arefi( {types.RealOrJump._REGEX.pattern})\Z')

    def __init__(self, refractive_index: types.RealOrJump):
        """
        Initializes ``Refi``.

        Parameters:
            refractive_index: Refractive index constant.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if refractive_index is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, refractive_index)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                refractive_index,
            ]
        )

        self.refractive_index: typing.Final[types.RealOrJump] = refractive_index


@dataclasses.dataclass
class RefiBuilder:
    """
    Builds ``Refi``.

    Attributes:
        refractive_index: Refractive index constant.
    """

    refractive_index: str | float | types.RealOrJump

    def build(self):
        """
        Builds ``RefiBuilder`` into ``Refi``.

        Returns:
            ``Refi`` for ``RefiBuilder``.
        """

        if isinstance(self.refractive_index, types.Real):
            refractive_index = self.refractive_index
        elif isinstance(self.refractive_index, float) or isinstance(self.refractive_index, int):
            refractive_index = types.RealOrJump(self.refractive_index)
        elif isinstance(self.refractive_index, str):
            refractive_index = types.RealOrJump.from_mcnp(self.refractive_index)

        return Refi(
            refractive_index=refractive_index,
        )
