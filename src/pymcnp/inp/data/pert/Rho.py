import re
import copy
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

    _KEYWORD = 'rho'

    _ATTRS = {
        'density': types.Real,
    }

    _REGEX = re.compile(rf'\Arho( {types.Real._REGEX.pattern[2:-2]})\Z')

    def __init__(self, density: types.Real):
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

        self.density: typing.Final[types.Real] = density


@dataclasses.dataclass
class RhoBuilder:
    """
    Builds ``Rho``.

    Attributes:
        density: Perturbed density.
    """

    density: str | float | types.Real

    def build(self):
        """
        Builds ``RhoBuilder`` into ``Rho``.

        Returns:
            ``Rho`` for ``RhoBuilder``.
        """

        density = self.density
        if isinstance(self.density, types.Real):
            density = self.density
        elif isinstance(self.density, float) or isinstance(self.density, int):
            density = types.Real(self.density)
        elif isinstance(self.density, str):
            density = types.Real.from_mcnp(self.density)

        return Rho(
            density=density,
        )

    @staticmethod
    def unbuild(ast: Rho):
        """
        Unbuilds ``Rho`` into ``RhoBuilder``

        Returns:
            ``RhoBuilder`` for ``Rho``.
        """

        return Rho(
            density=copy.deepcopy(ast.density),
        )
