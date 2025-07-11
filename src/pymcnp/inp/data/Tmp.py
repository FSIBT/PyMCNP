import re

from . import _option
from ...utils import types
from ...utils import errors


class Tmp(_option.DataOption):
    """
    Represents INP tmp elements.

    Attributes:
        suffix: Data card option suffix.
        temperatures: Cell temperatrues.
    """

    _KEYWORD = 'tmp'

    _ATTRS = {
        'suffix': types.Integer,
        'temperatures': types.Tuple[types.Real],
    }

    _REGEX = re.compile(rf'\Atmp(\d+)?((?: {types.Real._REGEX.pattern[2:-2]})+?)\Z')

    def __init__(self, temperatures: list[str] | list[float] | list[types.Real], suffix: str | int | types.Integer = None):
        """
        Initializes ``Tmp``.

        Parameters:
            suffix: Data card option suffix.
            temperatures: Cell temperatrues.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.suffix: types.Integer = suffix
        self.temperatures: types.Tuple[types.Real] = temperatures

    @property
    def suffix(self) -> types.Integer:
        """
        Gets ``suffix``.

        Returns:
            ``suffix``.
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
            else:
                raise TypeError

        self._suffix: types.Integer = suffix

    @property
    def temperatures(self) -> types.Tuple[types.Real]:
        """
        Gets ``temperatures``.

        Returns:
            ``temperatures``.
        """

        return self._temperatures

    @temperatures.setter
    def temperatures(self, temperatures: list[str] | list[float] | list[types.Real]) -> None:
        """
        Sets ``temperatures``.

        Parameters:
            temperatures: Cell temperatrues.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if temperatures is not None:
            array = []
            for item in temperatures:
                if isinstance(item, types.Real):
                    array.append(item)
                elif isinstance(item, int):
                    array.append(types.Real(item))
                elif isinstance(item, float):
                    array.append(types.Real(item))
                elif isinstance(item, str):
                    array.append(types.Real.from_mcnp(item))
                else:
                    raise TypeError
            temperatures = types.Tuple(array)

        if temperatures is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, temperatures)

        self._temperatures: types.Tuple[types.Real] = temperatures
