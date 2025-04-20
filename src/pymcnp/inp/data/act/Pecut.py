import re
import typing
import dataclasses


from .option_ import ActOption_
from ....utils import types
from ....utils import errors


class Pecut(ActOption_, keyword='pecut'):
    """
    Represents INP pecut elements.

    Attributes:
        cutoff: Delayed-gamma energy cutoff.
    """

    _ATTRS = {
        'cutoff': types.RealOrJump,
    }

    _REGEX = re.compile(rf'\Apecut( {types.RealOrJump._REGEX.pattern})\Z')

    def __init__(self, cutoff: types.RealOrJump):
        """
        Initializes ``Pecut``.

        Parameters:
            cutoff: Delayed-gamma energy cutoff.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if cutoff is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, cutoff)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                cutoff,
            ]
        )

        self.cutoff: typing.Final[types.RealOrJump] = cutoff


@dataclasses.dataclass
class PecutBuilder:
    """
    Builds ``Pecut``.

    Attributes:
        cutoff: Delayed-gamma energy cutoff.
    """

    cutoff: str | float | types.RealOrJump

    def build(self):
        """
        Builds ``PecutBuilder`` into ``Pecut``.

        Returns:
            ``Pecut`` for ``PecutBuilder``.
        """

        if isinstance(self.cutoff, types.Real):
            cutoff = self.cutoff
        elif isinstance(self.cutoff, float) or isinstance(self.cutoff, int):
            cutoff = types.RealOrJump(self.cutoff)
        elif isinstance(self.cutoff, str):
            cutoff = types.RealOrJump.from_mcnp(self.cutoff)

        return Pecut(
            cutoff=cutoff,
        )
