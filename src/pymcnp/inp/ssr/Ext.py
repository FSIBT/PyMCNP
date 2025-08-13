import re

from . import _option
from ... import types
from ... import errors


class Ext(_option.SsrOption):
    """
    Represents INP `ext` elements.
    """

    _KEYWORD = 'ext'

    _ATTRS = {
        'number': types.Distribution,
    }

    _REGEX = re.compile(rf'\Aext( {types.Distribution._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)

    def __init__(self, number: str | types.Distribution):
        """
        Initializes `Ext`.

        Parameters:
            number: Distribution number for baising sampling.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.number: types.Distribution = number

    @property
    def number(self) -> types.Distribution:
        """
        Distribution number for baising sampling

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._number

    @number.setter
    def number(self, number: str | types.Distribution) -> None:
        """
        Sets `number`.

        Parameters:
            number: Distribution number for baising sampling.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if number is not None:
            if isinstance(number, types.Distribution):
                number = number
            elif isinstance(number, str):
                number = types.Distribution.from_mcnp(number)

        if number is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, number)

        self._number: types.Distribution = number
