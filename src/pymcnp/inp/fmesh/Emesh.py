import re

from . import _option
from ... import types
from ... import errors


class Emesh(_option.FmeshOption):
    """
    Represents INP `emesh` elements.
    """

    _KEYWORD = 'emesh'

    _ATTRS = {
        'energy': types.Real,
    }

    _REGEX = re.compile(rf'\Aemesh( {types.Real._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)

    def __init__(self, energy: str | int | float | types.Real):
        """
        Initializes `Emesh`.

        Parameters:
            energy: Values of mesh points in energy.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.energy: types.Real = energy

    @property
    def energy(self) -> types.Real:
        """
        Values of mesh points in energy

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._energy

    @energy.setter
    def energy(self, energy: str | int | float | types.Real) -> None:
        """
        Sets `energy`.

        Parameters:
            energy: Values of mesh points in energy.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if energy is not None:
            if isinstance(energy, types.Real):
                energy = energy
            elif isinstance(energy, int) or isinstance(energy, float):
                energy = types.Real(energy)
            elif isinstance(energy, str):
                energy = types.Real.from_mcnp(energy)

        if energy is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, energy)

        self._energy: types.Real = energy
