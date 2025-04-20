import re
import typing
import dataclasses


from .option_ import SsrOption_
from ....utils import types
from ....utils import errors


class Bcw(SsrOption_, keyword='bcw'):
    """
    Represents INP bcw elements.

    Attributes:
        radius: Radius of cylindrical window.
        zb: Bottom of cylindrical window.
        ze: Top of cylindrical window.
    """

    _ATTRS = {
        'radius': types.RealOrJump,
        'zb': types.RealOrJump,
        'ze': types.RealOrJump,
    }

    _REGEX = re.compile(
        rf'\Abcw( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})\Z'
    )

    def __init__(self, radius: types.RealOrJump, zb: types.RealOrJump, ze: types.RealOrJump):
        """
        Initializes ``Bcw``.

        Parameters:
            radius: Radius of cylindrical window.
            zb: Bottom of cylindrical window.
            ze: Top of cylindrical window.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if radius is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, radius)
        if zb is None or not (0 < zb):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, zb)
        if ze is None or not (0 < zb < ze):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, ze)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                radius,
                zb,
                ze,
            ]
        )

        self.radius: typing.Final[types.RealOrJump] = radius
        self.zb: typing.Final[types.RealOrJump] = zb
        self.ze: typing.Final[types.RealOrJump] = ze


@dataclasses.dataclass
class BcwBuilder:
    """
    Builds ``Bcw``.

    Attributes:
        radius: Radius of cylindrical window.
        zb: Bottom of cylindrical window.
        ze: Top of cylindrical window.
    """

    radius: str | float | types.RealOrJump
    zb: str | float | types.RealOrJump
    ze: str | float | types.RealOrJump

    def build(self):
        """
        Builds ``BcwBuilder`` into ``Bcw``.

        Returns:
            ``Bcw`` for ``BcwBuilder``.
        """

        if isinstance(self.radius, types.Real):
            radius = self.radius
        elif isinstance(self.radius, float) or isinstance(self.radius, int):
            radius = types.RealOrJump(self.radius)
        elif isinstance(self.radius, str):
            radius = types.RealOrJump.from_mcnp(self.radius)

        if isinstance(self.zb, types.Real):
            zb = self.zb
        elif isinstance(self.zb, float) or isinstance(self.zb, int):
            zb = types.RealOrJump(self.zb)
        elif isinstance(self.zb, str):
            zb = types.RealOrJump.from_mcnp(self.zb)

        if isinstance(self.ze, types.Real):
            ze = self.ze
        elif isinstance(self.ze, float) or isinstance(self.ze, int):
            ze = types.RealOrJump(self.ze)
        elif isinstance(self.ze, str):
            ze = types.RealOrJump.from_mcnp(self.ze)

        return Bcw(
            radius=radius,
            zb=zb,
            ze=ze,
        )
