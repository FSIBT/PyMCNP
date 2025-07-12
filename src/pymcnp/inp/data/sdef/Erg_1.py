import re

from . import _option
from ....utils import types
from ....utils import errors


class Erg_1(_option.SdefOption):
    """
    Represents INP erg variation #1 elements.
    """

    _KEYWORD = 'erg'

    _ATTRS = {
        'energy': types.DistributionNumber,
    }

    _REGEX = re.compile(rf'\Aerg( {types.DistributionNumber._REGEX.pattern[2:-2]})\Z')

    def __init__(self, energy: str | types.DistributionNumber):
        """
        Initializes ``Erg_1``.

        Parameters:
            energy: Kinetic energy.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.energy: types.DistributionNumber = energy

    @property
    def energy(self) -> types.DistributionNumber:
        """
        Kinetic energy

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._energy

    @energy.setter
    def energy(self, energy: str | types.DistributionNumber) -> None:
        """
        Sets ``energy``.

        Parameters:
            energy: Kinetic energy.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if energy is not None:
            if isinstance(energy, types.DistributionNumber):
                energy = energy
            elif isinstance(energy, str):
                energy = types.DistributionNumber.from_mcnp(energy)

        if energy is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, energy)

        self._energy: types.DistributionNumber = energy
