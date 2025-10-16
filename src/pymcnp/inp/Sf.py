import re

from . import _card
from .. import types
from .. import errors


class Sf(_card.Card):
    """
    Represents INP `sf` cards.
    """

    _KEYWORD = 'sf'

    _ATTRS = {
        'suffix': types.Integer,
        'numbers': types.Tuple(types.Integer),
    }

    _REGEX = re.compile(rf'\Asf(\d+)((?: {types.Integer._REGEX.pattern[2:-2]})+?)\Z', re.IGNORECASE)

    def __init__(self, suffix: str | int | types.Integer, numbers: list[str] | list[int] | list[types.Integer]):
        """
        Initializes `Sf`.

        Parameters:
            suffix: Data card option suffix.
            numbers: Tallies for problem surface numbers to flag.

        Raises:
            InpError: SEMANTICS_CARD.
        """

        self.suffix: types.Integer = suffix
        self.numbers: types.Tuple(types.Integer) = numbers

    @property
    def suffix(self) -> types.Integer:
        """
        Data card option suffix

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._suffix

    @suffix.setter
    def suffix(self, suffix: str | int | types.Integer) -> None:
        """
        Sets `suffix`.

        Parameters:
            suffix: Data card option suffix.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if suffix is not None:
            if isinstance(suffix, types.Integer):
                suffix = suffix
            elif isinstance(suffix, int):
                suffix = types.Integer(suffix)
            elif isinstance(suffix, str):
                suffix = types.Integer.from_mcnp(suffix)

        if suffix is None or not (suffix <= 99_999_999):
            raise errors.InpError(errors.InpCode.SEMANTICS_CARD, suffix)

        self._suffix: types.Integer = suffix

    @property
    def numbers(self) -> types.Tuple(types.Integer):
        """
        Tallies for problem surface numbers to flag

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
            numbers: Tallies for problem surface numbers to flag.

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
