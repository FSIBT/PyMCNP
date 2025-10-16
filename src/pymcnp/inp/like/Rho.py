import re

from . import _option
from ... import types
from ... import errors


class Rho(_option.LikeOption):
    """
    Represents INP `rho` elements.
    """

    _KEYWORD = 'rho'

    _ATTRS = {
        'density': types.Real,
    }

    _REGEX = re.compile(rf'\Arho( {types.Real._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)

    def __init__(self, density: types.Real):
        """
        Initializes `Rho`.

        Parameters:
            density: Cell density.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.density: types.Real = density

    @property
    def density(self) -> types.Real:
        """
        Gets `density`.

        Returns:
            `density`.
        """

        return self._density

    @density.setter
    def density(self, density: str | int | float | types.Real) -> None:
        """
        Sets `density`.

        Parameters:
            density: Cell density.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if density is not None:
            if isinstance(density, types.Real):
                density = density
            elif isinstance(density, float) or isinstance(density, int):
                density = types.Real(density)
            elif isinstance(density, str):
                density = types.Real.from_mcnp(density)

        if density is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, density)

        self._density: types.Real = density
