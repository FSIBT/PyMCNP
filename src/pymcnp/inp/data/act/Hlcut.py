import re
import typing
import dataclasses


from ._option import ActOption
from ....utils import types
from ....utils import errors


class Hlcut(ActOption):
    """
    Represents INP hlcut elements.

    Attributes:
        cutoff: Spontaneous-decay half-life threshold.
    """

    _ATTRS = {
        'cutoff': types.RealOrJump,
    }

    _REGEX = re.compile(rf'\Ahlcut( {types.RealOrJump._REGEX.pattern})\Z')

    def __init__(self, cutoff: types.RealOrJump):
        """
        Initializes ``Hlcut``.

        Parameters:
            cutoff: Spontaneous-decay half-life threshold.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if cutoff is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, cutoff)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                cutoff,
            ]
        )

        self.cutoff: typing.Final[types.RealOrJump] = cutoff


@dataclasses.dataclass
class HlcutBuilder:
    """
    Builds ``Hlcut``.

    Attributes:
        cutoff: Spontaneous-decay half-life threshold.
    """

    cutoff: str | float | types.RealOrJump

    def build(self):
        """
        Builds ``HlcutBuilder`` into ``Hlcut``.

        Returns:
            ``Hlcut`` for ``HlcutBuilder``.
        """

        if isinstance(self.cutoff, types.Real):
            cutoff = self.cutoff
        elif isinstance(self.cutoff, float) or isinstance(self.cutoff, int):
            cutoff = types.RealOrJump(self.cutoff)
        elif isinstance(self.cutoff, str):
            cutoff = types.RealOrJump.from_mcnp(self.cutoff)

        return Hlcut(
            cutoff=cutoff,
        )
