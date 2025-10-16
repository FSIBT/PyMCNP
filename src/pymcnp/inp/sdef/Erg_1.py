import re

from . import _option
from ... import types
from ... import errors


class Erg_1(_option.SdefOption):
    """
    Represents INP `erg` elements variation #1.
    """

    _KEYWORD = 'erg'

    _ATTRS = {
        'energy': types.Distribution,
    }

    _REGEX = re.compile(rf'\Aerg( {types.Distribution._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)

    def __init__(self, energy: str | types.Distribution):
        """
        Initializes `Erg_1`.

        Parameters:
            energy: Kinetic energy.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.energy: types.Distribution = energy

    @property
    def energy(self) -> types.Distribution:
        """
        Kinetic energy

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._energy

    @energy.setter
    def energy(self, energy: str | types.Distribution) -> None:
        """
        Sets `energy`.

        Parameters:
            energy: Kinetic energy.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if energy is not None:
            if isinstance(energy, types.Distribution):
                energy = energy
            elif isinstance(energy, str):
                energy = types.Distribution.from_mcnp(energy)

        if energy is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, energy)

        self._energy: types.Distribution = energy
