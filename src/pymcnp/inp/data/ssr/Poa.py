import re
import typing
import dataclasses


from .option_ import SsrOption_
from ....utils import types
from ....utils import errors


class Poa(SsrOption_, keyword='poa'):
    """
    Represents INP poa elements.

    Attributes:
        angle: Angle within which particles accepeted for transport.
    """

    _ATTRS = {
        'angle': types.RealOrJump,
    }

    _REGEX = re.compile(rf'\Apoa( {types.RealOrJump._REGEX.pattern})\Z')

    def __init__(self, angle: types.RealOrJump):
        """
        Initializes ``Poa``.

        Parameters:
            angle: Angle within which particles accepeted for transport.

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
class PoaBuilder:
    """
    Builds ``Poa``.

    Attributes:
        angle: Angle within which particles accepeted for transport.
    """

    angle: str | float | types.RealOrJump

    def build(self):
        """
        Builds ``PoaBuilder`` into ``Poa``.

        Returns:
            ``Poa`` for ``PoaBuilder``.
        """

        if isinstance(self.angle, types.Real):
            angle = self.angle
        elif isinstance(self.angle, float) or isinstance(self.angle, int):
            angle = types.RealOrJump(self.angle)
        elif isinstance(self.angle, str):
            angle = types.RealOrJump.from_mcnp(self.angle)

        return Poa(
            angle=angle,
        )
