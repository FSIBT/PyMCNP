import re

from . import _entry
from .... import types
from .... import errors


class Bias(_entry.DnebEntry):
    """
    Represents INP `bias` elements.
    """

    _KEYWORD = ''

    _ATTRS = {
        'weight': types.Real,
        'energy': types.Real,
    }

    _REGEX = re.compile(rf'\A({types.Real._REGEX.pattern[2:-2]}) ({types.Real._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)

    def __init__(self, weight: str | int | float | types.Real, energy: str | int | float | types.Real):
        """
        Initializes `Bias`.

        Parameters:
            weight: Weight for bias.
            energy: Energy boundary for bias.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.weight: types.Real = weight
        self.energy: types.Real = energy

    @property
    def weight(self) -> types.Real:
        """
        Weight for bias

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._weight

    @weight.setter
    def weight(self, weight: str | int | float | types.Real) -> None:
        """
        Sets `weight`.

        Parameters:
            weight: Weight for bias.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if weight is not None:
            if isinstance(weight, types.Real):
                weight = weight
            elif isinstance(weight, int) or isinstance(weight, float):
                weight = types.Real(weight)
            elif isinstance(weight, str):
                weight = types.Real.from_mcnp(weight)

        if weight is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, weight)

        self._weight: types.Real = weight

    @property
    def energy(self) -> types.Real:
        """
        Energy boundary for bias

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
            energy: Energy boundary for bias.

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
