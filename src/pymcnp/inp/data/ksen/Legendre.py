import re

from . import _option
from ....utils import types
from ....utils import errors


class Legendre(_option.KsenOption):
    """
    Represents INP legendre elements.

    Attributes:
        number: Order of Legendre moments to calculate sensitivities.
    """

    _KEYWORD = 'legendre'

    _ATTRS = {
        'number': types.Integer,
    }

    _REGEX = re.compile(rf'\Alegendre( {types.Integer._REGEX.pattern[2:-2]})\Z')

    def __init__(self, number: str | int | types.Integer):
        """
        Initializes ``Legendre``.

        Parameters:
            number: Order of Legendre moments to calculate sensitivities.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.number: types.Integer = number

    @property
    def number(self) -> types.Integer:
        """
        Gets ``number``.

        Returns:
            ``number``.
        """

        return self._number

    @number.setter
    def number(self, number: str | int | types.Integer) -> None:
        """
        Sets ``number``.

        Parameters:
            number: Order of Legendre moments to calculate sensitivities.

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
            else:
                raise TypeError

        if number is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, number)

        self._number: types.Integer = number
