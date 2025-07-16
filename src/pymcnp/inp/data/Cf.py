import re

from . import _option
from ... import types
from ... import errors


class Cf(_option.DataOption):
    """
    Represents INP cf elements.
    """

    _KEYWORD = 'cf'

    _ATTRS = {
        'suffix': types.Integer,
        'numbers': types.Tuple[types.Integer],
    }

    _REGEX = re.compile(rf'\Acf(\d+)((?: {types.Integer._REGEX.pattern[2:-2]})+?)\Z')

    def __init__(self, suffix: str | int | types.Integer, numbers: list[str] | list[int] | list[types.Integer]):
        """
        Initializes ``Cf``.

        Parameters:
            suffix: Data card option suffix.
            numbers: Tallies for problem cell numbers to flag.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.suffix: types.Integer = suffix
        self.numbers: types.Tuple[types.Integer] = numbers

    @property
    def suffix(self) -> types.Integer:
        """
        Data card option suffix

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._suffix

    @suffix.setter
    def suffix(self, suffix: str | int | types.Integer) -> None:
        """
        Sets ``suffix``.

        Parameters:
            suffix: Data card option suffix.

        Raises:
            InpError: SEMANTICS_OPTION.
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
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, suffix)

        self._suffix: types.Integer = suffix

    @property
    def numbers(self) -> types.Tuple[types.Integer]:
        """
        Tallies for problem cell numbers to flag

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._numbers

    @numbers.setter
    def numbers(self, numbers: list[str] | list[int] | list[types.Integer]) -> None:
        """
        Sets ``numbers``.

        Parameters:
            numbers: Tallies for problem cell numbers to flag.

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
            numbers = types.Tuple(array)

        if numbers is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, numbers)

        self._numbers: types.Tuple[types.Integer] = numbers
