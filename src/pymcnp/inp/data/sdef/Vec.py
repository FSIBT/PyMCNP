import re
import typing
import dataclasses


from ._option import SdefOption
from ....utils import types
from ....utils import errors


class Vec(SdefOption):
    """
    Represents INP vec elements.

    Attributes:
        x: Reference vector for DIR x-component.
        y: Reference vector for DIR y-component.
        z: Reference vector for DIR z-component.
    """

    _ATTRS = {
        'x': types.RealOrJump,
        'y': types.RealOrJump,
        'z': types.RealOrJump,
    }

    _REGEX = re.compile(
        rf'\Avec( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})\Z'
    )

    def __init__(self, x: types.RealOrJump, y: types.RealOrJump, z: types.RealOrJump):
        """
        Initializes ``Vec``.

        Parameters:
            x: Reference vector for DIR x-component.
            y: Reference vector for DIR y-component.
            z: Reference vector for DIR z-component.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if x is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, x)
        if y is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, y)
        if z is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, z)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                x,
                y,
                z,
            ]
        )

        self.x: typing.Final[types.RealOrJump] = x
        self.y: typing.Final[types.RealOrJump] = y
        self.z: typing.Final[types.RealOrJump] = z


@dataclasses.dataclass
class VecBuilder:
    """
    Builds ``Vec``.

    Attributes:
        x: Reference vector for DIR x-component.
        y: Reference vector for DIR y-component.
        z: Reference vector for DIR z-component.
    """

    x: str | float | types.RealOrJump
    y: str | float | types.RealOrJump
    z: str | float | types.RealOrJump

    def build(self):
        """
        Builds ``VecBuilder`` into ``Vec``.

        Returns:
            ``Vec`` for ``VecBuilder``.
        """

        if isinstance(self.x, types.Real):
            x = self.x
        elif isinstance(self.x, float) or isinstance(self.x, int):
            x = types.RealOrJump(self.x)
        elif isinstance(self.x, str):
            x = types.RealOrJump.from_mcnp(self.x)

        if isinstance(self.y, types.Real):
            y = self.y
        elif isinstance(self.y, float) or isinstance(self.y, int):
            y = types.RealOrJump(self.y)
        elif isinstance(self.y, str):
            y = types.RealOrJump.from_mcnp(self.y)

        if isinstance(self.z, types.Real):
            z = self.z
        elif isinstance(self.z, float) or isinstance(self.z, int):
            z = types.RealOrJump(self.z)
        elif isinstance(self.z, str):
            z = types.RealOrJump.from_mcnp(self.z)

        return Vec(
            x=x,
            y=y,
            z=z,
        )
