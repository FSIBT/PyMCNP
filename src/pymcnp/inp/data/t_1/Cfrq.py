import re

from . import _option
from ....utils import types
from ....utils import errors


class Cfrq(_option.TOption_1):
    """
    Represents INP cfrq elements.

    Attributes:
        frequency: Frequency of cycling.
    """

    _KEYWORD = 'cfrq'

    _ATTRS = {
        'frequency': types.Real,
    }

    _REGEX = re.compile(rf'\Acfrq( {types.Real._REGEX.pattern[2:-2]})\Z')

    def __init__(self, frequency: str | int | float | types.Real):
        """
        Initializes ``Cfrq``.

        Parameters:
            frequency: Frequency of cycling.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.frequency: types.Real = frequency

    @property
    def frequency(self) -> types.Real:
        """
        Gets ``frequency``.

        Returns:
            ``frequency``.
        """

        return self._frequency

    @frequency.setter
    def frequency(self, frequency: str | int | float | types.Real) -> None:
        """
        Sets ``frequency``.

        Parameters:
            frequency: Frequency of cycling.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if frequency is not None:
            if isinstance(frequency, types.Real):
                frequency = frequency
            elif isinstance(frequency, int):
                frequency = types.Real(frequency)
            elif isinstance(frequency, float):
                frequency = types.Real(frequency)
            elif isinstance(frequency, str):
                frequency = types.Real.from_mcnp(frequency)
            else:
                raise TypeError

        if frequency is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, frequency)

        self._frequency: types.Real = frequency
