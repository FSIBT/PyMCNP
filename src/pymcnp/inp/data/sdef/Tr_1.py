import re

from . import _option
from .... import types
from .... import errors


class Tr_1(_option.SdefOption):
    """
    Represents INP tr variation #1 elements.
    """

    _KEYWORD = 'tr'

    _ATTRS = {
        'number': types.Distribution,
    }

    _REGEX = re.compile(rf'\Atr( {types.Distribution._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)

    def __init__(self, number: str | int | types.Distribution):
        """
        Initializes ``Tr_1``.

        Parameters:
            number: Particle weight.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.number: types.Distribution = number

    @property
    def number(self) -> types.Distribution:
        """
        Particle weight

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._number

    @number.setter
    def number(self, number: str | int | types.Distribution) -> None:
        """
        Sets ``number``.

        Parameters:
            number: Particle weight.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if number is not None:
            if isinstance(number, types.Distribution):
                number = number
            elif isinstance(number, int):
                number = types.Distribution(number)
            elif isinstance(number, str):
                number = types.Distribution.from_mcnp(number)

        if number is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, number)

        self._number: types.Distribution = number
