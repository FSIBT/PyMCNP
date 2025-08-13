import re

from . import _option
from ... import types
from ... import errors


class Ein(_option.KsenOption):
    """
    Represents INP `ein` elements.
    """

    _KEYWORD = 'ein'

    _ATTRS = {
        'energies': types.Tuple(types.Real),
    }

    _REGEX = re.compile(rf'\Aein((?: {types.Real._REGEX.pattern[2:-2]})+?)\Z', re.IGNORECASE)

    def __init__(self, energies: list[str] | list[float] | list[types.Real]):
        """
        Initializes `Ein`.

        Parameters:
            energies: List of ranges for incident energies.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.energies: types.Tuple(types.Real) = energies

    @property
    def energies(self) -> types.Tuple(types.Real):
        """
        List of ranges for incident energies

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._energies

    @energies.setter
    def energies(self, energies: list[str] | list[float] | list[types.Real]) -> None:
        """
        Sets `energies`.

        Parameters:
            energies: List of ranges for incident energies.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if energies is not None:
            array = []
            for item in energies:
                if isinstance(item, types.Real):
                    array.append(item)
                elif isinstance(item, int) or isinstance(item, float):
                    array.append(types.Real(item))
                elif isinstance(item, str):
                    array.append(types.Real.from_mcnp(item))
            energies = types.Tuple(types.Real)(array)

        if energies is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, energies)

        self._energies: types.Tuple(types.Real) = energies
