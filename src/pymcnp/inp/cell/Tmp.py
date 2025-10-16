import re

from . import _option
from ... import types
from ... import errors


class Tmp(_option.CellOption):
    """
    Represents INP `tmp` elements.
    """

    _KEYWORD = 'tmp'

    _ATTRS = {
        'suffix': types.Integer,
        'temperature': types.Tuple(types.Real),
    }

    _REGEX = re.compile(rf'\Atmp(\d+)((?: {types.Real._REGEX.pattern[2:-2]})+?)\Z', re.IGNORECASE)

    def __init__(self, temperature: list[str] | list[float] | list[types.Real], suffix: str | int | types.Integer = None):
        """
        Initializes `Tmp`.

        Parameters:
            suffix: Thermal time index.
            temperature: Temperature at time index.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.suffix: types.Integer = suffix
        self.temperature: types.Tuple(types.Real) = temperature

    @property
    def suffix(self) -> types.Integer:
        """
        Thermal time index

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._suffix

    @suffix.setter
    def suffix(self, suffix: str | int | types.Integer) -> None:
        """
        Sets `suffix`.

        Parameters:
            suffix: Thermal time index.

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

        self._suffix: types.Integer = suffix

    @property
    def temperature(self) -> types.Tuple(types.Real):
        """
        Temperature at time index

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._temperature

    @temperature.setter
    def temperature(self, temperature: list[str] | list[float] | list[types.Real]) -> None:
        """
        Sets `temperature`.

        Parameters:
            temperature: Temperature at time index.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if temperature is not None:
            array = []
            for item in temperature:
                if isinstance(item, types.Real):
                    array.append(item)
                elif isinstance(item, int) or isinstance(item, float):
                    array.append(types.Real(item))
                elif isinstance(item, str):
                    array.append(types.Real.from_mcnp(item))
            temperature = types.Tuple(types.Real)(array)

        if temperature is None or not (min(map(lambda temp: temp, temperature)) > 0):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, temperature)

        self._temperature: types.Tuple(types.Real) = temperature
