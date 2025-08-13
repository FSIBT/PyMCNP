import re

from . import _card
from .. import types
from .. import errors


class Bflcl(_card.Card):
    """
    Represents INP bflcl cards.
    """

    _KEYWORD = 'bflcl'

    _ATTRS = {
        'numbers': types.Tuple(types.Integer),
    }

    _REGEX = re.compile(rf'\Abflcl((?: {types.Integer._REGEX.pattern[2:-2]})+?)\Z', re.IGNORECASE)

    def __init__(self, numbers: list[str] | list[int] | list[types.Integer]):
        """
        Initializes `Bflcl`.

        Parameters:
            numbers: Tuple of BFLD map numbers.

        Raises:
            InpError: SEMANTICS_CARD.
        """

        self.numbers: types.Tuple(types.Integer) = numbers

    @property
    def numbers(self) -> types.Tuple(types.Integer):
        """
        Tuple of BFLD map numbers

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
            numbers: Tuple of BFLD map numbers.

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
