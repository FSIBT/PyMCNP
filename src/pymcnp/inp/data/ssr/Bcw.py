import re
import typing
import dataclasses


from ._option import SsrOption
from ....utils import types
from ....utils import errors


class Bcw(SsrOption):
    """
    Represents INP bcw elements.

    Attributes:
        radius: Radius of cylindrical window.
        zb: Bottom of cylindrical window.
        ze: Top of cylindrical window.
    """

    _ATTRS = {
        'radius': types.Real,
        'zb': types.Real,
        'ze': types.Real,
    }

    _REGEX = re.compile(
        rf'\Abcw( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})\Z'
    )

    def __init__(self, radius: types.Real, zb: types.Real, ze: types.Real):
        """
        Initializes ``Bcw``.

        Parameters:
            radius: Radius of cylindrical window.
            zb: Bottom of cylindrical window.
            ze: Top of cylindrical window.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if radius is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, radius)
        if zb is None or not (0 < zb.value):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, zb)
        if ze is None or not (0 < zb.value < ze.value):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, ze)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                radius,
                zb,
                ze,
            ]
        )

        self.radius: typing.Final[types.Real] = radius
        self.zb: typing.Final[types.Real] = zb
        self.ze: typing.Final[types.Real] = ze


@dataclasses.dataclass
class BcwBuilder:
    """
    Builds ``Bcw``.

    Attributes:
        radius: Radius of cylindrical window.
        zb: Bottom of cylindrical window.
        ze: Top of cylindrical window.
    """

    radius: str | float | types.Real
    zb: str | float | types.Real
    ze: str | float | types.Real

    def build(self):
        """
        Builds ``BcwBuilder`` into ``Bcw``.

        Returns:
            ``Bcw`` for ``BcwBuilder``.
        """

        radius = self.radius
        if isinstance(self.radius, types.Real):
            radius = self.radius
        elif isinstance(self.radius, float) or isinstance(self.radius, int):
            radius = types.Real(self.radius)
        elif isinstance(self.radius, str):
            radius = types.Real.from_mcnp(self.radius)

        zb = self.zb
        if isinstance(self.zb, types.Real):
            zb = self.zb
        elif isinstance(self.zb, float) or isinstance(self.zb, int):
            zb = types.Real(self.zb)
        elif isinstance(self.zb, str):
            zb = types.Real.from_mcnp(self.zb)

        ze = self.ze
        if isinstance(self.ze, types.Real):
            ze = self.ze
        elif isinstance(self.ze, float) or isinstance(self.ze, int):
            ze = types.Real(self.ze)
        elif isinstance(self.ze, str):
            ze = types.Real.from_mcnp(self.ze)

        return Bcw(
            radius=radius,
            zb=zb,
            ze=ze,
        )
