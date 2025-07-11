import re

from . import _option
from ....utils import types
from ....utils import errors


class Rho(_option.PertOption):
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

    def __init__(self, density: str | int | float | types.Real):
        """
        Initializes ``Rho``.

        Parameters:
            density: Perturbed density.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.density: types.Real = density

    @property
    def density(self) -> types.Real:
        """
        Gets ``density``.

        Returns:
            ``density``.
        """

        return self._density

    @density.setter
    def density(self, density: str | int | float | types.Real) -> None:
        """
        Sets ``density``.

        Parameters:
            density: Perturbed density.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if density is not None:
            if isinstance(density, types.Real):
                density = density
            elif isinstance(density, int):
                density = types.Real(density)
            elif isinstance(density, float):
                density = types.Real(density)
            elif isinstance(density, str):
                density = types.Real.from_mcnp(density)
            else:
                raise TypeError

        if density is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, density)

        self._density: types.Real = density
