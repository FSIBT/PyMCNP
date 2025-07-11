import re

from . import _option
from ....utils import types
from ....utils import errors


class Old(_option.SsrOption):
    """
    Represents INP old elements.

    Attributes:
        numbers: Tuple of surface numbers from subset of surfaces on SSW card.
    """

    _KEYWORD = 'old'

    _ATTRS = {
        'numbers': types.Tuple[types.Integer],
    }

    _REGEX = re.compile(rf'\Aold((?: {types.Integer._REGEX.pattern[2:-2]})+?)\Z')

    def __init__(self, numbers: list[str] | list[int] | list[types.Integer]):
        """
        Initializes ``Old``.

        Parameters:
            numbers: Tuple of surface numbers from subset of surfaces on SSW card.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.numbers: types.Tuple[types.Integer] = numbers

    @property
    def numbers(self) -> types.Tuple[types.Integer]:
        """
        Gets ``numbers``.

        Returns:
            ``numbers``.
        """

        return self._numbers

    @numbers.setter
    def numbers(self, numbers: list[str] | list[int] | list[types.Integer]) -> None:
        """
        Sets ``numbers``.

        Parameters:
            numbers: Tuple of surface numbers from subset of surfaces on SSW card.

        Raises:
            InpError: SEMANTICS_OPTION.
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
                else:
                    raise TypeError
            numbers = types.Tuple(array)

        if numbers is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, numbers)

        self._numbers: types.Tuple[types.Integer] = numbers
