import re

from . import _option
from ... import types
from ... import errors


class Bflcl(_option.CellOption):
    """
    Represents INP `bflcl` elements.
    """

    _KEYWORD = 'bflcl'

    _ATTRS = {
        'number': types.Integer,
    }

    _REGEX = re.compile(rf'\Abflcl( {types.Integer._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)

    def __init__(self, number: str | int | types.Integer):
        """
        Initializes `Bflcl`.

        Parameters:
            number: Cell magnetic field number.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.number: types.Integer = number

    @property
    def number(self) -> types.Integer:
        """
        Cell magnetic field number

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
            number: Cell magnetic field number.

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

        if number is None or not (number >= 0):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, number)

        self._number: types.Integer = number
