import re

from . import _card
from .. import types
from .. import errors


class Cosy(_card.Card):
    """
    Represents INP cosy cards.
    """

    _KEYWORD = 'cosy'

    _ATTRS = {
        'numbers': types.Tuple(types.Integer),
    }

    _REGEX = re.compile(rf'\Acosy((?: {types.Integer._REGEX.pattern[2:-2]})+?)\Z', re.IGNORECASE)

    def __init__(self, numbers: list[str] | list[int] | list[types.Integer]):
        """
        Initializes `Cosy`.

        Parameters:
            numbers: Tuple of COSY map numbers.

        Raises:
            InpError: SEMANTICS_CARD.
        """

        self.numbers: types.Tuple(types.Integer) = numbers

    @property
    def numbers(self) -> types.Tuple(types.Integer):
        """
        Tuple of COSY map numbers

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._numbers

    @numbers.setter
    def numbers(self, numbers: list[str] | list[int] | list[types.Integer]) -> None:
        """
        Sets `numbers`.

        Parameters:
            numbers: Tuple of COSY map numbers.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if numbers is not None:
            array = []
            for item in numbers:
                if isinstance(item, types.Integer):
                    array.append(item)
                elif isinstance(item, int):
                    array.append(types.Integer(item))
                elif isinstance(item, str):
                    array.append(types.Integer.from_mcnp(item))
            numbers = types.Tuple(types.Integer)(array)

        if numbers is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_CARD, numbers)

        self._numbers: types.Tuple(types.Integer) = numbers
