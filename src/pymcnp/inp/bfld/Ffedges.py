import re

from . import _option
from ... import types
from ... import errors


class Ffedges(_option.BfldOption):
    """
    Represents INP `ffedges` elements.
    """

    _KEYWORD = 'ffedges'

    _ATTRS = {
        'numbers': types.Tuple(types.Real),
    }

    _REGEX = re.compile(rf'\Affedges((?: {types.Real._REGEX.pattern[2:-2]})+?)\Z', re.IGNORECASE)

    def __init__(self, numbers: list[str] | list[float] | list[types.Real]):
        """
        Initializes `Ffedges`.

        Parameters:
            numbers: Surface numbers to apply field fringe edges.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.numbers: types.Tuple(types.Real) = numbers

    @property
    def numbers(self) -> types.Tuple(types.Real):
        """
        Surface numbers to apply field fringe edges

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._numbers

    @numbers.setter
    def numbers(self, numbers: list[str] | list[float] | list[types.Real]) -> None:
        """
        Sets `numbers`.

        Parameters:
            numbers: Surface numbers to apply field fringe edges.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if numbers is not None:
            array = []
            for item in numbers:
                if isinstance(item, types.Real):
                    array.append(item)
                elif isinstance(item, int) or isinstance(item, float):
                    array.append(types.Real(item))
                elif isinstance(item, str):
                    array.append(types.Real.from_mcnp(item))
            numbers = types.Tuple(types.Real)(array)

        if numbers is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, numbers)

        self._numbers: types.Tuple(types.Real) = numbers
