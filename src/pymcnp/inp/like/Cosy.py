import re

from . import _option
from ... import types
from ... import errors


class Cosy(_option.LikeOption):
    """
    Represents INP `cosy` elements.
    """

    _KEYWORD = 'cosy'

    _ATTRS = {
        'number': types.Integer,
    }

    _REGEX = re.compile(rf'\Acosy( {types.Integer._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)

    def __init__(self, number: str | int | types.Integer):
        """
        Initializes `Cosy`.

        Parameters:
            number: Cell cosy map number.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.number: types.Integer = number

    @property
    def number(self) -> types.Integer:
        """
        Gets `number`.

        Returns:
            `number`.
        """

        return self._number

    @number.setter
    def number(self, number: str | int | types.Integer) -> None:
        """
        Sets `number`.

        Parameters:
            number: Cell cosy map number.

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

        if number is None or number not in {1, 2, 3, 4, 5, 6}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, number)

        self._number: types.Integer = number
