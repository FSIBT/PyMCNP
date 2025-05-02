import re
import typing
import dataclasses


from ._option import PertOption
from ....utils import types
from ....utils import errors


class Rho(PertOption):
    """
    Represents INP rho elements.

    Attributes:
        density: Perturbed density.
    """

    _ATTRS = {
        'density': types.RealOrJump,
    }

    _REGEX = re.compile(rf'\Arho( {types.RealOrJump._REGEX.pattern})\Z')

    def __init__(self, density: types.RealOrJump):
        """
        Initializes ``Rho``.

        Parameters:
            density: Perturbed density.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if density is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, density)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                density,
            ]
        )

        self.density: typing.Final[types.RealOrJump] = density


@dataclasses.dataclass
class RhoBuilder:
    """
    Builds ``Rho``.

    Attributes:
        density: Perturbed density.
    """

    density: str | float | types.RealOrJump

    def build(self):
        """
        Builds ``RhoBuilder`` into ``Rho``.

        Returns:
            ``Rho`` for ``RhoBuilder``.
        """

        if isinstance(self.density, types.Real):
            density = self.density
        elif isinstance(self.density, float) or isinstance(self.density, int):
            density = types.RealOrJump(self.density)
        elif isinstance(self.density, str):
            density = types.RealOrJump.from_mcnp(self.density)

        return Rho(
            density=density,
        )
