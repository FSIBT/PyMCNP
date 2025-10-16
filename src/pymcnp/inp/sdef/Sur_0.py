import re

from . import _option
from ... import types
from ... import errors


class Sur_0(_option.SdefOption):
    """
    Represents INP `sur` elements variation #0.
    """

    _KEYWORD = 'sur'

    _ATTRS = {
        'number': types.Integer,
    }

    _REGEX = re.compile(rf'\Asur( {types.Integer._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)

    def __init__(self, number: str | int | types.Integer):
        """
        Initializes `Sur_0`.

        Parameters:
            number: Surface number.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.number: types.Integer = number

    @property
    def number(self) -> types.Integer:
        """
        Surface number

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._number

    @number.setter
    def number(self, number: str | int | types.Integer) -> None:
        """
        Sets `number`.

        Parameters:
            number: Surface number.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if number is not None:
            if isinstance(number, types.Integer):
                number = number
            elif isinstance(number, int):
                number = types.Integer(number)
            elif isinstance(number, str):
                number = types.Integer.from_mcnp(number)

        if number is None or not (isinstance(number.value, types.Jump) or (number >= 0 and number <= 99_999_999)):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, number)

        self._number: types.Integer = number
