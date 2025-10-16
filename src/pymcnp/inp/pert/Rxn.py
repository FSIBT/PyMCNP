import re

from . import _option
from ... import types
from ... import errors


class Rxn(_option.PertOption):
    """
    Represents INP `rxn` elements.
    """

    _KEYWORD = 'rxn'

    _ATTRS = {
        'numbers': types.Tuple(types.Integer),
    }

    _REGEX = re.compile(rf'\Arxn((?: {types.Integer._REGEX.pattern[2:-2]})+?)\Z', re.IGNORECASE)

    def __init__(self, numbers: list[str] | list[int] | list[types.Integer]):
        """
        Initializes `Rxn`.

        Parameters:
            numbers: ENDF/B reaction number.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.numbers: types.Tuple(types.Integer) = numbers

    @property
    def numbers(self) -> types.Tuple(types.Integer):
        """
        ENDF/B reaction number

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._numbers

    @numbers.setter
    def numbers(self, numbers: list[str] | list[int] | list[types.Integer]) -> None:
        """
        Sets `numbers`.

        Parameters:
            numbers: ENDF/B reaction number.

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
            numbers = types.Tuple(types.Integer)(array)

        if numbers is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, numbers)

        self._numbers: types.Tuple(types.Integer) = numbers
