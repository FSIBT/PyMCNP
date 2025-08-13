import re

from . import _card
from .. import types


class Void(_card.Card):
    """
    Represents INP `void` cards.
    """

    _KEYWORD = 'void'

    _ATTRS = {
        'numbers': types.Tuple(types.Integer),
    }

    _REGEX = re.compile(rf'\Avoid((?: {types.Integer._REGEX.pattern[2:-2]})+?)?\Z', re.IGNORECASE)

    def __init__(self, numbers: list[str] | list[int] | list[types.Integer] = None):
        """
        Initializes `Void`.

        Parameters:
            numbers: Tuple of cell numbers.

        Raises:
            InpError: SEMANTICS_CARD.
        """

        self.numbers: types.Tuple(types.Integer) = numbers

    @property
    def numbers(self) -> types.Tuple(types.Integer):
        """
        Tuple of cell numbers

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
            numbers: Tuple of cell numbers.

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

        self._numbers: types.Tuple(types.Integer) = numbers
