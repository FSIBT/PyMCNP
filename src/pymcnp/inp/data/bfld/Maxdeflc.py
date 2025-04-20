import re
import typing
import dataclasses


from .option_ import BfldOption_
from ....utils import types
from ....utils import errors


class Maxdeflc(BfldOption_, keyword='maxdeflc'):
    """
    Represents INP maxdeflc elements.

    Attributes:
        angle: Maximum deflection angles.
    """

    _ATTRS = {
        'angle': types.RealOrJump,
    }

    _REGEX = re.compile(rf'\Amaxdeflc( {types.RealOrJump._REGEX.pattern})\Z')

    def __init__(self, angle: types.RealOrJump):
        """
        Initializes ``Maxdeflc``.

        Parameters:
            angle: Maximum deflection angles.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if angle is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, angle)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                angle,
            ]
        )

        self.angle: typing.Final[types.RealOrJump] = angle


@dataclasses.dataclass
class MaxdeflcBuilder:
    """
    Builds ``Maxdeflc``.

    Attributes:
        angle: Maximum deflection angles.
    """

    angle: str | float | types.RealOrJump

    def build(self):
        """
        Builds ``MaxdeflcBuilder`` into ``Maxdeflc``.

        Returns:
            ``Maxdeflc`` for ``MaxdeflcBuilder``.
        """

        if isinstance(self.angle, types.Real):
            angle = self.angle
        elif isinstance(self.angle, float) or isinstance(self.angle, int):
            angle = types.RealOrJump(self.angle)
        elif isinstance(self.angle, str):
            angle = types.RealOrJump.from_mcnp(self.angle)

        return Maxdeflc(
            angle=angle,
        )
