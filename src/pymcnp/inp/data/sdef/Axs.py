import re
import typing
import dataclasses


from ._option import SdefOption
from ....utils import types
from ....utils import errors


class Axs(SdefOption):
    """
    Represents INP axs elements.

    Attributes:
        x: Reference vector for EXT and RAD x-component.
        y: Reference vector for EXT and RAD y-component.
        z: Reference vector for EXT and RAD z-component.
    """

    _ATTRS = {
        'x': types.Real,
        'y': types.Real,
        'z': types.Real,
    }

    _REGEX = re.compile(
        rf'\Aaxs( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})\Z'
    )

    def __init__(self, x: types.Real, y: types.Real, z: types.Real):
        """
        Initializes ``Axs``.

        Parameters:
            x: Reference vector for EXT and RAD x-component.
            y: Reference vector for EXT and RAD y-component.
            z: Reference vector for EXT and RAD z-component.

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

        self.x: typing.Final[types.Real] = x
        self.y: typing.Final[types.Real] = y
        self.z: typing.Final[types.Real] = z


@dataclasses.dataclass
class AxsBuilder:
    """
    Builds ``Axs``.

    Attributes:
        x: Reference vector for EXT and RAD x-component.
        y: Reference vector for EXT and RAD y-component.
        z: Reference vector for EXT and RAD z-component.
    """

    x: str | float | types.Real
    y: str | float | types.Real
    z: str | float | types.Real

    def build(self):
        """
        Builds ``AxsBuilder`` into ``Axs``.

        Returns:
            ``Axs`` for ``AxsBuilder``.
        """

        x = self.x
        if isinstance(self.x, types.Real):
            x = self.x
        elif isinstance(self.x, float) or isinstance(self.x, int):
            x = types.Real(self.x)
        elif isinstance(self.x, str):
            x = types.Real.from_mcnp(self.x)

        y = self.y
        if isinstance(self.y, types.Real):
            y = self.y
        elif isinstance(self.y, float) or isinstance(self.y, int):
            y = types.Real(self.y)
        elif isinstance(self.y, str):
            y = types.Real.from_mcnp(self.y)

        z = self.z
        if isinstance(self.z, types.Real):
            z = self.z
        elif isinstance(self.z, float) or isinstance(self.z, int):
            z = types.Real(self.z)
        elif isinstance(self.z, str):
            z = types.Real.from_mcnp(self.z)

        return Axs(
            x=x,
            y=y,
            z=z,
        )
