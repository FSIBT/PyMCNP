import re
import typing
import dataclasses


from ._option import BfldOption
from ....utils import types
from ....utils import errors


class Maxstep(BfldOption, keyword='maxstep'):
    """
    Represents INP maxstep elements.

    Attributes:
        size: Maximum step size.
    """

    _ATTRS = {
        'size': types.RealOrJump,
    }

    _REGEX = re.compile(rf'\Amaxstep( {types.RealOrJump._REGEX.pattern})\Z')

    def __init__(self, size: types.RealOrJump):
        """
        Initializes ``Maxstep``.

        Parameters:
            size: Maximum step size.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if size is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, size)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                size,
            ]
        )

        self.size: typing.Final[types.RealOrJump] = size


@dataclasses.dataclass
class MaxstepBuilder:
    """
    Builds ``Maxstep``.

    Attributes:
        size: Maximum step size.
    """

    size: str | float | types.RealOrJump

    def build(self):
        """
        Builds ``MaxstepBuilder`` into ``Maxstep``.

        Returns:
            ``Maxstep`` for ``MaxstepBuilder``.
        """

        if isinstance(self.size, types.Real):
            size = self.size
        elif isinstance(self.size, float) or isinstance(self.size, int):
            size = types.RealOrJump(self.size)
        elif isinstance(self.size, str):
            size = types.RealOrJump.from_mcnp(self.size)

        return Maxstep(
            size=size,
        )
