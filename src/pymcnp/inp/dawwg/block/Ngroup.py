import re

from . import _option
from .... import types
from .... import errors


class Ngroup(_option.BlockOption):
    """
    Represents INP `ngroup` elements.
    """

    _KEYWORD = 'ngroup'

    _ATTRS = {
        'value': types.Integer,
    }

    _REGEX = re.compile(rf'\Angroup( {types.Integer._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)

    def __init__(self, value: str | int | types.Integer):
        """
        Initializes `Ngroup`.

        Parameters:
            value: Number of energy groups.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.value: types.Integer = value

    @property
    def value(self) -> types.Integer:
        """
        Number of energy groups

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._value

    @value.setter
    def value(self, value: str | int | types.Integer) -> None:
        """
        Sets `value`.

        Parameters:
            value: Number of energy groups.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if value is not None:
            if isinstance(value, types.Integer):
                value = value
            elif isinstance(value, int):
                value = types.Integer(value)
            elif isinstance(value, str):
                value = types.Integer.from_mcnp(value)

        if value is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, value)

        self._value: types.Integer = value
