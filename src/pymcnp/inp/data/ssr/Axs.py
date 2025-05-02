import re
import typing
import dataclasses


from ._option import SsrOption
from ....utils import types
from ....utils import errors


class Axs(SsrOption):
    """
    Represents INP axs elements.

    Attributes:
        cosines: Direction cosines defining.
    """

    _ATTRS = {
        'cosines': types.Tuple[types.RealOrJump],
    }

    _REGEX = re.compile(rf'\Aaxs((?: {types.RealOrJump._REGEX.pattern})+?)\Z')

    def __init__(self, cosines: types.Tuple[types.RealOrJump]):
        """
        Initializes ``Axs``.

        Parameters:
            cosines: Direction cosines defining.

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
class AxsBuilder:
    """
    Builds ``Axs``.

    Attributes:
        cosines: Direction cosines defining.
    """

    cosines: list[str] | list[float] | list[types.RealOrJump]

    def build(self):
        """
        Builds ``AxsBuilder`` into ``Axs``.

        Returns:
            ``Axs`` for ``AxsBuilder``.
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

        return Axs(
            cosines=cosines,
        )
