import re

from . import _option
from ... import types
from ... import errors


class Erg_0(_option.SdefOption):
    """
    Represents INP `erg` elements variation #0.
    """

    _KEYWORD = 'erg'

    _ATTRS = {
        'energy': types.Real,
    }

    _REGEX = re.compile(rf'\Aerg( {types.Real._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)

    def __init__(self, energy: str | int | float | types.Real):
        """
        Initializes `Erg_0`.

        Parameters:
            energy: Kinetic energy.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.energy: types.Real = energy

    @property
    def energy(self) -> types.Real:
        """
        Kinetic energy

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
            energy: Kinetic energy.

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
