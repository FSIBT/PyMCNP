import re

from . import _option
from ... import types
from ... import errors


class Erg(_option.PertOption):
    """
    Represents INP `erg` elements.
    """

    _KEYWORD = 'erg'

    _ATTRS = {
        'energy_lower_bound': types.Real,
        'energy_upper_bound': types.Real,
    }

    _REGEX = re.compile(rf'\Aerg( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)

    def __init__(self, energy_lower_bound: str | int | float | types.Real, energy_upper_bound: str | int | float | types.Real):
        """
        Initializes `Erg`.

        Parameters:
            energy_lower_bound: Lower bound for energy pertubation.
            energy_upper_bound: Upper bound for energy pertubation.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.energy_lower_bound: types.Real = energy_lower_bound
        self.energy_upper_bound: types.Real = energy_upper_bound

    @property
    def energy_lower_bound(self) -> types.Real:
        """
        Lower bound for energy pertubation

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._energy_lower_bound

    @energy_lower_bound.setter
    def energy_lower_bound(self, energy_lower_bound: str | int | float | types.Real) -> None:
        """
        Sets `energy_lower_bound`.

        Parameters:
            energy_lower_bound: Lower bound for energy pertubation.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if energy_lower_bound is not None:
            if isinstance(energy_lower_bound, types.Real):
                energy_lower_bound = energy_lower_bound
            elif isinstance(energy_lower_bound, int) or isinstance(energy_lower_bound, float):
                energy_lower_bound = types.Real(energy_lower_bound)
            elif isinstance(energy_lower_bound, str):
                energy_lower_bound = types.Real.from_mcnp(energy_lower_bound)

        if energy_lower_bound is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, energy_lower_bound)

        self._energy_lower_bound: types.Real = energy_lower_bound

    @property
    def energy_upper_bound(self) -> types.Real:
        """
        Upper bound for energy pertubation

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._energy_upper_bound

    @energy_upper_bound.setter
    def energy_upper_bound(self, energy_upper_bound: str | int | float | types.Real) -> None:
        """
        Sets `energy_upper_bound`.

        Parameters:
            energy_upper_bound: Upper bound for energy pertubation.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if energy_upper_bound is not None:
            if isinstance(energy_upper_bound, types.Real):
                energy_upper_bound = energy_upper_bound
            elif isinstance(energy_upper_bound, int) or isinstance(energy_upper_bound, float):
                energy_upper_bound = types.Real(energy_upper_bound)
            elif isinstance(energy_upper_bound, str):
                energy_upper_bound = types.Real.from_mcnp(energy_upper_bound)

        if energy_upper_bound is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, energy_upper_bound)

        self._energy_upper_bound: types.Real = energy_upper_bound
